from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
# Create your views here.

def index(request):
    #instantiate
    form=LoginForm(request.POST or None)
    response = render(request, 'login/index.html', {'form':form})
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
    else: 
        response = render(request, 'login/index.html', {'form':LoginForm(request.POST)})
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
