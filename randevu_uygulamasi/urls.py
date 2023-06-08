# randevu_uygulamasi/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.randevu_listesi, name='randevu_listesi'),
    path('olustur/', views.randevu_olustur, name='randevu_olustur'),
    path('randevu_detay/<int:randevu_id>/', views.randevu_detay, name='randevu_detay'),
     path('blocked_dates/', views.blocked_dates, name='blocked_dates'),
]

