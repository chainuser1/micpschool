__author__ = 'Pareng Jay'
from django.urls import path

from . import views
app_name='exams'
urlpatterns=[

    path('',views.index, name='home'),
    path('<str:slug>/questionaire/',views.questionaire, name='questionaire'),
    path('questionaire/<int:user_id>/answer', views.save_choice, name='answer-question'),
]
