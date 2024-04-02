from django.contrib import admin
from .models import  Author, BlogPost, Comment

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 3

class BlogPostAdmin(admin.ModelAdmin):

    inlines = [CommentInline]

admin.site.register(Author)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment)
