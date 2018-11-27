from django.db import models

# Create your models here.

class Question(models.Model):
    question_text=models.CharField(max_length=120)

    def __str__(self):
       return self.question_text

class Answer(models.Model):
    answer_id=models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text=models.CharField(max_length=70)
    right_answer=models.CharField(max_length=70)

    def __str__(self):
        return self.answer_text
    def __str__(self):
        return self.right_answer

class Choice(models.Model):
    choice_id=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_ans=models.CharField(max_length=70)

    def __str__(self):
        return self.choice_ans
