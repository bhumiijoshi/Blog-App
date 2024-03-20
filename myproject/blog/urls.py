from django.urls import path
from . import views

urlpatterns = [
     path("", views.HomeView.as_view(), name="home"),
     path("blogs/",views.BlogList.as_view(), name="blog_list"),
     
]