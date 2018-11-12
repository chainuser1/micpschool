from django.db import models

# Create your models here.

class News(models.Model):
    news_title=models.CharField(max_length=30)
    news_body=models.CharField(max_length=3000)
    pub_date=models.DateTimeField('date published')

class Comments(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    comment_text=models.CharField(max_length=200)

