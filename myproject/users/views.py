from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .form import LoginForm, SignupForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View, generic

class LogIn(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
   
    def post(self, request, *args, **kwargs):
        next_url = request.POST.get('next')
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('blog:blog_list')
        
        messages.error(request,f'Invalid username or password')
        return render(request,'users/login.html',{'form': form})
    
class LogOut(View):
    def get(self, request):
        logout(request)
        messages.success(request,f'You have been logged out.')
        return redirect('users:login')        
    
class SignUp(FormView):
    template_name = "users/signup.html"
    form_class = SignupForm
    
    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            return redirect('users:login')
        else:
            return render(request, 'users/signup.html', {'form': form})