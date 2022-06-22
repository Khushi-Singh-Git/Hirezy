from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import Group
# Create your views here.


#Sign Ups
#-------------------------------------START-----------------------------------------------------------------------------------#

def applicantsignup(request):
    userForm = forms.ApplicantUserForm()
    applicantForm = forms.ApplicantForm()
    context = {'userForm':userForm, 'applicantForm':applicantForm}
    if request.method=="POST":
        userForm = forms.ApplicantUserForm(request.POST)
        applicantForm = forms.ApplicantForm(request.POST, request.FILES)
        if userForm.is_valid() and applicantForm.is_valid():
            user = userForm.save()
            user.save()
            applicant = applicantForm.save(commit=False)
            applicant.user = user
            applicant = applicant.save()
            my_applicant_group = Group.objects.get_or_create(name='APPLICANT')
            my_applicant_group[0].user_set.add(user)

            return redirect('applicantsignin')
    return render(request, 'user/applicantsignup.html', context)


def mafiososignup(request):
    userForm = forms.MafiosoUserForm()
    context = {'userForm':userForm}
    if request.method=="POST":
        userForm = forms.MafiosoUserForm(request.POST)
        if userForm.is_valid():
            user = userForm.save()
            user.save()
            my_mafioso_group = Group.objects.get_or_create(name='MAFIOSO')
            my_mafioso_group[0].user_set.add(user)

            return redirect('mafiososignin')
    return render(request, 'user/mafiososignup.html', context)


#Sign Ups
#-------------------------------------END-----------------------------------------------------------------------------------#
