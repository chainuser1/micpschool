# Generated by Django 2.1.5 on 2019-02-11 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exams', '0002_auto_20190204_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_num_for_student', models.IntegerField(default=0)),
                ('num_questions', models.IntegerField(null=True)),
                ('complete', models.BooleanField(default=False)),
                ('final_score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'answer', 'verbose_name_plural': 'answers'},
        ),
        migrations.AlterField(
            model_name='questionresponse',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response', to='exams.Answer'),
        ),
        migrations.AlterField(
            model_name='questionresponse',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response', to='exams.Question'),
        ),
        migrations.AlterField(
            model_name='questionresponse',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to=settings.AUTH_USER_MODEL),
        ),
    ]
