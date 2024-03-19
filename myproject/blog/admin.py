from django.contrib import admin
from .models import  Authors, BlogPost, Comment

admin.site.register(Authors)
admin.site.register(BlogPost)
admin.site.register(Comment)