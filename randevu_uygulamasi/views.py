

from django.shortcuts import render, redirect
from .models import Randevu
from .forms import RandevuForm

def randevu_listesi(request):
    randevular = Randevu.objects.all().order_by('tarih_saat')

    return render(request, 'randevu_uygulamasi/randevu_listesi.html', {'randevular': randevular})

def randevu_olustur(request):
    if request.method == "POST":
        form = RandevuForm(request.POST)
        if form.is_valid():
            randevu = form.save()  # formu kaydedip dönen randevu nesnesini alıyoruz
            return redirect('randevu_detay', randevu_id=randevu.id)  # bu nesnenin id'siyle randevu_detay görünümüne yönlendiriyoruz
        else:
            print(form.errors)
    else:
        form = RandevuForm()
    return render(request, 'randevu_uygulamasi/randevu_olustur.html', {'form': form})

def randevu_detay(request, randevu_id):
    randevu = Randevu.objects.get(id=randevu_id)
    return render(request, 'randevu_uygulamasi/randevu_detay.html', {'randevu': randevu})


# views.py

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_appointment_confirmation_email(customer_email, customer_name, appointment_date):
    subject = 'Randevu Onayı'
    template = 'appointment_confirmation.html'
    context = {
        'customer_name': customer_name,
        'appointment_date': appointment_date
    }
    message = render_to_string(template, context)

    send_mail(
        subject,
        '',
        settings.DEFAULT_FROM_EMAIL,
        [customer_email],
        html_message=message
    )

