from django.http import HttpResponse
from django.shortcuts import render
from .models import place,team

# Create your views here.
def homepage(request):
    name = 'India'
    return render(request,"HomePage.html",{'obj': name})
def about(request):
    return HttpResponse("Hello I am About")
def contact(request):
    return render(request,"contact.html")
def detail(request):
    return HttpResponse("Hello I am Detail")
def thanks(request):
    return render(request,"thanks.html")
def add(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    return render(request,"add.html",{'Add': add,'Sub': sub,'Mul': mul,'Div': div})
def index(request):
    obj = place.objects.all()
    obj1 = team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

