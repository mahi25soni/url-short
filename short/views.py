from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login , logout , authenticate
from .forms import *
import json
from .utils import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def LogIn(request):
    if request.method == 'POST':
        loginform = LoginForm(data = request.POST)
        if loginform.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            reg = authenticate(request , username = username, password=password)
            if reg is not None:
                login(request, reg)
                return HttpResponseRedirect('/') 
    else:
        loginform = LoginForm()
    return render(request, 'short/login.html', {'form':loginform})

def SignUp(request):
    if request.method == 'POST':
        userform = MyUser(data = request.POST)
        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect('/login/')

    else:
        userform = MyUser()
    return render(request, 'short/signup.html', {'form':userform})

def LogOut(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def home(request):
    reqobject = request.build_absolute_uri()

    user = request.user
    if request.method == 'POST':
        form = URLForm(data = request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            websitename = getsitename(url)
            anurl, created = ALLurl.objects.get_or_create(user = user, websitename = websitename, url = url)
            shorted = getshorterlink(reqobject)
            anurl.shorted = shorted
            anurl.save()
            messages.success(request , shorted)
            return HttpResponseRedirect('/')
    else:
        form = URLForm()
    return render(request , 'short/home.html' , {'form':form})

@login_required(login_url='/login/')
def showurls(request):
    anurl = ALLurl.objects.filter(user = request.user)
    return render(request , 'short/showurls.html' , {'data':anurl})

def removeurl(request, pk):
    anurl = ALLurl.objects.get(id=pk)
    anurl.delete()
    return HttpResponseRedirect('/showurls/')

def redirecting(request, para):
    print()
    anurl = ALLurl.objects.get(shorted = request.build_absolute_uri())
    url = anurl.url
    return HttpResponseRedirect(url)




