from django.contrib import admin
from .models import  Author, BlogPost, Comments


admin.site.register(Author)
admin.site.register(BlogPost)
admin.site.register(Comments)