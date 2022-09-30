from django.contrib import sitemaps
from django.urls import reverse

from urunler.models import urunler


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self): # tüm linkler
        return ['index','urunler', 'urun_search', 'kurumsal', 'referanslar', 'iletisim',]

    def location(self, item):
        return reverse(item)

class UrunlerViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    def items(self):
        return urunler.objects.all()



