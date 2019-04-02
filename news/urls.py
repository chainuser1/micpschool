__author__ = 'Pareng Jay'
from django.urls import path
from django.contrib import admin
from . import views

app_name="articles"
urlpatterns = [
	path('',views.index, name='articles'),
	path('<str:slug>/details',views.detail, name='article-details'),
]