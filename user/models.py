from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

company_departments = (('Water','Water'),
('Fire','Fire'),
('Air','Air'),
('Earth','Earth'),
('Heart','Heart'),
)

skills_list = (('Resilience','Resilience' ),
    ('Good communication','Good communication' ),
    ('Leadership', 'Leadership'),
    ('Management','Management' ),
    ('Adaptability', 'Adaptability'),
    ('Team Player','Team Player' ),
    ('Problem Solving Skills','Problem Solving Skills' ),
    ('Critical Thinking Skills', 'Critical Thinking Skills'),
    ('Flexibility','Flexibility' ),
    ('Organization Skills', 'Organization Skills'),
    ('Management','Management' ),
    ('Adaptability', 'Adaptability'),
    ('Creativity','Creativity' ),
    ('Computer Software and Application Knowledge', 'Computer Software and Application Knowledge'),
    ('Data Analysis','Data Analysis' ),
    ('Project Management', 'Project Management'),
    ('Marketing','Marketing' ),
    ('Coding', 'Coding'),
    ('Debugging','Debugging' ),
    ('C++', 'C++'),
    ('SQL','SQL' ),
    ('Python', 'Python'),
    ('Java','Java' ),
    ('JavaScript', 'JavaScript'),
    ('Servers','Servers' ),
    ('Network Security', 'Network Security'),
    ('SAS','SAS' ),
    ('Machine Learning','Machine Learning' ),
    ('Artificial Intelligence', 'Artificial Intelligence'),
    ('Algorithms','Algorithms' ),
    ('Big Data', 'Big Data'),
    )
    
    
    
    
    
    


# Create your models here.
class Mafioso(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=500)
    bio = models.CharField(max_length=500)
    company_departments = models.CharField(max_length=500, choices=company_departments, default='Earth')





class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)
    yoe = models.IntegerField()
    profile_pic = models.ImageField(upload_to = 'static/user/profile_pic/', null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    skills = MultiSelectField(choices = skills_list, max_choices=5, null=True)
    compat_score = models.CharField(max_length=100)

class QuizScore(models.Model):
    quiz_score = models.IntegerField(default=0)