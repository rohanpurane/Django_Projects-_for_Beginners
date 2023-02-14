from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import *
from .forms import *
from django.core.cache import cache
from .caches import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.

def home(request):
    data = Post.objects.all()
    return render(request, 'home.html',{'data':data})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def user_register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                group = Group.objects.get(name='Author')
                user.groups.add(group)
                messages.success(request, 'Congratulations! You have become an Auther')
                return redirect('/register/')
        else:
            form = RegistrationForm()
        return render(request, 'register.html',{'form':form})
    else:
        return redirect('/dashboard/')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username = uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Succesfully !!')
                    return redirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'login.html',{'form':form})
    else:
        return redirect('/dashboard/')


def dashboard(request):
    if request.user.is_authenticated:
        data = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        ip = request.session.get('ip', 0)
        ct = cache.get('count', version=user.pk)
        context = {
            'data' : data, 
            'full_name' : full_name,
            'groups' : gps,
            'ip' : ip,
            'count' : ct,
        }
        return render(request, 'dashboard.html',context)
    else:
        return redirect('/')

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            Post.objects.create(title=title, desc=desc)
            messages.success(request, 'New Post Added Successfully !!')
            return redirect('/dashboard/')
    else:
        form = PostForm()
    return render(request, 'new_post.html',{'form':form})

@login_required
def update_post(request, pk):
    if request.method == 'POST':
        pi = Post.objects.get(id=pk)
        form = PostForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Updated Successfully !!')
            return redirect('/dashboard/')
    else:
        pi = Post.objects.get(id=pk)
        form = PostForm(instance=pi)
    return render(request, 'update_post.html',{'form':form})

@login_required
def delete_post(request, pk):
    pi = Post.objects.get(id=pk)
    pi.delete()
    messages.success(request, 'Post Deleted Successfully !!')
    return redirect('/dashboard/')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Thanks For Your Valuable Time')
        return HttpResponseRedirect('/')
    else:
        return redirect('/')