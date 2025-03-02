from django.urls import path
from django.shortcuts import render
from . import views

app_name='portfolio'

urlpatterns = [
    path("",views.home, name="home"),
    path("about/",views.about, name="about"),
    path("projects/",views.projects, name="projects"),
    path("contact/",views.contact, name="contact"),
    path('contact/success/', views.contact_success, name='contact_success'),
]
