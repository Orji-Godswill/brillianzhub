# Generated by Django 3.2.13 on 2024-01-06 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0002_alter_appointment_number_team_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='number_team_members',
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointment_type',
            field=models.CharField(choices=[('1', 'Stock Investment'), ('2', 'Real Estate'), ('4', 'Personal Finance'), ('more than 3', 'Others')], default='1', max_length=15),
        ),
    ]