# Generated by Django 4.1.7 on 2023-04-06 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lrs_app', '0032_alter_review_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lrs_app.student'),
        ),
    ]
