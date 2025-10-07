from django.urls import path
from . import views

urlpattern = [
    path('home/',views.home,name='home')
]