from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('new_job/', views.new_job, name='new_job'),
]