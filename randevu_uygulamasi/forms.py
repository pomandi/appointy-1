from django import forms
from .models import Randevu

class RandevuForm(forms.ModelForm):
    isim = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'})
    )
    telefon = forms.CharField(   # Telefon numarası alanını formunuza ekledik
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'})
    )
    tarih_saat = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'], 
        widget=forms.DateTimeInput(attrs={'class': 'form-control form-control-lg datetimepicker', 'type': 'datetime-local'})
    )
    aciklama = forms.CharField(
    widget=forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': 3, 'placeholder': 'Kaç kişi için randevu alıyorsunuz?'})
    )
    




    class Meta:
        model = Randevu
        fields = ['isim', 'email', 'telefon', 'tarih_saat', 'aciklama']  # 'telefon' alanını ekledik
