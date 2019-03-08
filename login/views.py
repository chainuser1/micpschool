from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache
from .forms import LoginForm, RegisterForm
# Create your views here.

@never_cache
def index(request):
    #instantiate
    if request.user.is_authenticated:
        return redirect(reverse("exams:home"))

    form=LoginForm(request.POST or None)
    response = render(request, 'login/login.html', {'form':form})
    #get the redirection page
    try:
        if("next" in request.GET):
            request.session['next']=request.GET["next"]
    except KeyError as e:
        print(e)
    #login and validation here


    if (request.POST and form.is_valid()):
        user=form.login(request)
        if(user):
            login(request, user)
            try:
                if("next" in request.session):
                    response =  redirect(request.session["next"])
            except KeyError:
                response = redirect("exams:home")
    return response

@never_cache
def auth(request):
    # redirect if user is authenticated
    if request.user.is_authenticated:
        return redirect(reverse("exams:home"))

    username = request.POST['username']
    password = request.POST['password']
    response = redirect('exams:home')
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

@never_cache
def register(request):
    if request.user.is_authenticated:
        return redirect(reverse("exams:home"))
    form = RegisterForm(request.POST or None)
    response =  None
    if(request.POST and form.is_valid()):
        form.save()
        username = request.POST["username"]
        password = request.POST["password1"]
        user = authenticate(username=username, password=password)
        login(request, user)
        if("next" in request.session):
            response=redirect(request.session["next"])
        else:
            response=redirect('master')
    else: 
        response = render(request, 'login/register.html', {'form':form})
    return response
    