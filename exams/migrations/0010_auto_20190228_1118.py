# Generated by Django 2.1.5 on 2019-02-28 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0009_auto_20190228_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselindex',
            name='file',
            field=models.ImageField(upload_to='carousel_index'),
        ),
    ]
