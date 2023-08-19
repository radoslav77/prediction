from django import views
from django.urls import path, include
from . import views

# input views 
urlpatterns = [
    path('', views.index, name='index'),
    path('months/<str:month>', views.months, name='months'),
    path('month', views.pyMonth, name='pyMonth'),

    #API
    path('jsMonth', views.month, name='month'),

]
