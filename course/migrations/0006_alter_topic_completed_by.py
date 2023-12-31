# Generated by Django 3.2.13 on 2023-11-12 05:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0005_alter_topic_completed_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='completed_by',
            field=models.ManyToManyField(blank=True, related_name='completed_topics', to=settings.AUTH_USER_MODEL),
        ),
    ]