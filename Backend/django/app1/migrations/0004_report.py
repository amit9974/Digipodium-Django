# Generated by Django 4.1.1 on 2022-09-28 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.IntegerField()),
                ('hindi', models.IntegerField()),
                ('science', models.IntegerField()),
                ('math', models.IntegerField()),
                ('computer', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.student')),
            ],
        ),
    ]
