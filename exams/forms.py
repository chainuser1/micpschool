
from django.forms import ModelForm, formset_factory
from .models import QuestionResponse
class QuestionResponseForm(ModelForm):
	class Meta:
		model=QuestionResponse
		


