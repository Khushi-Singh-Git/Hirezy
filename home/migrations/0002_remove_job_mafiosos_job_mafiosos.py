# Generated by Django 4.0.5 on 2022-06-05 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_quizscore_remove_applicant_quiz_score'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='mafiosos',
        ),
        migrations.AddField(
            model_name='job',
            name='mafiosos',
            field=models.ManyToManyField(to='user.mafioso'),
        ),
    ]
