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
    path("", views.guestbook, name="guestbook"),
    # localhost:8000/guestbook
    path("write", views.write, name="write"),
    # localhost:8000/guestbook/write
    path("writepro", views.writepro, name="writepro"),
    # localhost:8000/guestbook/writepro
    path("passwdck", views.passwdck, name="passwdck"),
    # localhost:8000/guestbook/passwdck
    path("delete", views.delete, name="delete"),
    # localhost:8000/guestbook/delete
    path("update", views.update, name="update"),
    # localhost:8000/guestbook/update
]


# views.py
from django.shortcuts import render, redirect
from guestbook.models import Guestbook
from django.template import loader
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.utils.decorators import method_decorator

# def guestbook(request):
#     gblist = Guestbook.objects.order_by("-idx")
#     gbcount = Guestbook.objects.count()
#     context = {
#         "gblist" : gblist,
#         "gbcount" : gbcount
#         }
#     template = loader.get_template("guestbook.html")
#     return HttpResponse(template.render(context, request))
class ListView(View):
    def get(self, request):
        gblist = Guestbook.objects.order_by("-idx")
        gbcount = Guestbook.objects.count()
        context = {
            "gblist" : gblist,
            "gbcount" : gbcount
            }
        template = loader.get_template("guestbook.html")
        return HttpResponse(template.render(context, request))

# def write(request):
#     template = loader.get_template("write.html")
#     return HttpResponse(template.render({}, request))
# @csrf_exempt
# def writepro(request):
#     dto = Guestbook(
#         name = request.POST["name"],
#         email = request.POST["email"],
#         passwd = request.POST["passwd"],
#         content = request.POST["content"]
#         )
#     dto.save()
#     return redirect("guestbook")    
class WriteView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return super(WriteView, self).dispatch(request, *args, **kwargs)
    def get(self, request):
        template = loader.get_template("write.html")
        return HttpResponse(template.render({}, request))
    def post(self, request):
        dto = Guestbook(
            name = request.POST["name"],
            email = request.POST["email"],
            passwd = request.POST["passwd"],
            content = request.POST["content"]
        )
        dto.save()
        return redirect("/guestbook")

# @csrf_exempt
# def passwdck(request):
#     idx = request.POST["idx"]
#     passwd = request.POST["passwd"]
#     dto = Guestbook.objects.get(idx=idx)
#     if passwd == dto.passwd : 
#         template = loader.get_template("edit.html")
#         context = {
#             "dto" : dto
#             }
#         return HttpResponse(template.render(context, request))
#     else:
#         return redirect("guestbook")    
class PasswdView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return super(PasswdView, self).dispatch(request, *args, **kwargs)
    def post(self, request):
        idx = request.POST["idx"]
        passwd = request.POST["passwd"]
        dto = Guestbook.objects.get(idx=idx)
        if passwd == dto.passwd:
            template = loader.get_template("edit.html")
            context = {
                "dto" : dto
                }
            return HttpResponse(template.render(context, request))
        else:
            return redirect("/guestbook")
 
# def delete(request):
#     idx = request.GET["idx"]
#     dto = Guestbook.objects.get(idx=idx)
#     dto.delete()
#     return redirect("guestbook")
# @csrf_exempt
# def update(request):
#     idx = request.POST["idx"]
#     dto = Guestbook.objects.get(idx=idx)
#     newdto = Guestbook(
#         idx = dto.idx,
#         name = dto.name,
#         email = request.POST["email"],
#         passwd = request.POST["passwd"],
#         content = request.POST["content"],
#         postdate = dto.postdate
#         )
#     newdto.save()
#     return redirect("guestbook")
class UpdateView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateView, self).dispatch(request, *args, **kwargs)
    def get(self, request):
        idx = request.GET["idx"]
        dto = Guestbook.objects.get(idx=idx)
        dto.delete()
        return redirect("/guestbook")
    def post(self, request):
        idx = request.POST["idx"]
        dto = Guestbook.objects.get(idx=idx)
        newdto = Guestbook(
            idx = dto.idx,
            name = dto.name,
            email = request.POST["email"],
            passwd = request.POST["passwd"],
            content = request.POST["content"],
            postdate = dto.postdate
        )
        newdto.save()
        return redirect("/guestbook")


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
