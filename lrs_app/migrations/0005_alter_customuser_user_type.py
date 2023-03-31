# Generated by Django 4.1.7 on 2023-03-25 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lrs_app', '0004_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('admin', 'admin'), ('lecturer', 'lecturer'), ('student', 'student')], default='admin', max_length=10),
        ),
    ]