# Generated by Django 4.1.7 on 2023-04-05 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lrs_app', '0030_remove_lecturer_email_remove_lecturer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='phone_number',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
