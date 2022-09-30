from django.contrib import admin

# Register your models here.
from kurumsal.models import Hakkimizda


class HakkimizdaAdmin(admin.ModelAdmin):
    list_display = ['title','sira_no', 'image_tag', 'konum', 'durum']
    ordering = ['sira_no']  # ters sıralama
    readonly_fields = ('image_tag',)
    list_editable = ['sira_no','konum','durum']
    list_filter = ['durum']
admin.site.register(Hakkimizda, HakkimizdaAdmin)