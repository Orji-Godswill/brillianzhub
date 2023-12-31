# Generated by Django 3.2.13 on 2023-09-23 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='instructor',
            field=models.BooleanField(default=False),
        ),
    ]
