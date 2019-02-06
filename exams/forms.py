
from django import forms
from django.forms import ModelForm, formset_factory
from .models import QuestionResponse, Answer, Question
class QuestionResponseForm(ModelForm):

	answer=forms.ModelChoiceField(queryset=None,widget=forms.RadioSelect(attrs={'class':'radio'}))
	def __init__(self,*args, **kwargs):
		super(QuestionResponseForm, self).__init__(*args, **kwargs)
		request = kwargs.pop('request', None)
		self.fields['answer'].queryset = Answer.objects.all()
		
	class Meta:
		model=QuestionResponse
		exclude = ()
		
    

