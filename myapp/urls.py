from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contacts", views.contacts, name='contacts'),
    path("familypack", views.familypack, name='familypack'),
    path("cream", views.cream, name='cream'),
    path("softy", views.softy, name='softy'),
]
