## Boookmark ##


# models.py : 테이블 생성
from django.db import models
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField("url", unique=True)
    def __str__(self):
        return self.title

# dos (cmd)
# python manage.py makemigrations
# python manage.py migrate

# admin.py : 관리자 페이지 설정
from django.contrib import admin
from bookmark.models import Bookmark
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("title", "url")
admin.site.register(Bookmark, BookmarkAdmin)


# urls.py
from django.urls.conf import path, re_path
from bookmark import views

urlpatterns = [
    path("", views.home, name="home"),  # index(=시작) 페이지
    # http://localhost:8000/bookmark
    re_path(r"^detail$", views.detail, name="detail"),
    # http://localhost:8000/bookmark/detail
]


# views.py
from django.shortcuts import render
from bookmark.models import Bookmark
from django.template import loader
from django.http.response import HttpResponse

# http://localhost:8000/bookmark
def home(request):
    urllist = Bookmark.objects.order_by("title")
    # select * from bookmark_bookmark order by title;
    urlcount = Bookmark.objects.all().count()
    # select count(*) from bookmark_bookmark;
    template = loader.get_template("home.html")
    context = {
            "urllist" : urllist,
            "urlcount" : urlcount,
        }
    return HttpResponse(template.render(context, request))

# http://localhost:8000/bookmark/detail
def detail(request):
    url = request.GET["url"]
    dto = Bookmark.objects.get(url=url)
    template = loader.get_template("detail.html")
    return HttpResponse(template.render({"dto":dto}, request))


## templates (Package) : 보여주는 페이지

# detail.html
# <!DOCTYPE html>
# <html>
# 	<head>
# 		<meta charset="UTF-8">
# 		<title> Bookmark </title>
# 	</head>
# 	<body>
# 		<h2> {{ dto.title }}  </h2>
# 		<br><br>
# 		URL : <a href="{{ dto.url }}"> {{ dto.title }} </a>
# 	</body>
# </html>

# home.html
# {% load static %}
# <!DOCTYPE html>
# <html>
# 	<head>
# 		<meta charset="UTF-8">
# 		<title> Bookmark </title>
# 		<link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
# 	</head>
# 	<body background="{% static 'images/a.jpg' %}">
# 		<h2> 북마크 </h2>
# 		<br><br>
# 		{{ urlcount }}개의 북마크가 있습니다. <br>
# 		<br>
# 		<ul>
# 			{% for row in urllist %}	
# 				<li> <a href="detail?url={{ row.url }}"> {{ row.title }} </a> </li> <br>
# 			{% endfor %}
# 		</ul>	
# 	</body>
# </html>
