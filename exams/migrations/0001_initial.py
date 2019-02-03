# Generated by Django 2.1.4 on 2019-02-01 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=300)),
                ('correct', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Answers',
            },
        ),
        migrations.CreateModel(
            name='ICategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('published', models.BooleanField(default=False)),
                ('description', models.TextField(default='Description for ICategory')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
                ('published', models.BooleanField(default=False)),
                ('save_for_exam', models.BooleanField(default=False)),
                ('icategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='exams.ICategory')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='exams.Question'),
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('question', 'answer_text')},
        ),
    ]
