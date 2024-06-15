## Guestbook ##


# models.py
from django.db import models
from _datetime import datetime

class Guestbook( models.Model ):
    idx = models.AutoField( primary_key=True )
    name = models.CharField( null=False, max_length=50 )
    email = models.EmailField( null=False, max_length=50 )
    passwd = models.CharField( null=False, max_length=50 )
    content = models.TextField( null=False )
    postdate = models.DateField( default=datetime.now, blank=True )


# admin.py
from django.contrib import admin
from guestbook.models import Guestbook

class GuestbookAdmin( admin.ModelAdmin ):
    list_display = ( "name", "email", "passwd", "content" )
admin.site.register( Guestbook, GuestbookAdmin )


# urls.py
from django.urls.conf import path
from guestbook import views

urlpatterns = [
    path( "", views.guestbook, name="guestbook" ),
]


# views.py
from django.shortcuts import render
from guestbook.models import Guestbook
from django.template import loader
from django.http.response import HttpResponse

def guestbook( request ):
    gblist = Guestbook.objects.order_by( "-idx" )
    gbcount = Guestbook.objects.count()
    context = {
        "gblist" : gblist,
        "gbcount" : gbcount
    }
    template = loader.get_template( "guestbook.html" )
    return HttpResponse( template.render( context, request ) )


# guestbook.html
# <!DOCTYPE html>
# <html>
# 	<head>
# 		<meta charset="UTF-8">
# 		<title> Guestbook </title>
# 	</head>
# 	<body>
# 		<h2> 글목록 </h2>
# 		<br>
# 		{{ gbcount }}개의 글이 있습니다.
# 		<br><br>
# 		<input type="button" value="글쓰기" onclick="location='write'">
# 		{% for gb in gblist %}
# 			<form method="post" action="passwdck">
# 				{% csrf_token %}
# 				<input type="hidden" name="idx" value="{{ gb.idx }}">
# 				<table border="1" style="margin: 5px 0px">
# 					<tr>
# 						<th width="100"> 이름 </th>
# 						<td width="100" align="center"> {{ gb.name }}  </td>
# 						<th width="100"> 작성일 </th>
# 						<td width="100" align="center"> {{ gb.postdate|date:"Y-m-d" }} </td>						
# 					</tr>	
# 					<tr>
# 						<th> 이메일 </th>
# 						<td colspan="3"> {{ gb.email }} </td>
# 					</tr>				
# 					<tr>
# 						<th> 내용 </th>
# 						<td colspan="3"> <pre>{{ gb.content }}</pre> </td>
# 					</tr>
# 					<tr>
# 						<th> 비밀번호 </th>
# 						<td colspan="2"> <input type="password" name="passwd"> </td>
# 						<th>
# 							<input type="submit" value="수정 / 삭제">
# 						</th>						
# 					</tr>
# 				</table>
# 			</form>		
# 		{% endfor %}	
# 	</body>
# </html>
