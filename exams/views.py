from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, Choice
# Create your views here.

def index(request):
    return render(request, 'exams/index.html')

def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if(user is not None):
        login(request, user)
        return redirect('home')
    else:
        return redirect('home')

def sign_out(request):
    logout(request)
    return redirect('home')

@login_required(login_url='home')
def give_exam(request):
    questions=Question.objects.order_by('-id') [:4]
    return render(request, 'exams/questionaire.html', {'questions':questions})
