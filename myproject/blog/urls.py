from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
     path("", views.HomeView.as_view(), name="home"),
     path("blogs/",views.BlogList.as_view(), name="blog_list"),
     path("blogger/<int:pk>/",views.AuthorProfile.as_view(), name="author"),
     path("blogs/<int:pk>/",views.BlogDetail.as_view(), name="blogdetail"),
     path("bloggers/",views.BloggerList.as_view(), name="bloggerlist"), 
     path("createauthor/",views.CreateAuthor.as_view(), name="create_author"), 
     
]