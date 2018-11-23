from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request, 'index')

def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if(user is not None):
        login(request, user)
        return redirect(request,'exams/index.html')
    else:
        return redirect(request,'exams/index.html')

def sign_out(request):
    logout(request)
    return redirect(request,'exams/index.html')
