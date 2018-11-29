from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Quiz(models.Model):
    quiz_text=models.CharField(max_length=50)
    def __str__(self):
        return self.quiz_text

class Question(models.Model):
    question_text=models.CharField(max_length=120)
    quiz=models.ForeignKey(Quiz, default=0, on_delete=models.CASCADE)
    right_answer=models.CharField(max_length=70, default='None')
    paginate_by = 10
    def __str__(self):
       return self.question_text

class Answer(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE, default=0)
    answer_text=models.CharField(max_length=70)
    def __str__(self):
        return self.answer_text


class Choice(models.Model):
    answer=models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    choice_ans=models.CharField(max_length=70)
    def __str__(self):
        return self.choice_ans
