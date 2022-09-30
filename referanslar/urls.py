from django.urls import path
from . import views

urlpatterns = [path('referanslar/', views.referanslar, name='referanslar'),]
