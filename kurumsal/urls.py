from django.urls import path
from . import views

urlpatterns = [path('kurumsal/', views.kurumsal, name='kurumsal'),]
