from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe


class urunler(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    kategori = models.CharField(blank=True, max_length=15)
    title = models.CharField(blank=True, max_length=150)
    sira_no = models.CharField(max_length=3, choices=[(str(x), str(x)) for x in range(1, 100)])
    image = models.ImageField(blank=True, upload_to='images/urunler/')
    durum = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=True, unique=True, blank=True, default=None, max_length=180)

    icerik = RichTextUploadingField(blank=True)
    aciklama = RichTextUploadingField(blank=True)
    kullanim_alani = RichTextUploadingField(blank=True) # kullanım alanı
    ozellikler = RichTextUploadingField(blank=True)
    degerler = RichTextUploadingField(blank=True)

    head_keywords = models.TextField(blank=True, max_length=500)
    head_description = models.TextField(blank=True, max_length=500)

    def get_absolute_url(self):
        return reverse('urunler', kwargs={'id': self.id, 'slug': self.slug})

    # Admin panel title show
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

