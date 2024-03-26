from django.urls import path
from . import views

app_name = "users"

urlpatterns = [

    path('login/', views.LogIn.as_view(), name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    
]