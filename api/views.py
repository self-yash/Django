from django.shortcuts import render,get_object_or_404
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

@api_view(['GET'])
def product_detail(request,pk):
    products = get_object_or_404(Product, pk=pk)
    serializer= ProductSerializer(products)
    return Response(serializer.data)
    