# Generated by Django 4.1.7 on 2023-04-04 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lrs_app', '0025_rename_gender_lecturer_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecturer',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='lecturer',
            old_name='lastname',
            new_name='last_name',
        ),
    ]