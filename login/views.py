from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    response = render(request, 'login/index.html')
    try:
        if("next" in request.GET):
            request.session['next']=request.GET["next"]
    except KeyError:
        response =  HttpResponse('Unable to redirect your page')
    return response

def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    response=redirect('exams:home')
    user = authenticate(username=username, password=password)
    if(user is not None):
        login(request, user)
        try:
            if("next" in request.session):
                response =  redirect(request.session["next"])
        except KeyError:
            response = redirect("exams:home")
    else:
        response = redirect("login:login_do")
    return response

def sign_out(request):
    logout(request)
    return redirect("exams:home")
