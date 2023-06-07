from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Randevu

class UserAdmin(BaseUserAdmin):
    # Her kullanıcı için e-posta adresini göstermek için list_display'i özelleştirin.
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

class RandevuAdmin(admin.ModelAdmin):
    list_display = ('isim', 'email', 'tarih_saat', 'aciklama')

# Yeni UserAdmin sınıfınızla User modelini yeniden kaydedin.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Randevu modelini kaydedin
admin.site.register(Randevu, RandevuAdmin)
