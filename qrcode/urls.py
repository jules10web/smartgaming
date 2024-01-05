from django.urls import path
from . import views

urlpatterns=[

    path('qrc/',views.qrc, name='qrc'),
]
