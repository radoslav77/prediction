from django import views
from django.urls import path, include
from . import views

# input views 
urlpatterns = [
    path('', views.index, name='index'),
    path('month/<str:month>', views.months, name='months'),

]
