# Generated by Django 3.2.13 on 2023-09-09 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]