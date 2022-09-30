from django.db import models


from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from django.core.validators import FileExtensionValidator
# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(blank=True, max_length=300) # Başlık
    keywords = models.TextField(blank=True, max_length=500) # Anahtar kelimeler
    description = models.TextField(blank=True,max_length=500) # Açıklama
    company = models.CharField(blank=True, max_length=100) # firma adı
    author = models.CharField(blank=True,max_length=30) # yazar
    url = models.CharField(blank=True,max_length=50) # yazar linkedin url
    address = models.CharField(blank=True,max_length=150) # firma adresi
    maps = models.TextField(blank=True,max_length=250) # firma konum
    phone = models.CharField(blank=True,max_length=30) # firma telefon
    fax = models.CharField(blank=True,max_length=30) # firma fax
    email = models.CharField(blank=True,max_length=50) # firma e-mail
    smtpserver = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=20)
    smtpport = models.CharField(blank=True,max_length=20)
    icon = models.ImageField(blank=True,upload_to='images/icon/') # firma tarayıcı iconu
    #logo = models.ImageField(blank=True,upload_to='images/logo/')
    # svg= yazan kısım logodur.
    svg= models.FileField(null=True, blank=True, upload_to="images/svg/", validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    hits_count = models.IntegerField(default=0) # ziyaretçi sayısı

    # Admin panel title show
    def __str__(self):
        return self.title

class SosyalMedya(models.Model):
    STATUS = (
        ('True', 'Aktif'),
        ('False', 'Pasif'),
    )
    title = models.CharField(blank=True, max_length=50)
    icon = models.CharField(blank=True, max_length=50)
    href = models.CharField(blank=True, max_length=150)
    durum = models.CharField(max_length=10, choices=STATUS)
    sira_no = models.CharField(max_length=2, choices=[(str(x), str(x)) for x in range(0, 10)])

    def __str__(self):
        return self.title

class Slider(models.Model):
    STATUS = (
        ('True', 'Aktif'),
        ('False', 'Pasif'),
    )
    title = models.CharField(blank=True, max_length=250)
    image = models.ImageField(blank=True, upload_to='images/slider/')
    sira_no = models.CharField(max_length=2, choices=[(str(x),str(x)) for x in range(0,20)])
    durum = models.CharField(max_length=10, choices=STATUS)


    # Admin panel title show
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'