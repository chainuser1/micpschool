__author__ = 'Pareng Jay'
from django.urls import path

from . import views

urlpatterns=[
    path('',views.index, name='home'),
    path('auth/', views.auth, name='auth'),
    path('log-out/', views.sign_out, name="sign-out"),
    path('questionaire/',views.give_exam, name='questionaire')
]
