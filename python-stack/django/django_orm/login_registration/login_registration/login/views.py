from django.shortcuts import redirect, render
import re
from . models import*
from django.contrib import messages
import bcrypt


def index(request):
    return render(request,"index.html")

def registration(request):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    errors={}
    if len(request.POST['fname'])<2:
        errors["first_name"]="first name is too short"  #errors[dict key]

    if len(request.POST['lname'])<2:
        errors["last_name"]="last name is too short"
        
    if not EMAIL_REGEX.match(request.POST['email']):
        errors['email']="Ivalid email address!"

    if len(request.POST["password"]) <8:
        errors['password']="short password"

    if request.POST["password"]!=request.POST["confirm"]:
        errors["confirm"]="Not matching"
    for key,value in errors.items():  #key and value here just a name we can cgange and errors.item this will connect us to dict
        if len(errors)>0:
            messages.error(request,value)  #messages.error it's a built in     
    else:
        first=request.POST['fname']
        last=request.POST['lname']
        em=request.POST['email']
        pas=request.POST['password']
        conf=request.POST['confirm']
        if pas==conf: #to make shure again of confirmation
            hash = bcrypt.hashpw(pas.encode(), bcrypt.gensalt()).decode()
            user=Users.objects.create(first_name=first,last_name=last,email=em,password=hash)
            if 'name' not in request.session: #we creat a session by checking if there a key called ['name'] in this session 
                request.session['name']=first
            return redirect("/sucsess")
        return redirect("/") # if the pass dosen't equal to conf this will run

def sucsess(request):
    return render(request,'welcom.html')

def logout(request):
    del request.session['name']
    return redirect("/")

def login(request):
    user=Users.objects.filter(email=request.POST['lemail'])  #use filter here to return list of object
    if user: #this mean if len (user)>0
        if bcrypt.checkpw(request.POST['lpassword'].encode(), user[0].password.encode()):
            if 'name' not in request.session: #we creat a session by checking if there a key called ['name'] in this session 
                request.session['name']=user[0].first_name
            return redirect("/sucsess")
        return redirect('/') 
    return redirect('/') 
    



    

    
    

              
    

    
    
    