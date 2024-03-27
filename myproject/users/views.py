from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .form import LoginForm, SignupForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View, generic
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class LogIn(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url  
        else:
            return reverse_lazy('blog:blog_list')  
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    
class LogOut(View):
    def get(self, request):
        logout(request)
        messages.success(request,f'You have been logged out.')
        return redirect('users:login')        
    
class SignUp(FormView):
    redirect_authenticated_user = True
    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy('users:login')
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('blog:blog_list')  
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        
        return super(SignUp, self).form_valid(form)