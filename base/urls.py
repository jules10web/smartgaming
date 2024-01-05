from django.urls import path
from . import views


urlpatterns=[

        path('', views.home, name= 'home'),
        path('room/<str:pk>/',views.room, name= 'room'),
        path('screen/',views.screen, name='screen'),
        path('gamer_form/',views.gamer_form, name='gamer_form'),
        path('login/',views.login, name='login'),
        path('sign/',views.sign, name='sign'),
]

