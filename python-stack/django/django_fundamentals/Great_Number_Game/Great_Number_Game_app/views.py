from django.shortcuts import render
import random 	


def index(request):
    request.session['random']=random.randint(1, 100)
    return render(request,'index.html')


# Create your views here.
