from django.urls import path, include
from . import views
from .views import create_job_posting
from .views import assign_job_posting

urlpatterns = [
    path('', views.login),
    path('signin/', views.signin),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),  
    path('create_job_posting/', create_job_posting, name='create_job_posting'),
    path('assign_job_posting/', assign_job_posting, name='assign_job_posting'),
]