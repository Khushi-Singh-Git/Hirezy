from django import forms
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.forms import UserCreationForm


# class DoctorUserForm(UserCreationForm):
    
#     class Meta:
#         model = User
#         fields = ["first_name", "last_name", "username", "password1", "password2"]

# class DoctorForm(forms.ModelForm):
#     class Meta:
#         model = models.Doctor
#         fields = ["mobile", "department", "profile_pic"]


class ApplicantUserForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password1", "password2"]

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = models.Applicant
        fields = [ "bio","yoe"]

class MafiosoUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password1', 'password2']

class MafiosoForm(forms.ModelForm):
    class Meta:
        model = models.Mafioso
        fields = [ "company_name","bio", "company_departments"]



