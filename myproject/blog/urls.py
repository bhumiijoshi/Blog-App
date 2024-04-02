from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("blogs/", views.BlogList.as_view(), name="blog_list"),
    path("blogger/<int:pk>/", views.BloggerDetail.as_view(), name="blogger"),
    path("blogs/<int:pk>/", views.BlogDetail.as_view(), name="blogdetail"),
    path("bloggers/", views.BloggerList.as_view(), name="bloggerlist"),
    path("createblogger/", views.CreateBlogger.as_view(), name="create_blogger"),
    path("bloggerprofile/", views.BloggerProfile.as_view(), name="blogger_profile"),
    path("createpost/", views.CreatePost.as_view(), name="create_post"),
    path("updatepost/<int:pk>/", views.UpdatePost.as_view(), name="update_post"),
    path("deletepost/<int:pk>/", views.DeletePost.as_view(), name="delete_post"),
]
