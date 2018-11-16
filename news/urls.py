from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:news_id>/', views.details,name="details" ),
    path('<int:news_id>/', views.comment_add, name="add")
]
