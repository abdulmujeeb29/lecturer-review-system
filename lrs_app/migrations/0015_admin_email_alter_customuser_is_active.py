# Generated by Django 4.1.7 on 2023-04-01 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lrs_app', '0014_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
