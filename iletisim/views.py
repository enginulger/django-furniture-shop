from django.shortcuts import render

# Create your views here.


from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponseRedirect
from iletisim.forms import iletisimForm
from home.models import Setting, SosyalMedya

def iletisim(request):
    sosyalMedya = SosyalMedya.objects.all().order_by('sira_no')[:]
    setting = Setting.objects.get(pk=1)
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        mesaj ="Mesaj: " + message + '\n\n' + "E-mail: " + email + '\n' + "Phone: " + phone + '\n' + "Ad Soyad: " + subject
        send_mail(subject, mesaj, settings.EMAIL_HOST_USER, ['obcmobilya@gmail.com'], fail_silently=False)
        messages.success(request, "Mesajınız alındı. En kısa sürede geri dönüş yapılacaktır. Teşekkür ederiz.")
        #return redirect('iletisim')
        return HttpResponseRedirect('/iletisim')
    context = {'setting': setting,
               'sosyalMedya': sosyalMedya.filter(durum=True),
               'iletisim_page': 'active'}

    return render(request, 'iletisim.html', context)