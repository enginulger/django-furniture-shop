from django.db import models

# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe


class Hakkimizda(models.Model):
    KONUM = (
        ('left', 'Sol'),
        ('right', 'Sağ'),
    )
    DURUM = (
        ('True', 'Aktif'),
        ('False', 'Pasif'),
    )
    title = models.CharField(blank=True,max_length=200)
    company = models.CharField(blank=True, max_length=200)
    icerik= RichTextUploadingField(blank=True)
    konum = models.CharField(max_length=10, choices=KONUM)
    image = models.ImageField(blank=True, upload_to='images/hakkimizda/')
    sira_no = models.CharField(max_length=2, choices=[(str(x), str(x)) for x in range(0, 10)])
    durum = models.CharField(max_length=10, choices=DURUM)

    # Admin panel title show
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
