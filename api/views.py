from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer= ProductSerializer(products,many=True)
    return Response(serializer.data)

def product_detail(request,pk):
