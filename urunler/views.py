from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import SosyalMedya, Setting
from urunler.models import urunler

from urunler.form import SearchForm
import json

def Urunler(request, id, slug):
    sosyalMedya = SosyalMedya.objects.all().order_by('sira_no')[:]
    setting = Setting.objects.get(pk=1)
    metal = urunler.objects.all().order_by('sira_no')[:]
    kimyasal = urunler.objects.all().order_by('sira_no')[:]
    Urun = urunler.objects.get(pk=id)
    context = {'setting':setting,
               'sosyalMedya': sosyalMedya.filter(durum=True),
               'metal': metal.filter(durum=True),
               'kimyasal': kimyasal.filter(durum=True),
               'urun':Urun,
               'slug':slug,
               'urunler_page':'active'}
    return render(request,'urundetay.html',context)


def Metal(request):
    sosyalMedya = SosyalMedya.objects.all().order_by('sira_no')[:]
    setting = Setting.objects.get(pk=1)
    metal = urunler.objects.all().order_by('sira_no')[:]
    context = {'metal': metal.filter(durum=True),
               'setting':setting,
               'sosyalMedya': sosyalMedya.filter(durum=True),
               'urunler_page':'active'}
    return render(request,'urunler.html',context)





def urun_search(request):
    sosyalMedya = SosyalMedya.objects.all().order_by('sira_no')[:]
    setting = Setting.objects.get(pk=1)
    metal = urunler.objects.all().order_by('sira_no')[:]
    kimyasal = urunler.objects.all().order_by('sira_no')[:]
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            Urun_search = urunler.objects.filter(title__icontains=query, durum=True)
            context = {
                'setting': setting,
                'sosyalMedya': sosyalMedya.filter(durum=True),
                'metal': metal.filter(durum=True),
                'kimyasal': kimyasal.filter(durum=True),
                'urunler_page': 'active',
                'urun': Urun_search}
            return render(request, 'urun_search.html', context)
    return HttpResponseRedirect('/')

def urun_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term','')
        urun = urunler.objects.filter(title__icontains=q)
        results = []
        for rs in urun:
            belge_json={}
            belge_json = rs.title
            results.append(belge_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)