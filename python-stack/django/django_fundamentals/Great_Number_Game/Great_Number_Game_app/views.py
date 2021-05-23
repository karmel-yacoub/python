from django.shortcuts import render,HttpResponse,redirect
import random 	


def index(request):
    if 'name' not in request.session:
        request.session['name']=random.randint(1,100)
        print(request.session['name'])
    return render(request,'index.html')
   
def user(request):
    guss=request.POST['guess']
    if int(guss)==request.session['name']:
        request.session['result']="correct"
    elif int(guss)>request.session['name']:
        request.session['result']="High"
    else:
        request.session['result']="low"

    return redirect('/')



    
# Create your views here.
