from django.contrib import admin
from .models import Slider,Team,Youtuber
from django.utils.html import format_html
# Register your models here.
admin.site.register(Slider)



class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src= "{}" width="40px" style="border-redius:150px" />'.format(object.photo.url))

    list_display = ('id','first_name','role','created_date','thumbnail')

    list_display_links = ["first_name"]
    #for search
    search_fields = ('first_name','role')
    list_filter = ('role','last_name')


class YtAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src= "{}" width="40px" style="border-redius:150px" />'.format(object.photo.url))

    list_display = ('id','name','thumbnail','created_date','city','subs_count','is_featured')

    list_display_links = ["name","thumbnail"]
    #for search
    search_fields = ('name','role')
    list_filter = ('subs_count','camera_type','name')
    list_editable = ('is_featured',)

admin.site.register(Youtuber,YtAdmin)
