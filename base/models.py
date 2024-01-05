from django.db import models
from django.core.files import File
from PIL  import Image
from django.forms import ModelForm

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254,blank= True)
    econtact=models.CharField(max_length=15,blank= True)
    password=models.CharField(max_length=8)
    password_retype=models.CharField(max_length=8)

    def __str__(self):
        return self.name


class Room(models.Model):
    name= models.CharField(max_length=200)
    description=models.TextField(null=True,blank=False)
    image=models.ImageField(upload_to='images')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
    

    
class Screen(models.Model):
    name=models.CharField(max_length=200)
    active=models.BooleanField(default='false')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
    
    



    