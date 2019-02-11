from django import template
from django.contrib.auth.models import Group

# use to register functions as template tags
register =  template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
	# return True if group in user.groups.all() else False
	return user.groups.filter(name=group_name).exists()