# Generated by Django 4.1.1 on 2022-10-12 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_alter_images_upload_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='upload_at',
            field=models.DateField(auto_created=True, null=True),
        ),
    ]
