# Generated by Django 4.0.4 on 2022-09-27 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0075_blog_blog_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='class_name',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
