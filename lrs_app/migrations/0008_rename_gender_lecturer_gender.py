# Generated by Django 4.1.7 on 2023-03-26 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lrs_app', '0007_remove_customuser_gender_alter_lecturer_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecturer',
            old_name='Gender',
            new_name='gender',
        ),
    ]