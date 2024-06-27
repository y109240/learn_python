## 추천?

# suggest/models.py
from django.db import models
class Suggest( models.Model ):      # suggest_suggest
    id = models.CharField( primary_key=True, verbose_name="아이디", max_length=50)
    num1 = models.CharField( null=False, verbose_name="추천1", max_length=100 )
    num2 = models.CharField( null=False, verbose_name="추천2", max_length=100 )
    num3 = models.CharField( null=False, verbose_name="추천3", max_length=100 )
    num4 = models.CharField( null=False, verbose_name="추천4", max_length=100 )
    num5 = models.CharField( null=False, verbose_name="추천5", max_length=100 )
    suggesttime = models.DateTimeField( auto_now_add=True, null=False, blank=True, verbose_name="추천일" )


# suggest/admin.py
from django.contrib import admin
from suggest.models import Suggest
class SuggestAdmin( admin.ModelAdmin ):
    list_display = ( "id", "num1", "num2", "num3", "num4", "num5" )
admin.site.register( Suggest, SuggestAdmin )


# urls.py
from django.urls.conf import path
from suggest import views
urlpatterns = [
    path( "", views.SuggestView.as_view(), name="suggest"),
    # localhost:8000/suggest/
]


# views.py
from django.shortcuts import render
from django.views.generic.base import View
import logging
from django.template import loader
from django.http.response import HttpResponse
logger = logging.getLogger(__name__)
class SuggestView( View ):
    def get( self, request ):
        id = request.session["memid"]
        context = {
            "memid" : id, 
            }
        template = loader.get_template( "suggest/suggest.html" )
        return HttpResponse( template.render( context, request ) )
    def post( self, request ):
        pass