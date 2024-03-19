from django.shortcuts import render
from django.views import View, generic
from .models import BlogPost

class HomeView(View):
    def get(self, request):
        return render(request, "blog/home.html")

class BlogList(generic.ListView):
     paginate_by = 5
     template_name = "blog/bloglist.html"
     context_object_name = "blogs"
     
     def get_queryset(self):
         return BlogPost.objects.order_by("-created_at")
