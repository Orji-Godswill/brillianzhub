# Generated by Django 3.2.13 on 2024-01-04 19:04

import ckeditor_uploader.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='text_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]