from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import ICategory, Quiz, Question, Answer, QuestionResponse
from django.views import generic
# Create your views here.

def get_categories():
    return ICategory.objects.all()

def index(request):
    categories = get_categories()
    return render(request, 'exams/index.html',{'categories':categories})


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
def questionaire(request, slug):
    categories = get_categories()
    questions = get_object_or_404(ICategory, slug=slug).questions.order_by('id')[:3]
    user = User.objects.get(id=request.user.id)
    type=get_object_or_404(ICategory, slug=slug).name
    context= {'categories':categories, 'questions':questions, 'type':type}
    return render(request, 'exams/questionaire.html', context)


@login_required(redirect_field_name='next', login_url = 'login:login_do')
def save_choices(request):
    if(request.POST):
        pass



