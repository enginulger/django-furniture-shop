from django.shortcuts import render

from home.models import Setting, SosyalMedya
from kurumsal.models import Hakkimizda
# Create your views here.
def kurumsal(request):
    sosyalMedya = SosyalMedya.objects.all().order_by('sira_no')[:]
    setting = Setting.objects.get(pk=1)
    hakkimizda = Hakkimizda.objects.all().order_by('sira_no')[:]
    context = {'setting': setting,
               'sosyalMedya': sosyalMedya.filter(durum=True),
               'hakkimizda': hakkimizda.filter(durum=True),
               'kurumsal_page': 'active'}
    return render(request, "kurumsal.html", context)
