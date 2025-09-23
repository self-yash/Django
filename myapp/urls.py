from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('students/create/',views.create_student,name='create_student'),
    path('students/list/',views.list_student,name='list_student'),
    path('students/view/<int:rollno>/',views.get_student,name='get_student'),
    path('students/delete/<int:rollno>/',views.delete_student,name='delete_student'),
    path('students/update/<int:rollno>/',views.update_student,name='update_student'),
]