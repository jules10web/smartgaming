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
    return render(request, 'base/home.html', {'rooms':rooms})

def room(request,pk):
    
    room=Room.objects.get(id=pk)
    context={'room':room}
    
    return render(request, 'base/room.html',context)

def screen(request,pk):
    context:{'Screens': screen}
    screen=Screen.objects.get(Screen.status)
    return render(request,'base/screen.html')

def form(request):
    context:{'Screens': screen}
    
    return render(request,'base/form.html',{'form':form})

