from django.contrib import admin

# Register your models here.
from .models import Room
from .models import Screen
from .models import Users

admin.site.register(Room)
admin.site.register(Screen)
admin.site.register(Users)