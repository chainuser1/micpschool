from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Quiz(models.Model):
    quiz_text=models.CharField(max_length=50)
    def __str__(self):
        return self.quiz_text

class Question(models.Model):
    question_text=models.TextField()
    quiz=models.ForeignKey(Quiz, default=0, on_delete=models.CASCADE)
    paginate_by = 10

    def __str__(self):
       return self.question_text

class Answer(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE, default=0)
    answer_text=models.CharField(max_length=300)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text


class Choice(models.Model):
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_given = models.ForeignKey(Answer, on_delete=models.CASCADE)
    choice_text  = models.CharField(max_length=300, default=None)

