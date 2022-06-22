# Generated by Django 4.0.5 on 2022-06-04 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mafioso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=500)),
                ('bio', models.CharField(max_length=500)),
                ('company_departments', models.CharField(choices=[('Water', 'Water'), ('Fire', 'Fire'), ('Air', 'Air'), ('Earth', 'Earth'), ('Heart', 'Heart')], default='Earth', max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=500)),
                ('yoe', models.IntegerField()),
                ('profile_pic', models.ImageField(upload_to='static/user/profile_pic/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('skills', multiselectfield.db.fields.MultiSelectField(choices=[('Resilience', 'Resilience'), ('Good communication', 'Good communication'), ('Leadership', 'Leadership'), ('Management', 'Management'), ('Adaptability', 'Adaptability'), ('Team Player', 'Team Player'), ('Problem Solving Skills', 'Problem Solving Skills'), ('Critical Thinking Skills', 'Critical Thinking Skills'), ('Flexibility', 'Flexibility'), ('Organization Skills', 'Organization Skills'), ('Management', 'Management'), ('Adaptability', 'Adaptability'), ('Creativity', 'Creativity'), ('Computer Software and Application Knowledge', 'Computer Software and Application Knowledge'), ('Data Analysis', 'Data Analysis'), ('Project Management', 'Project Management'), ('Marketing', 'Marketing'), ('Coding', 'Coding'), ('Debugging', 'Debugging'), ('C++', 'C++'), ('SQL', 'SQL'), ('Python', 'Python'), ('Java', 'Java'), ('JavaScript', 'JavaScript'), ('Servers', 'Servers'), ('Network Security', 'Network Security'), ('SAS', 'SAS'), ('Machine Learning', 'Machine Learning'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Algorithms', 'Algorithms'), ('Big Data', 'Big Data')], max_length=416)),
                ('compat_score', models.CharField(max_length=100)),
                ('quiz_score', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]