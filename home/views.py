from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Job, JobApplication, Questions
from user.models import Applicant, Mafioso, QuizScore
from django.contrib.auth.models import User
from user.forms import ApplicantUserForm, MafiosoUserForm, ApplicantForm
from home.forms import QuizForm



# Create your views here.


#Checking if the user is an applicant/mafioso
#-------------------------------------START-----------------------------------------------------------------------------------#



def is_applicant(user):
    return user.groups.filter(name='APPLICANT').exists()

def is_mafioso(user):
    return user.groups.filter(name='MAFIOSO').exists()


#Checking if the user is an applicant/mafioso
#-------------------------------------END-----------------------------------------------------------------------------------#




#Clicks on homepage
#-------------------------------------START-----------------------------------------------------------------------------------#



def homeclick(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/afterlogin')
    return render(request, 'home/homeclick.html')


def mafiosoclick(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/afterlogin')
    return render(request, 'home/mafiosoclick.html')

def applicantclick(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'home/applicantclick.html')



#Clicks on homepage
#-------------------------------------END-----------------------------------------------------------------------------------#



# def quizpage1(request):
#     form = Quizpage1form()
#     if request.method=="POST":
#         a = Questions.objects.filter(ans=request.ans).exists()
#         if a:
#             a = Applicant()
#             a.quiz_marks+=1
#         else:
#             pass
#         redirect('quizpage2')
#     return render(request, 'home/quizpage1.html', context={'form':form,})

#Rerouting to the dashboard after logging in
#-------------------------------------START-----------------------------------------------------------------------------------#


def afterlogin(request):
    if is_applicant(request.user):
        return redirect('applicantdashboard')
        
    elif is_mafioso(request.user):
        return redirect('mafiosodashboard')

#Rerouting to the dashboard after logging in
#-------------------------------------END-----------------------------------------------------------------------------------#



#Applicant Dashboard
#-------------------------------------START-----------------------------------------------------------------------------------#



@login_required(login_url='applicantsignin')
@user_passes_test(is_applicant)
def applicantdashboard(request):
    applicant=Applicant.objects.get(user_id=request.user.id)
    jobs = Job.objects.all()
    mafioso = ['GREEN WORK', 'LEAP CITIES', 'ThingsCloud']
    mydict={
    'applicant':applicant,
    'jobs':jobs,
    'mafioso':mafioso,
    }
    return render(request,'home/applicantdashboard.html',context=mydict)

global count
count = 0


@login_required(login_url='applicantsignin')
@user_passes_test(is_applicant)
def applicantviewjob(request, slug):
    global count
    job = Job.objects.filter(job_department=slug)
    redirect_url = 'applicantswipejob'
    slug = slug
    id = job.id[count]
    count+=1
    return redirect(f'{redirect_url}/{slug}/{id}')


@login_required(login_url='applicantsignin')
@user_passes_test(is_applicant)
def applicantswipejob(request, slug, id):
    global count
    job_by_dept = Job.objects.get(job_department=slug)
    if count>len(job_by_dept.job_name):
        count=0
        redirect('jobsfinished')
    job = Job.objects.filter(job_department=slug, id=id)
    slug = slug
    id = job_by_dept.id[count]
    count+=1
    context = {
        'job':job,
        'slug':slug,
        'id':id,    
        }
    redirect_url = 'applicantswipejob'
    
    return render(request, 'home/applicantswipejob.html', context)

@login_required(login_url='applicantsignin')
@user_passes_test(is_applicant)
def applicantrightswipejob(request, slug, id):
    global count
    jobapplication = JobApplication()
    user = User.objects.get(id = request.user.id)
    applicant = Applicant.objects.get(first_name=user.first_name)
    job = Job.objects.get(id=id)
    mafiosos = job.mafiosos
    jobapplication.applicant = applicant
    jobapplication.job=job
    jobapplication.maafiosos=mafiosos
    jobapplication.save()
    job_by_dept = Job.objects.filter(job_department=slug)
    redirect_url = 'applicantswipejob'
    slug = slug
    id = job_by_dept.id[count]
    count+=1
    return redirect(f'{redirect_url}/{slug}/{id}')

@login_required(login_url='applicantsignin')
@user_passes_test(is_applicant)
def applicantleftswipejob(request, slug, id):
    global count
    job_by_dept = Job.objects.filter(job_department=slug)
    redirect_url = 'applicantswipejob'
    slug = slug
    id = job_by_dept.id[count]
    count+=1
    return redirect(f'{redirect_url}/{slug}/{id}')



@login_required(login_url='applicantsignin')
@user_passes_test(is_applicant)
def applicantprofile(request):
    applicant = Applicant.objects.get(id=request.user.id)
    context = {
        'applicant':applicant,
    }
    return render(request,'home/applicantprofile.html',context=context)

@login_required(login_url='applicantsignin')
@user_passes_test(is_applicant)
def applicantupdateprofile(request):
    applicant = Applicant.objects.get(id=request.user.id)
    user=User.objects.get(id=applicant.user_id)

    userForm=ApplicantUserForm(instance=user)
    applicantForm=ApplicantForm(request.FILES,instance=user)
    mydict={'userForm':userForm,'applicantForm':applicantForm}
    if request.method=='POST':
        userForm=ApplicantUserForm(request.POST,instance=user)
        applicantForm=ApplicantForm(request.POST,request.FILES,instance=applicant)
        if userForm.is_valid() and applicantForm.is_valid():
            user=userForm.save()
            user.save()
            applicant=applicantForm.save(commit=False)
            applicant.save()
            return redirect('applicantprofile')
    return render(request,'home/applicantupdateprofile.html',context=mydict)


@login_required(login_url='applicantsignin')
@user_passes_test(is_applicant)
def applicantviewjobs(request):
    job = Job.objects.all()
    context = {
        'job':job,
    }
    return render(request, 'home/applicantviewjob.html', context)

@login_required(login_url='applicantsignin')
@user_passes_test(is_applicant)
def deletejobs(request):
    job = Job.objects.all().first()
    job.delete()
    job.save()
    return redirect(applicantviewjob)

@login_required(login_url='applicantsignin')
@user_passes_test(is_applicant)
def applicantviewappliedjobs(request):
    job = JobApplication.objects.get(applicant=request.user.applicant)
    context = {
        'job':job,
    }
    return render(request, 'home/applicantviewappliedjob.html', context)

# @login_required(login_url='applicantlogin')
# @user_passes_test(is_applicant)
# def applicantapplyjobs(request):
#     job = JobApplication()

#     context = {
#         'job':job,
#     }
#     return render(request, 'home/applicantviewappliedjob.html', context)

@login_required(login_url='applicantsignin')
@user_passes_test(is_applicant)
def applicantmessages(request):
    return render(request, 'home/applicantmessages.html')



'''def quizpage1(request):
    form = Quizpage1form()
    if request.method == "POST":
        a = Questions.objects.filter(ans=request.ans).exists()
        if a:
            a = Applicant()
            a.quiz_marks += 1
        else:
            pass
        redirect('quizpage2')
    return render(request, 'home/quizpage1.html', context={'form': form, })'''

# global count1
# count1=0
# def quizpage(request):
#     global count1
#     print(count1)
#     count1=0
#     quizscore = QuizScore.objects.all()
    
#     if count1<5:
#         quizform = QuizForm()
#         questions = Questions.objects.all()
#         question = questions[count1].question
#         answer = questions[count1].answer
#         context = {
#             'question':question,
#             'answer':answer,
#         }
#         print(count1)

#         if request.method=="POST":
#             print(count1)

#             answer = request.POST.get('answer')
#             print(answer)
#             print(questions[count1].answer)
#             if int(answer)==int(questions[count1].answer):
#                 a = QuizScore.objects.get(pk=1)
#                 print(a.quiz_score)
#                 a.quiz_score+=1
#                 print(a.quiz_score)
#                 QuizScore.objects.all().update(quiz_score = a.quiz_score)
#                 count1+=1
#                 print(count1)
#     else:
#         count1= 0
#         return render(request, 'home/quizresult.html', context={'quizscore':a.quizscore,})

        
    
#     return render(request, 'home/quizpage.html', context)

# def quizpage(request, pk):
#     # print(count1)
#     # count1=0
#     quizscore = QuizScore.objects.all()
    
#     if pk<5:
#         quizform = QuizForm()
#         questions = Questions.objects.all()
#         question = questions[pk].question
#         answer = questions[pk].answer
#         context = {
#             'question':question,
#             'answer':answer,
#         }
#         print(pk)

#         if request.method=="POST":
#             print(pk)

#             answer = request.POST.get('answer')
#             print(answer)
#             print(questions[pk].answer)
#             if int(answer)==int(questions[pk].answer):
#                 a = QuizScore.objects.get(pk=1)
#                 print(a.quiz_score)
#                 a.quiz_score+=1
#                 print(a.quiz_score)
#                 QuizScore.objects.all().update(quiz_score = a.quiz_score)
#                 pk+=1
#                 print(pk)
#     else:
#         pk= 0
#         return render(request, 'home/quizresult.html', context={'quizscore':a.quizscore,})

        
    
#     return render(request, 'home/quizpage.html', context)


# from .serializers import QuestionSerializer
# from rest_framework.generics import ListAPIView
# from rest_framework.permissions import IsAdminUser
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser

# @csrf_exempt
# def quizpage(request):
#     """
#     List all transformers, or create a new transformer
#     """
#     applicant = Applicant.objects.filter(id=request.user.id)
#     if count1>4:
#         return render(request, 'home/quizresult.html', context={'applicant':applicant,})
#     else:
#         quizform = QuizForm()
#         questions = Questions.objects.all()
#         question = questions[count1].question
#         answer = questions[count1].answer
#         context = {
#             'question':question,
#             'answer':answer,
#         }
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = QuestionSerializer(data=data)
#         if serializer.is_valid():
#             answer = serializer.data['answer']
#             if answer==applicant.answer[count1]:
#                 applicant.quiz_marks+=1
#                 applicant.save()
#     return render(request, 'home/quizpage.html', context)



def quizpage(request):
    a=0
    questions = Questions.objects.all()
    question = questions[a].question
    answer = questions[a].answer
    context = {
        'question':question,
        'answer':answer,
    }

    if request.method=="POST":

        answer = request.POST.get('answer')
        if int(answer)==int(questions[a].answer):
            a = QuizScore.objects.get(pk=1)
            if a.quiz_score>5:
                QuizScore.objects.all().update(quiz_score = 0)
                a = QuizScore.objects.get(pk=1)
                a.quiz_score+=1 
            a.quiz_score+=1
            QuizScore.objects.all().update(quiz_score = a.quiz_score)
        return redirect('quizpage2')

    return render(request, 'home/quizpage.html', context)

def quizpage2(request):
    a=1
    questions = Questions.objects.all()
    question = questions[a].question
    answer = questions[a].answer
    context = {
        'question':question,
        'answer':answer,
    }

    if request.method=="POST":

        answer = request.POST.get('answer')
        if int(answer)==int(questions[a].answer):
            a = QuizScore.objects.get(pk=1)
            if a.quiz_score>5:
                QuizScore.objects.all().update(quiz_score = 0)
                a = QuizScore.objects.get(pk=1)
                a.quiz_score+=1 
            a.quiz_score+=1
            QuizScore.objects.all().update(quiz_score = a.quiz_score)
        return redirect('quizpage3')
    return render(request, 'home/quizpage.html', context)

def quizpage3(request):
    a=2
    questions = Questions.objects.all()
    question = questions[a].question
    answer = questions[a].answer
    context = {
        'question':question,
        'answer':answer,
    }

    if request.method=="POST":

        answer = request.POST.get('answer')
        if int(answer)==int(questions[a].answer):
            a = QuizScore.objects.get(pk=1)
            if a.quiz_score>5:
                QuizScore.objects.all().update(quiz_score = 0)
                a = QuizScore.objects.get(pk=1)
                a.quiz_score+=1 
            a.quiz_score+=1
            QuizScore.objects.all().update(quiz_score = a.quiz_score)
        return redirect('quizpage4')
    return render(request, 'home/quizpage.html', context)


def quizpage4(request):
    a=3
    questions = Questions.objects.all()
    question = questions[a].question
    answer = questions[a].answer
    context = {
        'question':question,
        'answer':answer,
    }

    if request.method=="POST":

        answer = request.POST.get('answer')
        if int(answer)==int(questions[a].answer):
            a = QuizScore.objects.get(pk=1)
            if a.quiz_score>5:
                QuizScore.objects.all().update(quiz_score = 0)
                a = QuizScore.objects.get(pk=1)
                a.quiz_score+=1 
            a.quiz_score+=1
            QuizScore.objects.all().update(quiz_score = a.quiz_score)
        return redirect('quizpage5')
    return render(request, 'home/quizpage.html', context)


def quizpage5(request):
    a=4
    questions = Questions.objects.all()
    question = questions[a].question
    answer = questions[a].answer
    context = {
        'question':question,
        'answer':answer,
    }

    if request.method=="POST":

        answer = request.POST.get('answer')
        if int(answer)==int(questions[a].answer):
            a = QuizScore.objects.get(pk=1)
            if a.quiz_score>5:
                QuizScore.objects.all().update(quiz_score = 0)
                a = QuizScore.objects.get(pk=1)
                a.quiz_score+=1 
            a.quiz_score+=1
            QuizScore.objects.all().update(quiz_score = a.quiz_score)
        return redirect('quizresult')
    return render(request, 'home/quizpage.html', context)


def quizresult(request):
    a = QuizScore.objects.get(pk=1)
    b = a.quiz_score
    context = {
        'quizresult':b
    }
    QuizScore.objects.all().update(quiz_score = 0)
    return render(request, 'home/quizresult.html', context)


@login_required(login_url='applicantsignin')
@user_passes_test(is_applicant)
def applicantapply(request, slug, id):
    jobapplication = JobApplication()
    user = User.objects.get(id = request.user.id)
    applicant = Applicant.objects.get(id=request.user.id)
    job = Job.objects.get(id=id)
    mafiosos = job.mafiosos
    jobapplication.applicant = applicant
    jobapplication.job=job
    jobapplication.maafiosos=mafiosos
    jobapplication.save()
    return redirect('applicantdashboard')