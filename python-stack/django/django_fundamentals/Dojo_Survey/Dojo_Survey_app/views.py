from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def result(request):
    name = request.POST['name']
    location=request.POST['location']
    favLanguage=request.POST['favLanguage']
    comment=request.POST['comment']
    context={
        "name":name,
        "location":location,
        "favLanguage":favLanguage,
        "comment":comment,
    }
    return render(request,'cntext.html',context)

# Create your views here.
