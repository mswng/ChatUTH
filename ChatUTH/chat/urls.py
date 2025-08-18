from django.contrib import admin
from django.urls import path
# from django.shortcuts import render 
from . import views
from .views import *



urlpatterns = [
    path('', views.TrangChu, name= 'TrangChu'),
    # path('admin/', admin.site.urls), 
    path('ChatURLAdmin/', views.add_crawled_page, name='ChatURLAdmin'),
    path('them_nhanh/', views.admin, name='ThemNhanh'),
    path('quanLy/', views.quanLi, name='quanLy')

]