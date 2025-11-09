from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('product/', views.ProductListAPIView.as_view()),
    path('product/info',views.product_info),
    path('product/<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('order/', views.order_list),
]