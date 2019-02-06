
from django import forms
from django.forms import ModelForm, formset_factory
from .models import QuestionResponse, Answer, Question
class QuestionResponseForm(ModelForm):

	answer=forms.CharField(required=True,max_length=10,widget=forms.TextInput(attrs={'class':'answer',
		'disabled':'disabled', 'value':''}))
	def __init__(self,*args, **kwargs):
		super(QuestionResponseForm, self).__init__(*args, **kwargs)
		# request = kwargs.pop('request', None)
	
	class Meta:
		model=QuestionResponse
		fields = ['answer']
		
    

