from django.contrib import admin

# Register your models here.
from home.models import Setting, SosyalMedya, Slider

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'update_at','status']
admin.site.register(Setting, SettingAdmin)

class SosyalMedyaAdmin(admin.ModelAdmin):
    list_display = ['title','sira_no', 'durum']
    ordering = ['sira_no']  # ters sıralama
    list_filter = ['durum']
    list_editable = ['sira_no', 'durum']
admin.site.register(SosyalMedya, SosyalMedyaAdmin)

class SliderAdmin(admin.ModelAdmin):
    ordering = ['sira_no'] # ters sıralama
    list_display = ['title','sira_no','image_tag','durum']
    list_editable = ['sira_no','durum']
    readonly_fields = ('image_tag',)
    list_filter = ['durum']
    search_fields = ['title']
admin.site.register(Slider, SliderAdmin)