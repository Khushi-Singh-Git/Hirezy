from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('applicantsignup/', views.applicantsignup, name='applicantsignup'),
    path('applicantsignin/', LoginView.as_view(template_name='user/applicantsignin.html'), name='applicantsignin'),
    path('mafiososignup/', views.mafiososignup, name='mafiososignup'),
    path('mafiososignin/', LoginView.as_view(template_name='user/mafiososignin.html'), name='mafiososignin'),
    path('logout/',  LogoutView.as_view(template_name='user/logout.html'), name='logout'),
  


]
