from django.urls import path

from . import views

mapping=[
    path('',views.home,name='home')
]