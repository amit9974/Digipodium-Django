# Generated by Django 4.1.1 on 2022-10-01 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='upload_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]