__author__ = 'Pareng Je'

from django.urls import path

from . import views

app_name="login"

urlpatterns = [
    path('', views.index, name="login_do"),
    path('lico-auth/',views.auth, name='lico_auth'),
    path('lico-logout/', views.sign_out, name='lico_logout'),
    path('auth-register', views.register, name='lico_register'),
    path('auth-create-lico', views.store, name='lico_store'),
]
