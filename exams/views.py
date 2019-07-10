from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import ICategory, Question, Answer, QuestionResponse, Quiz, CarouselIndex
from django.http import JsonResponse
# from django.views import generic
# Create your views here.

# shows the exams home page
def index(request):
	context = {'images': CarouselIndex.objects.all()}
	return render(request, 'exams/index.html', context)

# pulls out questions for the chosen category
@login_required(redirect_field_name='next', login_url = 'login:login_do')
def questionaire(request, slug):
	category = get_object_or_404(ICategory, slug=slug)
	user = get_object_or_404(User, pk=request.user.id)
	questions = category.questions.order_by('id')[:10]
	type=get_object_or_404(ICategory, slug=slug).name
	context= {'questions':questions, 'type':type}
	if Quiz.objects.filter(category=category, student=user).exists():
		response = render(request, 'exams/questionaire.html', context)
	else:
		response = render(request, 'exams/question_display.html', context)
	return response


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
	num_of_questions=category.questions.count() #return number of questions from this category
	final_score=0
	context=None
	compl_x=0
	for question in category.questions.all():
		for answer in question.answers.all():
			for response in student.responses.filter(question=question, answer=answer):
				compl_x+=1#count user response from each question
				if answer.correct:#if answer is correct then score increments
					final_score+=1
	if compl_x<num_of_questions:#returns a 204 status for incomplete answer sheet
		return JsonResponse({'message':'Please answer all questions!'},status=204)
	else:
		try:#update or save new quiz instance
			quiz=student.quizzes.get(category=category)
			quiz.num_questions=num_of_questions
			quiz.final_score=final_score
			quiz.save(update_fields=['num_questions','final_score'])
		except Quiz.DoesNotExist:
			quiz=student.quizzes.create(category=category, num_questions=num_of_questions, final_score=final_score)
			quiz.save()
		return JsonResponse({'message':'Score is %d'%(final_score) ,status=200})
			
