from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Question, Answer, Choice
from django.urls import reverse
from django.views import generic
# Create your views here.

def index(request):
    return render(request, 'exams/index.html')

def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if(user is not None):
        login(request, user)
        return redirect('exams:home')
    else:
        return redirect('exams:home')

def sign_out(request):
    logout(request)
    return redirect('exams:home')

# @login_required(login_url='home')
# def questionaire(request):
#     questions=Question.objects.order_by('-id') [:4]
#     return render(request, 'exams/questionaire.html', {'questions':questions})

class QuestionaireView(LoginRequiredMixin,generic.ListView):
    login_url = 'login:login_do'
    redirect_field_name = "next"
    template_name='exams/questionaire.html'
    context_object_name='questions'
    def get_queryset(self):
        """Return the last three published questions."""
        return Question.objects.order_by('-id')[:3]
