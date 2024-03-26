from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.views import View, generic
from .models import BlogPost, Author, Comment
from django.conf import settings
from .form import CommentForm
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
  
class HomeView(View):
    def get(self, request):
        return render(request, "blog/home.html")

class BlogList(generic.ListView):
     paginate_by = settings.DEFAULT_PAGINATED_RECORDS
     template_name = "blog/bloglist.html"
     context_object_name = "blogs"
     
     def get_queryset(self):
         return BlogPost.objects.order_by("-created_at")
    
class AuthorProfile(generic.DetailView):
    model = Author
    template_name = "blog/author_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        context['author_posts'] = author.blogs.all().order_by("-created_at")
        return context

class BlogDetail(generic.DetailView,FormMixin):
    model = BlogPost
    template_name = "blog/blog_detail.html"
    context_object_name = "post"
    form_class = CommentForm 
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all().order_by("created_at")
        context['form'] = CommentForm()
        return context
    
    @method_decorator(login_required) 
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST) 
        post = self.get_object() 
         
        if form.is_valid():
            comment = form.cleaned_data['comment']
            comment_instance = Comment.objects.create(blog=post, comment=comment)
            return redirect('.')
            
class BloggerList(generic.ListView):
     model = Author
     paginate_by = settings.DEFAULT_PAGINATED_RECORDS
     template_name = "blog/blogger_list.html"
     context_object_name = "bloggers"