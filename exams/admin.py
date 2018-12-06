from django.contrib import admin
from .models import Question, Answer, Quiz
# Register your models here.

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 10

class QuizAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Your Quiz Category: ', {'fields' : ['quiz_text']})
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



admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
