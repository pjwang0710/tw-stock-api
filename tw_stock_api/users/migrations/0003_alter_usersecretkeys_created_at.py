# Generated by Django 3.2.3 on 2021-05-20 08:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210520_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersecretkeys',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
