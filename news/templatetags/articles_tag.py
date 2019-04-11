from django import template
from django.shortcuts import render, get_object_or_404
import string
from news.models import Article, Media
register =  template.Library()

@register.filter(name='capitalize')
def title_cap(title):
	return string.capwords(title)

@register.filter(name='mortify')
def mortify(content):
	return content [:250]+'...'

@register.filter(name='shorten_title')
def shorten_title(title):
	return title [:30]+'...'

@register.filter(name='media_url')
def get_media_url(article_id):
	article=get_object_or_404(Article, pk=article_id)
	return article.media.file.url