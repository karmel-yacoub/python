from django.http import request
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    
    context={
        'shows':shows.objects.all()
    }
    
    return render(request,'show.html',context)

def form(request):
    return render(request,'index.html')


def create(request):
    errors = shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')
    data=shows.objects.create(title=request.POST['title'],network=request.POST['network'],released_date=request.POST['release'],description=request.POST['description'])
    return redirect('/shows/'+str(data.id))

def information(request,the_id):
    context={
    "form":shows.objects.get(id=the_id)
    }
    return render(request,'information.html',context)

def edit(request,c_id):

    time=shows.objects.get(id=c_id).released_date
    c = shows.objects.get(id=c_id)
    context={
        "show": c,
        "date": time.strftime('%Y-%M-%D')
    }
    
    return render(request,'edit.html',context)


def update(request,e_id):

    errors = shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/'+str(e_id))
    
    a=shows.objects.get(id=e_id)
    a.title=request.POST['title']
    a.network=request.POST['network']
    a.description=request.POST['description']
    a.save()
    return redirect('/shows/'+str(e_id)/'/edit')

def destroy(request,d_id):
    
    d=shows.objects.get(id=d_id)
    d.delete()
    return redirect('/shows')

