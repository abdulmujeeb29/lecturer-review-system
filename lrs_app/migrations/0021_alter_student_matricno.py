# Generated by Django 4.1.7 on 2023-04-04 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lrs_app', '0020_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='matricno',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
