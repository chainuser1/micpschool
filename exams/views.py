from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Quiz, Question, Answer, Choice
from django.views import generic
from .forms import ChoiceForm
# Create your views here.

def index(request):
    quizzes=Quiz.objects.all().distinct()
    return render(request, 'exams/index.html',{'quizzes':quizzes})


# class QuestionaireView(LoginRequiredMixin,generic.DetailView):
#     model = Question
#     login_url = 'login:login_do'
#     redirect_field_name = "next"
#     template_name='exams/questionaire.html'
#     context_object_name='questions'
#     slug_field="category"
#     def get_queryset(self):
#         return get_object_or_404(Question,quiz_id=self.kwargs.get("category"))
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         """Return a list of quizzes title"""
#         context['quizzes'] = quizzes=Quiz.objects.all()
#         return context

@login_required(redirect_field_name='next', login_url = 'login:login_do')
def questionaire(request, category):
    quizzes=Quiz.objects.order_by('-quiz_text')
    questions = get_object_or_404(Quiz, quiz_text=category).question_set.order_by('id')[:3]
    return render(request, 'exams/questionaire.html', {'quizzes':quizzes, 'questions':questions})


@login_required(redirect_field_name='next', login_url = 'login:login_do')
def save_choices(request):
    pass

