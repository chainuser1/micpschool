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

    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return "Quiz {}".format(self.quiz_num_for_student)

class Category(models.Model):
    """Categories that questions can be in"""
    name = models.CharField(max_length=200, unique=True)
    published = models.BooleanField(default=False)
    description = models.TextField(default="Description for Category")
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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

        return super(Category, self).save(*args, **kwargs)

class Question(models.Model):
    question_text=models.TextField()
    quiz=models.ForeignKey(Quiz, default=0, on_delete=models.CASCADE)
    paginate_by = 10

    def __str__(self):
       return self.question_text

class Answer(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE, default=0, related_name="answers")
    answer_text=models.CharField(max_length=300)
    correct = models.BooleanField(default=False)

    class Meta:
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
    choice = models.ForeignKey(Answer,  on_delete=models.CASCADE)
    attempt_number = models.PositiveSmallIntegerField(blank=True, null=True)
