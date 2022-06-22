from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homeclick/', views.homeclick, name='homeclick'),
    path('mafiosoclick/', views.mafiosoclick, name='mafiosoclick'),
    path('applicantclick/', views.applicantclick, name='applicantclick'),
    path('applicantdashboard/', views.applicantdashboard, name='applicantdashboard'),
    path('applicantswipejob/<str:slug>/<int:id>/', views.applicantswipejob, name='applicantswipejob'),
    path('applicantrightswipejob/', views.applicantrightswipejob, name='applicantrightswipejob'),
    path('applicantleftswipejob/', views.applicantleftswipejob, name='applicantleftswipejob'),
    path('applicantprofile/', views.applicantprofile, name='applicantprofile'),
    path('applicantupdateprofile/', views.applicantupdateprofile, name='applicantupdateprofile'),
    path('applicantviewappliedjobs/', views.applicantviewappliedjobs, name='applicantviewappliedjobs'),
    path('applicantmessages/', views.applicantmessages, name='applicantmessages'),
    path('quizpage/', views.quizpage, name='quizpage'),
    path('quizpage2/', views.quizpage2, name='quizpage2'),
    path('quizpage3/', views.quizpage3, name='quizpage3'),
    path('quizpage4/', views.quizpage4, name='quizpage4'),
    path('quizpage5/', views.quizpage5, name='quizpage5'),
    path('quizresult/', views.quizresult, name='quizresult'),
    path('applicantapply/<str:slug>/<int:id>/', views.applicantapply, name='applicantapply'),
    path('applicantviewjobs/', views.applicantviewjobs, name='applicantviewjobs'),
    path('deletejobs/', views.deletejobs, name='deletejobs'),


    path('afterlogin/', views.afterlogin, name='afterlogin'),

]
