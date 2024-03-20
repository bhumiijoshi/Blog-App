from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.views import View, generic
from .models import BlogPost, Author
from django.conf import settings

 
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

class BlogDetail(generic.DetailView):
    model = BlogPost
    template_name = "blog/blog_detail.html"
    context_object_name = "post"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all().order_by("created_at")
        return context