from django.shortcuts import render

# Create your views here.
from home.models import Setting, Slider, SosyalMedya
from urunler.models import urunler

def index(request):
    Urunler = urunler.objects.all().order_by('sira_no')[:]
    setting = Setting.objects.get(pk=1)
    slider = Slider.objects.all().order_by('sira_no')[:]
    sosyalMedya = SosyalMedya.objects.all().order_by('sira_no')[:]

    x = Setting.objects.get(pk=1)
    x.hits_count = x.hits_count + 1
    x.save()
    context = {
        'urunler': Urunler.filter(durum=True),
        'setting': setting,
        'slider': slider.filter(durum=True),
        'sosyalMedya': sosyalMedya.filter(durum=True),
        'home_page': 'active',
        'page': 'home'}
    return render(request,"index.html",context)

