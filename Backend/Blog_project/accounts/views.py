from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout, get_user_model # user model is already exists
from django.contrib import messages
from django.contrib.auth.models import User

# User = get_user_model  #get the user model

# Create your views here.
def Do_Login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        uname = form.cleaned_data.get('username')
        pwd = form.cleaned_data.get('password')
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect ('/')
        else:
            messages.error(request, 'Wrong Credentials')
    ctx = {'form': form, 'title': 'Login | Blogist'}
    return render(request, "accounts/login.html", ctx)

def RegisterUserForm(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        
        if password1 == password2:
            user = User.objects.create_user(username, email, password1)
            user.save()
            messages.success(request, 'Registration Success')
            return redirect('/')
        else:
            messages.error(request, 'Password not match!!')
    ctx = {'form':form, 'title':'Blogist | Register'}
    return render(request, 'accounts/register.html',ctx)