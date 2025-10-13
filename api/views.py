from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
from django.http import JsonResponse

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    serializer= ProductSerializer(products,many=True)
    return JsonResponse({
        'data': serializer.data
    })