# Generated by Django 4.1.1 on 2022-10-28 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_blog_caption_blog_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='subject',
        ),
    ]