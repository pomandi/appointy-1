from django.db import models

class Randevu(models.Model):
    isim = models.CharField(max_length=50,null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    telefon = models.CharField(max_length=20, null=False, blank=False)
    tarih_saat = models.DateTimeField(null=True)
    aciklama = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.isim
