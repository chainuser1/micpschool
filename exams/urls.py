__author__ = 'Pareng Jay'
from django.urls import path

from . import views
app_name='exams'
urlpatterns=[
    path('',views.index, name='home'),
    path('<str:category>/questionaire/',views.questionaire, name='questionaire')
]
