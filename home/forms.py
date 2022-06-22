from django import forms
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.forms import UserCreationForm

class QuizForm(forms.ModelForm):
    class Meta:
        model = models.Questions
        fields = ['answer',]
    