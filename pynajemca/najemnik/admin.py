from django.contrib import admin
from najemnik.models import *


@admin.register(Lokal)
class LokalAdmin(admin.ModelAdmin):
    list_display = ['numer_lokalu','powierzchnia','opis_lokalu']


admin.site.register(Umowa)

@admin.register(LicznikStan)
class LicznikAdmin(admin.ModelAdmin):
    list_display = (
        'lokal',
        'typ_licznika',
        'nr_licznika',
        'stan_licznika',
        'data_odczytu',
    )

admin.site.register(Naliczenia)

@admin.register(MediaRozliczenia)
class MediaRozliczAdmin(admin.ModelAdmin):
    list_display = (
        'numer_fv',
        'media_typ',
        'zuzycie',
        'data_wyst',
        'do_zaplaty',
        'cena_jedn_np_fv',
        'cena_jednostkowa',
    )

@admin.register(Lokator)
class LokatorAdmin(admin.ModelAdmin):
    list_display = (
        'nazwisko',
        'imie',
        'pesel',
        'email',
    ) 


