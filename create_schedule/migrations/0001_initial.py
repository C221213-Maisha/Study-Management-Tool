# Generated by Django 5.1.3 on 2024-12-19 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('slot', models.IntegerField()),
                ('course_name', models.CharField(max_length=255)),
                ('teacher_name', models.CharField(max_length=255)),
                ('class_time', models.CharField(max_length=100)),
                ('classroom_number', models.CharField(max_length=50)),
            ],
        ),
    ]
