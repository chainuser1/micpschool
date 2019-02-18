from django.urls import path
from django.contrib import admin
from . import views
app_name='about'

urlpatterns = [
   path('',views.view_page, name='view_page'),
]