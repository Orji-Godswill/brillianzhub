# Generated by Django 3.2.13 on 2024-01-12 13:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0014_auto_20240112_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objective',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='courses_joined', to=settings.AUTH_USER_MODEL),
        ),
    ]
