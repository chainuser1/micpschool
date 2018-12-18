from django.contrib import admin
from .models import Question, Answer, ICategory
# Register your models here.

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 4

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Your Quiz Category: ', {'fields' : ['name', 'published','slug', 'description']})
    ]
    inlines = [QuestionInline]

class AnswerInline(admin.StackedInline):
    model = Answer
    limit = 4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Your Question Here: ', {'fields':['question_text']})
    ]
    inlines = [AnswerInline]



admin.site.register(ICategory, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
