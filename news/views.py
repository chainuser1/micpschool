from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News
from django_ajax.decorators import ajax
from django.core import serializers
# Create your views here.
def index(request):
    latest_news_list=News.objects.order_by('-pub_date') [:5]
    context={
        'latest_news_list':latest_news_list
    }
    return render(request, 'news/index.html', context)


def details(request, news_id):
    news=get_object_or_404(News,pk=news_id)
    # return {'news': news}
    return render(request, 'news/details.html',{'news':news})
