from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    try:
        if("next" in request.GET):
            request.session['next']=request.GET["next"]
    except KeyError:
        return HttpResponse('Unable to redirect your page')
    finally:
        return render(request, 'login/index.html')

def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if(user is not None):
        login(request, user)
        try:
        if("next" in request.session):
            return redirect(request.session["next"])
        except KeyError:
            return redirect("exams:home")
    else:
        return redirect("login:login_do")
