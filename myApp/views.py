from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from .models import Blogger, Blog
from .forms import UserRegisterationForm
from django.views.generic import ListView
import datetime
from django.conf import settings
from django.contrib.auth import authenticate, login as dj_login, logout


# Create your views here.




# This is for Login functionality
def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            messages.success(request, 'Successfully Logged In!')
            return redirect('login')
        else:
            messages.warning(request, "Invalid Credentials")
            return redirect('login')
    return render(request, 'login.html')

# This is for logout 
def Logout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out!")
    return redirect('login')


# This is for Registering User
class RegisterView(View):
    def get(self, request):
        form = UserRegisterationForm()
        if request.user.is_authenticated:
            pass
        return render(request, 'register.html', locals())

    def post(self, request):
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Registered Successfully!")
        else:
            messages.warning(request, "Invalid Credentials")
        return render(request, 'register.html', locals())

# This is for the Adding Blogs
def profile(request):
    msg = ''
    if request.method =='POST':
        blogger=request.POST.get('blogger')
        title=request.POST.get('title')
        content=request.POST.get('content')
        date = request.POST.get('date')
        time=request.POST.get('time')
        blog = Blog(blogger=blogger, title=title, content=content, date=date, time=time)
        blog.save()
        messages.success(request, "Check home Page to see your Blog!")
    return render(request, 'blog.html',{})

# This is to display the Blogs on the home page
def home(request):
    blog = Blog.objects.all()
    data={'blog':blog}
    return render(request, 'home.html', data)