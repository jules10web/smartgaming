from django.urls import path
from . import views


urlpatterns=[

        path('', views.home, name= 'home'),
        path('room/<str:pk>/',views.room, name= 'room'),
        path('screen/<str:pk>/',views.screen, name='screen'),
        path('form/',views.form, name='form'),
]

