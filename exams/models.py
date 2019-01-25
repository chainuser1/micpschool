from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.

class Quiz(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    quiz_num_for_student = models.IntegerField(default=0)
    #question_ids = models.TextField(default=None)
    num_questions = models.IntegerField(null=True)
    complete = models.BooleanField(default=False)
    final_score = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=5)

    class Meta:
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return "Quiz {}".format(self.quiz_num_for_student)

class ICategory(models.Model):
    """Categories that questions can be in"""
    name = models.CharField(max_length=200, unique=True)
    published = models.BooleanField(default=False)
    description = models.TextField(default="Description for ICategory")
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)


    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def active_questions(self):
        return self.questions.filter(published=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            max_length = 200
            self.slug = orig = slugify(self.name)[:max_length]

            for x in itertools.count(1):
                if not Question.objects.filter(slug=self.slug).exists():
                    break

                # Truncate the original slug dynamically. Minus 1 for the hyphen.
                self.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

        return super(ICategory, self).save(*args, **kwargs)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    title = models.CharField(max_length=120, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    icategory = models.ForeignKey(ICategory, related_name='questions', on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    save_for_exam = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            max_length = 200
            self.slug = orig = slugify(self.question_text)[:max_length]

            for x in itertools.count(1):
                if not Question.objects.filter(slug=self.slug).exists():
                    break

                # Truncate the original slug dynamically. Minus 1 for the hyphen.
                self.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

        return super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE, default=0, related_name="answers")
    answer_text=models.CharField(max_length=300)
    correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Answers"
        unique_together = [
            #one unique answer for each question
            ('question', 'answer_text')
        ]

    def __str__(self):
        return self.answer_text

    def __boolean__(self):
        return self.correct

class QuestionResponse(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="responses", null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,  on_delete=models.CASCADE)
    # attempt_number = models.PositiveSmallIntegerField(blank=True, null=True)



