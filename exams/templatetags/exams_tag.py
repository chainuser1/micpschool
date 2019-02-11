from django import template
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Group
from exams.models import ICategory, Answer
# use to register functions as template tags
register =  template.Library()


@register.filter(name='is_answer')
def is_answer(user, answer_id):
	answer=get_object_or_404(Answer,id=answer_id)
	return user.responses.filter(answer=answer).exists()

@register.filter(name='has_group')
def has_group(user, group_name):
	# return True if group in user.groups.all() else False
	return user.groups.filter(name=group_name).exists()


# used to get the categories without hassle
@register.simple_tag
def get_category():
	return ICategory.objects.all()
	
