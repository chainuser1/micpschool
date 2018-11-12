__author__ = 'Pareng Je'
from django.urls import path

from . import views

urlpatterns=[
    path('',views.index, name='index')
]