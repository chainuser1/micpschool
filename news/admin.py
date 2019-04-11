from django.contrib import admin
from .models import Article, Media
# Register your models here.


class MediaInline(admin.TabularInline):
	model=Media
	max_num = 1

class ArticleAdmin(admin.ModelAdmin):
	readonly_fields = ['slug']
	inlines = [MediaInline]
	

admin.site.register(Article, ArticleAdmin)
