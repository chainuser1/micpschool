from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import ICategory, Question, Answer, QuestionResponse
from django.http import JsonResponse
# from django.views import generic
# Create your views here.


def index(request):
    return render(request, 'exams/index.html')


@login_required(redirect_field_name='next', login_url = 'login:login_do')
def questionaire(request, slug):
    questions = get_object_or_404(ICategory, slug=slug).questions.order_by('id')[:10]
    type=get_object_or_404(ICategory, slug=slug).name
    context= {'questions':questions, 'type':type}
    return render(request, 'exams/questionaire.html', context)


@login_required(redirect_field_name='next', login_url = 'login:login_do')
def save_choice(request, user_id):
	response=None
	if(request.method=='GET'):#check if request method corresponds.
		"""Find the respective objects designated in foreign keys"""
		user=get_object_or_404(User,pk=user_id)
		question=get_object_or_404(Question,pk=request.GET['question_id'])
		answer=get_object_or_404(Answer,pk=request.GET['answer_id'])
		#update student response if exists and create new if not
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
	return response #return a json response object


@login_required(redirect_field_name='next', login_url='login:login_do')
def reset_quiz(request, name):
	user=get_object_or_404(User,pk=request.user.id)
	questions=get_object_or_404(ICategory, name=name).questions.order_by('id')
	for question in questions:
		# delete any instance of user choice
		QuestionResponse.objects.filter(user=user,question=question).delete()
	#return back
	return redirect(request.GET['next'])

@login_required(redirect_field_name='next', login_url='login:login_do')
def save_quiz(request, name):
	student=get_object_or_404(User, id=request.user.id)
	category=get_object_or_404(ICategory, name=name)

	num_of_questions=category.questions.objects.count() #count objects
	final_score=0
	for question in category.questions.all():
		for answer in question.answers.all():
			answer=answer.responses.filter(question=question)
			correct_answer=answer.objects.filter(correct=1)
			if correct_answer.id==answer.id:
				final_score+=1
	user.quizzes_set.create(category=category, final_score=final_score)
	return JsonResponse({'message':'Score is %d' %(final_score)})
			
