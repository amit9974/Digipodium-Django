# Generated by Django 4.1.1 on 2022-10-28 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_category_sub_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_category',
        ),
    ]