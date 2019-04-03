from django import template
from django.shortcuts import render, get_object_or_404
import string
register =  template.Library()

@register.filter(name='capitalize')
def title_cap(title):
	return string.capwords(title)

@register.filter(name='mortify')
def display_200(content):
	return content [:200]+'...'