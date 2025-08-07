from django.contrib import admin
from django.urls import path
# from django.shortcuts import render 
from . import views
from .views import *



urlpatterns = [
    path('', views.TrangChu, name= 'TrangChu'),
    
]