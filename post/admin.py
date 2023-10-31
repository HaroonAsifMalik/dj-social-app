from django.contrib import admin
from .models import Post , ResponseAgainstPost
# Register your models here.

@admin.register(Post)
class PostAdmin ( admin.ModelAdmin):
    list_display = [ 'id', 'author' , 'image' , 'date' ]

@admin.register(ResponseAgainstPost)
class ResponseAgainstPostAdmin(admin.ModelAdmin):
    list_display =['id' ,'user', 'share' , 'like' , 'comment']


