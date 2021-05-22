from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render , HttpResponse,redirect
from .models import users

# Create your views here.
def index(request):
    context={
        "user": users.objects.all()
    }
    return render(request,'index.html',context)

def form(request):
        users.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],email_address=request.POST['Email'],age=request.POST['Age'])
        return redirect('/')