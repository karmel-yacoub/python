from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    context={
        'all_dojos':Dojo.objects.all(),
    }
    return render(request,'index.html',context)
def creat(request):
     data1= Dojo.objects.create(name=request.POST['name'],city=request.POST['city'],state=request.POST['state'])
     return redirect('/')
def add(request):
    data2=Ninja.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],dojo=Dojo.objects.get(id=request.POST['children']))
    return redirect('/')
