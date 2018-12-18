from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ICategory, Quiz, Question, Answer, QuestionResponse
from django.views import generic
# Create your views here.

def get_categories():
    return ICategory.objects.all().distinct()

def index(request):
    return render(request, 'exams/index.html',{'categories':get_categories()})


# class QuestionaireView(LoginRequiredMixin,generic.DetailView):
#     model = Question
#     login_url = 'login:login_do'
#     redirect_field_name = "next"
#     template_name='exams/questionaire.html'
#     context_object_name='questions'
#     slug_field="ICategories"
#     def get_queryset(self):
#         return get_object_or_404(Question,quiz_id=self.kwargs.get("ICategories"))
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         """Return a list of quizzes title"""
#         context['quizzes'] = quizzes=Quiz.objects.all()
#         return context

@login_required(redirect_field_name='next', login_url = 'login:login_do')
def questionaire(request, ICategories):
    questions = get_object_or_404(Quiz, quiz_text=ICategories).question_set.order_by('id')[:3]
    return render(request, 'exams/questionaire.html', {'categories':get_categories(), 'questions':questions})


@login_required(redirect_field_name='next', login_url = 'login:login_do')
def save_choices(request):
    if(request.POST):
        pass



