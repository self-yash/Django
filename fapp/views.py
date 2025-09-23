from django.shortcuts import render
from rest_framework import viewsets
from .models import McDonalds
from .serializers import BookSerializer

# Create your views here.

def Home(request):
    return render(request,'McD/home.html')

def Menu(request):
    return render(request,'McD/menu.html')

class BookViewSet(viewsets.ModelViewSet):
    queryset = McDonalds.objects.all()
    serializer_class = BookSerializer