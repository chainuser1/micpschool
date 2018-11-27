__author__ = 'Pareng Jay'
from django.urls import path

from . import views
app_name='exams'
urlpatterns=[
    path('',views.index, name='home'),
    path('questionaire/',views.QuestionaireView.as_view(), name='questionaire')
]
