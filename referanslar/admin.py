from django.contrib import admin

# Register your models here.
from referanslar.models import Belgeler

class BelgelerAdmin(admin.ModelAdmin):
    list_display = ['title','sira_no', 'image_tag', 'durum']
    ordering = ['sira_no']  # ters sıralama
    readonly_fields = ('image_tag',)
    search_fields = ['title']
    list_editable = ['sira_no','durum']
admin.site.register(Belgeler, BelgelerAdmin)