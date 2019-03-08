from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
import itertools
import string

# Create your models here.
class News(models.Model):
	publisher = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="news")
	title = models.CharField(max_length=200, default=None)
	content = models.TextField(default=None)
	slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(default=timezone.now)

	def save(self, *args, **kwargs):
		if not self.slug:
			max_length = 200
			self.slug = orig = slugify(self.title)[:max_length]
			for x in itertools.count(1):
				if not News.objects.filter(slug=self.slug).exists():
					break
				# Truncate the original slug dynamically. Minus 1 for the hyphen
				self.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)
		return super(News, self).save(*args, **kwargs)

	def __str__(self):
		return self.title.cap_words()

	def __str__(self):
		return self.content

	class Meta:
		verbose_name='News'
		verbose_name_plural='News'

#=>media upload
class Media(models.Model):
	news  = models.ForeignKey(News, on_delete=models.CASCADE, default=None)
	file = models.ImageField(upload_to='news_media', blank=True)
	description = models.CharField(max_length=300, default=None)


# comments for article
class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	news = models.ForeignKey(News, on_delete=models.CASCADE, default=None)
	text = models.CharField(max_length=500, default=None)