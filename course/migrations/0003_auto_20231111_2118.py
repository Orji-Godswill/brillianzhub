# Generated by Django 3.2.13 on 2023-11-11 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='course.course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='course.course'),
            preserve_default=False,
        ),
    ]
