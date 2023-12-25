from django.shortcuts import render
from .models import Room
from .models import Screen

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


def form(request):
    screens = Screen.objects.all()

    if screens.isselected:
        active= True
   
    return render(request,'base/form.html',{'screens': screens})

