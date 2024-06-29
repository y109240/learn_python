## 게시판


# board/models.py
from django.db import models
class Board( models.Model ) :           # board_board
    num = models.AutoField( primary_key=True, verbose_name="글번호" )
    writer = models.CharField( max_length=50, null=False, verbose_name="작성자" )
    subject = models.CharField( max_length=300, null=False, verbose_name="글제목" )
    passwd = models.CharField( max_length=50, null=False, verbose_name="비밀번호" )
    content = models.TextField( max_length=2000, null=False, verbose_name="글내용" )
    readcount = models.IntegerField( default=0, verbose_name="조회수" )
    ref = models.IntegerField( verbose_name="그룹화아이디" )
    restep = models.IntegerField( verbose_name="글순서" )
    relevel = models.IntegerField( verbose_name="글레벨" )
    regdate = models.DateTimeField( auto_now_add=True, blank=True, verbose_name="작성일" )
    ip = models.CharField( max_length=20, verbose_name="아이피" )


# board/admin.py
from django.contrib import admin
from board.models import Board
class BoardAdmin( admin.ModelAdmin ) :
    list_display = ( "num", "writer", "subject", "passwd", "content", "readcount",
                    "ref", "restep", "relevel", "regdate", "ip" )
admin.site.register( Board, BoardAdmin )


# board\urls.py
from django.urls.conf import path
from django.views.generic.base import TemplateView
from board import views
urlpatterns = [
    path( "", views.ListView.as_view(), name="list" ),
    # localhost:8000/board/
    path( "write", views.WriteView.as_view(), name="write" ),
    # localhost:8000/board/write
    path( "detail", views.DetailView.as_view(), name="detail" ),
    # localhost:8000/board/detail
]


# board\views.py
from django.shortcuts import render, redirect
import logging
from django.views.generic.base import View
from board.models import Board
from django.template import loader
from django.http.response import HttpResponse
from django.utils.dateformat import DateFormat
from _datetime import datetime
logger = logging.getLogger( __name__ )

PAGE_SIZE = 10
PAGE_BLOCK = 10

class ListView( View ) :
    def get( self, request ) :
        count = Board.objects.all().count()
        pagenum = request.GET.get( "pagenum" )
        if not pagenum :
            pagenum = "1"
        pagenum = int( pagenum )
        start = ( pagenum - 1 ) * int( PAGE_SIZE )          # ( 5-1 ) * 10 + 1    41
        end = start + int( PAGE_SIZE )                      # 41 + 10             51
        if end > count :
            end = count
        dtos = Board.objects.order_by( "-ref", "restep" )[start:end]    # 41:50
        number = count - ( pagenum - 1 ) * int( PAGE_SIZE )             # 50 - ( 2-1 ) * 10
        
        pagecount = count // int( PAGE_SIZE )
        if count % int( PAGE_SIZE ) > 0 :
            pagecount += 1
        startpage = pagenum // int( PAGE_BLOCK ) * int( PAGE_BLOCK ) + 1    # 19  19//10*10+1    11
        endpage = startpage + int( PAGE_BLOCK ) - 1                         # 11 + 10 -1         20
        if endpage > pagecount :
            endpage = pagecount            
        pages = range( startpage, endpage+1 )      
        
        context = {
            "count" : count,
            "dtos" : dtos,
            "pagenum" : pagenum,
            "number" : number,
            "pages" : pages,
            "startpage" : startpage,
            "endpage" : endpage,
            "pageblock" : PAGE_BLOCK,
            "pagecount" : pagecount
            }
        template = loader.get_template( "board/list.html" )
        return HttpResponse( template.render( context, request ) )
    def post( self, request ) :
        pass

class WriteView( View ) :
    def get( self, request ) :
        ref = 1
        restep = 0
        relevel = 0
        num = request.GET.get( "num" )
        if num == None :
            # 제목글        list.html     GET     데이터 X
            try :
                # 글이 있는 경우
                maxnum = Board.objects.order_by( "-num" ).values()[0]["num"]
                ref = maxnum + 1        # 그룹화아이디 = 글번호최대값 + 1
            except IndexError :
                # 글이 없는 경우               
                ref = 1
        else :
            # 답글         content.html   GET     num ref restep relevel
            ref = request.GET["ref"]
            restep = request.GET["restep"]
            relevel = request.GET["relevel"]
            res = Board.objects.filter( ref__exact=ref ).filter( restep__gt=restep )
            for re in res :
                re.restep = int( re.restep ) + 1
                re.save()
            restep = int( restep ) + 1
            relevel = int( relevel ) + 1         
        memid = request.session.get( "memid" )        
        context = {
            "memid" : memid,
            "num" : num,
            "ref" : ref,
            "restep" : restep,
            "relevel" : relevel
            }        
        template = loader.get_template( "board/write.html" )
        return HttpResponse( template.render( context, request ) )    
    def post( self, request ) :
        dto = Board(
            # num            자동증가
            writer = request.POST["writer"],
            subject = request.POST["subject"],
            passwd = request.POST["passwd"],
            content = request.POST["content"],
            readcount = 0,
            ref = request.POST["ref"],
            restep = request.POST["restep"],
            relevel = request.POST["relevel"],
            regdate = DateFormat( datetime.now() ).format( "Y-m-d" ),
            ip = request.META.get( "REMOTE_ADDR" )
            )
        dto.save()
        return redirect( "http://localhost:8000/board" )

class DetailView( View ) :
    def get( self, request ) :         
        pagenum = request.GET["pagenum"]
        num = request.GET["num"]
        number = request.GET["number"]
        dto = Board.objects.get( num = num )
        if dto.ip != request.META.get( "REMOTE_ADDR" ) :
            dto.readcount += 1
            dto.save()
        context = {
            "pagenum" : pagenum,
            "dto" : dto,
            "number" : number
            }
        template = loader.get_template( "board/detail.html" )
        return HttpResponse( template.render( context, request ) )        
    def post( self, request ) :
        pass