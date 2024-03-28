from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse,reverse_lazy
from django.views import View, generic
from .models import BlogPost, Author, Comment
from django.conf import settings
from .form import CommentForm
from django.views.generic.edit import FormMixin, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
        context['author_posts'] = BlogPost.objects.select_related().filter(author = author)
        return context

class BlogDetail(generic.DetailView,FormMixin):
    model = BlogPost
    template_name = "blog/blog_detail.html"
    context_object_name = "post"
    form_class = CommentForm 
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = Comment.objects.select_related().filter(blog = post)
        context['form'] = CommentForm()
        return context


    def post(self, request, *args, **kwargs):
        
        if not request.user.is_authenticated: 
            return redirect(f'{reverse("users:login")}?next={request.path}')
        form = self.form_class(request.POST) 
        post = self.get_object()
        user = request.user
         
        if form.is_valid():
            comment = form.cleaned_data['comment']
            comment_instance = Comment.objects.create(user=user,blog=post, comment=comment)
            return redirect('.')
            
class BloggerList(generic.ListView):
     model = Author
     paginate_by = settings.DEFAULT_PAGINATED_RECORDS
     template_name = "blog/blogger_list.html"
     context_object_name = "bloggers"
     
     def get_queryset(self):
         return Author.objects.only('name','created_at')
     
class CreateAuthor(LoginRequiredMixin,CreateView):
    
    model = Author
    template_name = "blog/create_author.html"
    fields = ['name','biological_info']
       
    def form_valid(self, form):
        form = form.save(commit=False)
        user = self.request.user
        form.user = user
        form.save()
        return redirect('blog:blog_list')