from django.contrib import admin

# Register your models here.
from urunler.models import urunler


class UrunlerAdmin(admin.ModelAdmin):
    list_display = ['kategori','title','sira_no','image_tag','durum']
    readonly_fields = ('image_tag',)
    ordering = ['sira_no']  # ters sıralama
    list_filter = ['kategori','durum']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['title', 'sira_no', 'durum']

admin.site.register(urunler, UrunlerAdmin)