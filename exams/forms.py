__author__ = 'Pareng Je'
from django import forms
from  .models import Quiz, Question, Answer
from django.forms import inlineformset_factory
class ChoiceForm(forms.Form):

   def __init__(self, category):
       pass

   def clean(self):
       pass

   def save_choices(self):
       pass
