from django.db import models

# Create your models here.
class Room(models.Model):
    name= models.CharField(max_length=200)
    description=models.TextField(null=True,blank=False)
    image_url=models.CharField(max_length=2083)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
    
class Screen(models.Model):
    name=models.CharField(max_length=200)
    status=models.BooleanField('Active',False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name