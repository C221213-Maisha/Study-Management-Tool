# Generated by Django 5.1.3 on 2024-12-13 03:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_repository', '0002_folder_file_delete_studymaterial'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subfolders', to='study_repository.folder'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
