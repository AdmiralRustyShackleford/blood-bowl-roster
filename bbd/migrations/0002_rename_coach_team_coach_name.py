# Generated by Django 4.0.5 on 2022-06-23 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbd', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='coach',
            new_name='coach_name',
        ),
    ]