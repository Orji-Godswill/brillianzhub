# Generated by Django 3.2.13 on 2023-10-26 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('package', '0001_initial'),
        ('dividend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dividend',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_dividend', to='package.package'),
        ),
    ]
