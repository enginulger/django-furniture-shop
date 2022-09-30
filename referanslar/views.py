from django.shortcuts import render

# Create your views here.
from referanslar.models import Belgeler
from home.models import SosyalMedya, Setting


def referanslar(request):
    sosyalMedya = SosyalMedya.objects.all().order_by('sira_no')[:]
    setting = Setting.objects.get(pk=1)
    belgeler = Belgeler.objects.all().order_by('sira_no')[:]
    context = {'setting':setting,
               'sosyalMedya': sosyalMedya.filter(durum=True),
               'belgeler': belgeler.filter(durum=True),
               'belgeler_page': 'active'}
    return render(request,'referanslar.html',context)

