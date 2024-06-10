# models.py
from django.db import models
class Bookmark(models.Model) :
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)
    def __str__(self):
        return self.title
    
# admin.py
from django.contrib import admin
from bookmark.models import Bookmark
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
admin.site.register(Bookmark, BookmarkAdmin)