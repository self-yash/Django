from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('product/', views.product_list),
    path('product/info',views.product_info),
    path('product/<int:pk>/', views.product_detail),
    path('order/', views.order_list),
]