from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
from .views import MyTokenObtainPairView

#all urls here will be http://127.0.0.1:8000/api/

urlpatterns = [
    path('students/create/',views.create_student,name='create_student'),
    path('students/list/',views.list_student,name='list_student'),
    path('students/view/<int:rollno>/',views.get_student,name='get_student'),
    path('students/delete/<int:rollno>/',views.delete_student,name='delete_student'),
    path('students/update/<int:rollno>/',views.update_student,name='update_student'),
    path('protected/',views.protected_view,name='protected_view'),
    path('token/',MyTokenObtainPairView.as_view(),name='token_obtain_pair')
]