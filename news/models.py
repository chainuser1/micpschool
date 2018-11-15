from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class News(models.Model):
    news_title=models.CharField(max_length=30)
    news_body=models.CharField(max_length=3000)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.news_title

    def __str__(self):
        return self.news_body

    def __datetime__(self):
        return self.pub_date

    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)


class Comments(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    comment_text=models.CharField(max_length=200)
    def __str__(self):
        return self.comment_text
