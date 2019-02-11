__author__ = 'Pareng Jay'
from django.urls import path
from django.contrib import admin
from . import views
app_name='exams'
urlpatterns=[
	path('admin/site', admin.site.urls),
    path('',views.index, name='home'),
    path('<str:slug>/questionaire/',views.questionaire, name='questionaire'),
    path('questionaire/<int:user_id>/answer', views.save_choice, name='answer-question'),
    path('quiz/<str:name>/reset', views.reset_quiz, name='reset_quiz'),
    path('quiz/<str:name>/save', views.reset_quiz, name='save_quiz'),
]
