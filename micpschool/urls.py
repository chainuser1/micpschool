"""micpschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

admin.site.site_header = 'MICP Academy Admin'
admin.site.site_title = 'MICP Academy Admin'
admin.site.site_url = 'http://chainuser1.pythonanywhere.com/'
admin.site.index_title = 'MICP Academy Admin'
admin.empty_value_display = '**Empty**'


urlpatterns = [

    path('admin/site', admin.site.urls, name='admin'),
    path('', views.master, name='master'),
    path('exams/', include('exams.urls')),
    path('news/', include('news.urls')),
    path('login/', include('login.urls'))
]
