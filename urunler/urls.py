from django.urls import path
from . import views

urlpatterns = [
    path('urunler/', views.Metal, name='metal'),

    path('urunler/<int:id>/<slug:slug>', views.Urunler, name='urunler'),
    path('urun/search/', views.urun_search, name='urun_search'),
    path('search_auto/', views.urun_search_auto, name='urun_search_auto'),
]

