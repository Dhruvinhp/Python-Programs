from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('', views.index, name='web'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
]
