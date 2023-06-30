from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Blogger, Blog


# Register your models here.

@admin.register(Blogger)
class BloggerRegisteration(admin.ModelAdmin):
    list_display = ['id', 'user', 'password1']

@admin.register(Blog)
class BlogPost(admin.ModelAdmin):
    list_display=['id','blogger','title','content']

admin.site.unregister(Group)