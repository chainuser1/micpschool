from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import ICategory, Question, Answer, QuestionResponse
from django.http import JsonResponse
# from django.views import generic
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
    questions = get_object_or_404(ICategory, slug=slug).questions.order_by('id')[:10]
    type=get_object_or_404(ICategory, slug=slug).name
    context= {'categories':categories, 'questions':questions, 'type':type}
    return render(request, 'exams/questionaire.html', context)


@login_required(redirect_field_name='next', login_url = 'login:login_do')
def save_choice(request, user_id):
	response=None
	if(request.method=='GET'):
		user=get_object_or_404(User,pk=user_id)
		question=get_object_or_404(Question,pk=request.GET['question_id'])
		answer=get_object_or_404(Answer,pk=request.GET['answer_id'])
		try:
			q_response_obj=QuestionResponse.objects.get(user=user, question=question)
			q_response_obj.answer=answer
			q_response_obj.save(update_fields=['answer'])
		except QuestionResponse.DoesNotExist:
			q_response_obj=QuestionResponse(user=user,question=question, answer=answer)
			q_response_obj.save()
		response = JsonResponse({'message':'Your answer was saved!'})
	else:
		response = JsonResponse({'message':'An internal error occurred!'+request.method})
	return response