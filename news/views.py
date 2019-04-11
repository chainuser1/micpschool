from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Article, Media, Comment
from django.core.paginator import Paginator


def index(request):
	articles_list = Article.objects.all()
	paginator = Paginator(articles_list, 6)#6 articles per page
	page = request.GET.get('page')
	articles = paginator.get_page(page)
	return render(request, 'articles/index.html', {'page_obj':articles})

def detail(request):
	pass