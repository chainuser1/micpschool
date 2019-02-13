from django import template
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Group
from exams.models import ICategory, Answer
# use to register functions as template tags
register =  template.Library()


@register.filter(name='is_answer')
def is_answer(user, answer_id):
	answer=get_object_or_404(Answer,id=answer_id)
	# returns true if the answer id matches the constraint in the user response
	return user.responses.filter(answer=answer).exists()

@register.filter(name='has_group')
def has_group(user, group_name):
	# return True if group in user.groups.all() else False
	return user.groups.filter(name=group_name).exists()


# used to get the categories without hassle
@register.simple_tag
def get_category():
	return ICategory.objects.all()

#filter to determine if student already took the quiz
@register.filter(name='has_quiz')
def has_quiz(user, name):
	category = get_object_or_404(ICategory, name=name)
	return user.quizzes.filter(category=category).exists()

#returns a formatted output of final score/ num of questions
@register.filter(name='get_score')
def get_score(user, name):
	category = get_object_or_404(ICategory, name=name)
	quiz = user.quizzes.get(category=category)
	return "%d/%d" %(quiz.final_score, quiz.num_questions)

@register.filter(name='reveal_answer')
def reveal_answer(id):
	answer=Answer.objects.get(pk=id)
	if answer.correct:
		return 'text-success'
	else:
		return 'text-danger'