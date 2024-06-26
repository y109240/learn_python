## 회원가입


# member/models.py
from django.db import models
from member.choice import DEPART_CHOICE

class Member( models.Model ) :          # member_member
    id = models.CharField( max_length=50, verbose_name="아이디", primary_key=True )
    passwd = models.CharField( max_length=50, verbose_name="비밀번호", null=False )
    name = models.CharField( max_length=50, verbose_name="이름", null=False )
    email = models.CharField( max_length=100, verbose_name="이메일", null=True )
    tel = models.CharField( max_length=30, verbose_name="전화번호", null=True )
    depart = models.CharField( max_length=20, verbose_name="부서명", null=False, choices=DEPART_CHOICE )
    logtime = models.DateTimeField( auto_now_add=True, verbose_name="가입일자", null=False, blank=True )


# member/admin.py
from django.contrib import admin
from member.models import Member
class MemberAdmin( admin.ModelAdmin ) :
    list_display = ( "id", "passwd", "name", "email", "tel", "depart" )
admin.site.register( Member, MemberAdmin ) 


# member/urls.py
from django.views.generic.base import TemplateView
from django.urls.conf import path
from member import views
urlpatterns = [
    path( "", views.MainView.as_view(), name="main" ),
    # localhost:8000/member/
    path( "write", views.WriteView.as_view(), name="write" ),
    # localhost:8000/member/write
    path( "confirm", views.ConfirmView.as_view(), name="confirm" ),
    # localhost:8000/member/confirm
    path( "login", views.LoginView.as_view(), name="login" ),
    # localhost:8000/member/login
    path( "logout", views.LogoutView.as_view(), name="logout" ),
    # localhost:8000/member/logout
    path( "delete", views.DeleteView.as_view(), name="delete" ),
    # localhost:8000/member/delete
    path( "update", views.UpdateView.as_view(), name="update" ),
    # localhost:8000/member/update
    path( "updatepro", views.UpdateproView.as_view(), name="updatepro" ),
    # localhost:8000/member/updatepro
]


# member\views.py
from django.shortcuts import render, redirect
import logging
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.template import loader
from member.models import Member
from django.utils.dateformat import DateFormat
from _datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.conf.locale import id
logger = logging.getLogger( __name__ )

class MainView( View ) :
    def get( self, request ) :
        memid = request.session.get( "memid" )
        if memid : 
            # 로그인이 된 상태
            context = {
                "memid" : memid
            }
        else :
            # 로그인이 안 된 상태
            context = {}
        template = loader.get_template( "member/main.html" )
        return HttpResponse( template.render( context, request ) )        
    def post( self, request ) :
        pass

class WriteView( View ) :
    def get( self, request ) :    
        template = loader.get_template( "member/write.html" )
        return HttpResponse( template.render( {}, request ) )
    def post( self, request ) :
        id = request.POST["id"]
        passwd = request.POST["passwd"]
        name = request.POST["name"]
                
        email = ""
        email1 = request.POST["email1"]
        email2 = request.POST["email2"]
        if email1 :
            if email2 == "0" :
                # 직접입력
                email = email1
            else :
                # 선택입력
                email = email1 + "@" + email2
    
        tel = ""
        tel1 = request.POST["tel1"]
        tel2 = request.POST["tel2"]
        tel3 = request.POST["tel3"]
        if tel1 and tel2 and tel3 :
            tel = tel1 + "-" + tel2 + "-" + tel3
        
        depart = request.POST["depart"]
        
        dto = Member(
            id = id,
            passwd = passwd,
            name = name,
            email = email,
            tel = tel,
            depart = depart,
            logtime = DateFormat( datetime.now() ).format( "Y-m-d" )            
            ) 
        dto.save()
        logger.debug( id + "가입성공" )
        return redirect( "login" )

class ConfirmView( View ) :
    def get( self, request ) :
        id = request.GET["id"]        
        result = 0
        try :
            Member.objects.get( id=id )
            result = 1
        except ObjectDoesNotExist :
            result = 0
        context = { 
            "result" : result,
            "id" : id
        }    
        template = loader.get_template( "member/confirm.html" )
        return HttpResponse( template.render( context, request ) )       
    def post( self, request ) :
        pass     

class LoginView( View ) :    
    def get( self, request ) :
        template = loader.get_template( "member/login.html" )
        return HttpResponse( template.render( {}, request ) )        
    def post( self, request ) :    
        id = request.POST["id"]
        passwd = request.POST["passwd"]        
        try :
            dto = Member.objects.get( id = id )
            if passwd == dto.passwd :
                request.session["memid"] = id
                return redirect( "http://localhost:8000/member" )
            else : 
                message = "입력하신 비밀번호가 다릅니다"
        except ObjectDoesNotExist :
            message = "입력하신 아이디가 없습니다"
        template = loader.get_template( "member/login.html" )
        context = {
            "message" : message
            }
        return HttpResponse( template.render( context, request ) )

class LogoutView( View ):
    def get( self, request ):    
        del( request.session["memid"] )
        return redirect( "http://localhost:8000/member" )

class DeleteView( View ):
    def get( self, request ):
        template = loader.get_template( "member/delete.html" )
        return HttpResponse( template.render( {}, request ) )
    def post ( self, request ):
        id = request.session["memid"]
        passwd = request.POST["passwd"]
        dto = Member.objects.get( id=id )
        if passwd == dto.passwd:
            dto.delete()
            del( request.session["memid"] )
            logger.debug( id + "탈퇴성공" )
            return redirect( "http://localhost:8000/member")
        else:
            message = "입력하신 비밀번호가 다릅니다."
            context ={
                "message" : message
                }
            template = loader.get_template( "member/delete.html" )
            return HttpResponse( template.render( context, request ) )

class UpdateView( View ):
    def get( self, request ):
        template = loader.get_template( "member/update.html" )
        return HttpResponse( template.render( {}, request ) )
    def post( self, request ):
        id = request.session["memid"]
        passwd = request.POST["passwd"]
        dto = Member.objects.get( id=id )
        if passwd == dto.passwd:
            context = {
                "dto" : dto
                }
            if dto.email:
                e = dto.email.split( "@" )
                context["e"] = e
            if dto.tel:
                t = dto.tel.split( "-" )
                context["t"] = t
            template = loader.get_template( "member/updateview.html" )
            return HttpResponse( template.render( context, request ) )   
        else:
            message = "입력하신 비밀번호가 다릅니다."
            context = {
                "message" : message
                }
            template = loader.get_template( "member/update.html" )
            return HttpResponse( template.render( context, request ) )

class UpdateproView( View ):
    def get( self, request ):
        pass
    def post( self, request ):
        id = request.session["memid"]
        passwd = request.POST["passwd"]
        name = request.POST["name"]
        email = ""
        email1 = request.POST["email1"]
        email2 = request.POST["email2"]
        if( email and email2 ):
            email = email1 + "@" + email2
        tel = ""
        tel1 = request.POST["tel1"]
        tel2 = request.POST["tel2"]
        tel3 = request.POST["tel3"]
        if( tel1 and tel2 and tel3 ):
            tel = tel1 + "-" + tel2 + "-" + tel3
        depart = request.POST["depart"]
        logtime = request.POST["logtime"]
        dto = Member(
            id = id,
            passwd = passwd,
            name = name,
            email = email,
            tel = tel,
            depart = depart,
            logtime = logtime
            )
        dto.save()
        return redirect( "http://localhost:8000" )
