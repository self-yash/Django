from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("This is home page")
    return render(request,"learn/index.html")

def about(request):
    # return HttpResponse("This is about page")
    return render(request,"learn/index2.html")

def contact(request):
    # return HttpResponse("This is Contact page")
    return render(request,"learn/contact.html")