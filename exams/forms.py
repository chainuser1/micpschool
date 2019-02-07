
from django import forms
from django.forms.models import BaseInlineFormset
from django.shortcuts import get_object_or_404
from django.forms import ModelForm, formset_factory
from .models import QuestionResponse, Answer, Question, ICategory

class BaseAnswersFormset(BaseInlineFormset):
	def add_fields(self, form, index):
		super(self).add_fields(form, index)
		# save the formset in nested property
		form.nested = QuestionResponseFormset(
			instance = instance.form,
			data=form.data if form.is_bound else None,
			files=form.files if form.is_bound else None,
			prefix='question_response-%s-%s' %(form.prefix, QuestionReponseForm.prefix()),
			extra=1
			)

AnswersFormset = inlinefomset_factory(Question,QuestionResponse, BaseAnswersFormset, extra=1)


class QuestionResponseForm(ModelForm):

	class Meta:
		model=QuestionResponse
		fields = ['question','answer']
		exclude = ['user']


