from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Belgeler(models.Model):
    DURUM = (
        ('True', 'Aktif'),
        ('False', 'Pasif'),
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images/referanslar/')
    sira_no = models.CharField(max_length=2, choices=[(str(x), str(x)) for x in range(1, 50)])
    durum = models.CharField(max_length=10, choices=DURUM)

    # Admin panel title show
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


