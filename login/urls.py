__author__ = 'Pareng Je'

from django.urls import path

from . import views

app_name="login"

urlpatterns = [
    path('', views.index, name="login_do"),
    path('lico-auth/',views.auth, name='lico_auth'),
]
