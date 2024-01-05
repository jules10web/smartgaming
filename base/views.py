from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import Room
from .models import Screen
from .models import Users
from qrcode.models import Qrcode as qrc
from .forms import Gamer
from .forms import UserForm, SignupForm
from django.forms import ModelForm

# Create your views here.

#rooms=[
    #{'id': 1, 'name':'FIFA'},
    #{'id': 2,'name':'GTA'},
    #{'id': 3,'name':'COD'},

def home(request):
    rooms= Room.objects.all()
    context= {'rooms':rooms}
    return render(request, 'base/home.html',context)

def screen(request):
    screens=Screen.objects.all()
    context={'screens': screens}
    return render(request,'base/screen.html', context)


def room(request,pk):
    
    room=Room.objects.all()
    context={'room':room}
    
    return render(request, 'base/room.html',context)


def gamer_form(request):
    screens = Screen.objects.all()
    
            

    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = Gamer(request.POST)
        # check whether it's valid:
        if form.is_valid():
            qrc=qrc.objects.all()
    else:
            form=Gamer()

  
    return render(request,'base/gamer_form.html',{'form':form})

def login(request):
    log=UserForm()
    context={'log':log}
    if request.method=="POST":
        log=UserForm(request.POST)
        
        

    return render(request,'base/login.html',context)

def sign(request):
    sign=SignupForm()
    context={'sign': sign}
    if request.method=="POST":
        sign=SignupForm(request.POST)
        name=request.POST["name"]
        email=request.POST["email"]
        econtact=request.POST["econtact"]
        password=request.POST["password"]
        password_retype=request.POST["password_retype"]
        new_user=Users(name=name,email=email,econtact=econtact,password=password)
        new_user.save()
    return render(request,'base/signup.html',context)
