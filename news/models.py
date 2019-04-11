from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
import itertools, string
import string
from django.conf import settings
# Create your models here.
class Article(models.Model):
	publisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, related_name="articles")
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
				if not Article.objects.filter(slug=self.slug).exists():
					break
				# Truncate the original slug dynamically. Minus 1 for the hyphen
				self.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)
		return super(Article, self).save(*args, **kwargs)

	def __str__(self):
		return string.capwords(self.title)


	class Meta:
		verbose_name='Article'
		verbose_name_plural='Articles'

#media upload
class Media(models.Model):
	article  = models.ForeignKey(Article, on_delete=models.CASCADE)
	file = models.ImageField(upload_to='news_media', blank=True)
	description = models.CharField(max_length=300, default=None)

	class Meta:
		verbose_name='medium'
		verbose_name_plural='media'

	def __unicode__(self):
		return self.file

	def __str__(self):
		return self.description

# comments for article
class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, related_name="comments")
	article = models.ForeignKey(Article, on_delete=models.CASCADE, default=None, related_name="comments")
	text = models.CharField(max_length=500, default=None)