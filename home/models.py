from django.db import models
from user.models import Mafioso, Applicant
# Create your models here.

departments=(('SDE1','SDE1'),
('SDE2','SDE2'),
('Data Scientist','Data Scientist'),
('Data Analyst','Data Analyst'),
('Financial analyst','Financial analyst'),
('Sales representative','Sales representative'),
('Human resources','Human resources'),
('Marketing coordinator','Marketing coordinator'),
('Operations','Operations'),
('Environmental Engineer','Environmental Engineer')
)

class Job(models.Model):
    job_name = models.CharField(max_length=100)
    mafiosos = models.ManyToManyField(Mafioso)
    job_description = models.CharField(max_length=100) 
    job_department = models.CharField(choices=departments, max_length=200, default='Operations')





# class Department(models.Model):
#     dept_name = models.CharField(choices=departments, max_length=255)
#     dept_description = models.CharField(max_length=500)

class JobApplication(models.Model):
    applicant = models.OneToOneField(Applicant, on_delete=models.CASCADE)
    maafiosos = models.OneToOneField(Mafioso, on_delete=models.CASCADE)
    job = models.OneToOneField(Job, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)


class Questions(models.Model):
    question = models.CharField(max_length=500)
    answer = models.IntegerField()
