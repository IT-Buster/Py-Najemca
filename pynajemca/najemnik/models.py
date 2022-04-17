from email.policy import default
from sqlite3 import Row
from django.db import models

class Lokator(models.Model):
    nazwisko = models.CharField(max_length=30)
    imie = models.CharField(max_length=30)
    pesel = models.CharField(max_length=11)
    email = models.EmailField()

    class Meta:
        ordering = ('nazwisko',)
        verbose_name_plural = 'Lokatorzy'
    def __str__(self):
        return self.nazwisko

    
class Lokal(models.Model):
    numer_lokalu = models.IntegerField()
    powierzchnia = models.DecimalField(max_digits=4,decimal_places=2)
    opis_lokalu = models.TextField()
    
    class Meta:
        ordering = ('numer_lokalu',)
        verbose_name_plural = 'Lokale'
    def __str__(self):
        return str(self.numer_lokalu)

class Umowa(models.Model):
    nr_umowy = models.CharField(max_length=15)
    data_zawarcia = models.DateTimeField(auto_now=True)
    lokator = models.ForeignKey(Lokator, on_delete=models.CASCADE)
    lokal = models.ForeignKey(Lokal, on_delete=models.CASCADE)
    czynsz = models.DecimalField(max_digits=10,decimal_places=2)
    ilosc_osob = models.IntegerField()

    class Meta:
        ordering = ('-nr_umowy',)
        verbose_name_plural = 'Umowy'
    def __str__(self):
        return self.nr_umowy       

MEDIA_TYP = (
    (1, 'Woda'),
    (2, 'Ciepło'),
    (3, 'Odpady'),
)

class LicznikStan(models.Model):
    lokal = models.ForeignKey(Lokal, on_delete=models.CASCADE)
    typ_licznika = models.IntegerField(choices=MEDIA_TYP,default=1)
    nr_licznika = models.CharField(max_length=20, default='000000')
    stan_licznika = models.DecimalField(max_digits=10,decimal_places=2)
    data_odczytu = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-data_odczytu',)
        verbose_name_plural = 'Stany Liczników'
    def __str__(self):
        return str(self.data_odczytu)

class MediaRozliczenia(models.Model):
    numer_fv = models.CharField(max_length=5)
    media_typ = models.IntegerField(choices=MEDIA_TYP,default=1)
    zuzycie = models.DecimalField(max_digits=10,decimal_places=2)
    data_wyst = models.DateTimeField(auto_now=True)
    do_zaplaty = models.DecimalField(max_digits=10,decimal_places=2)
    cena_jedn_np_fv = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        ordering = ('-data_wyst',)
        verbose_name_plural = 'Rozliczenia z Dostawcami'
    def __str__(self):
        return self.numer_fv
    
    @property
    def cena_jednostkowa(self):
        return str( round(self.do_zaplaty/self.zuzycie ,2) )

class Naliczenia(models.Model):
    nr_umowy = models.ForeignKey(Umowa, on_delete=models.CASCADE)
    data_naliczenia = models.DateTimeField()
    czynsz = models.DecimalField(max_digits=10,decimal_places=2)
    cieplo_koszt = models.DecimalField(max_digits=10,decimal_places=2)
    cieplo_zuzycie = models.DecimalField(max_digits=10,decimal_places=2)
    woda_koszt = models.DecimalField(max_digits=10,decimal_places=2)
    woda_zuzycie = models.DecimalField(max_digits=10,decimal_places=2)
    odpady = models.DecimalField(max_digits=10,decimal_places=2)
    ilosc_osob = models.IntegerField()
    naleznosc = models.DecimalField(max_digits=10,decimal_places=2)
    saldo_stan = models.DecimalField(max_digits=10,decimal_places=2)
    kwota_wplywu_nalez = models.DecimalField(max_digits=10,decimal_places=2)
    data_wplywu_nalez = models.DateTimeField()
    data_wpisu = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-data_wpisu',)
        verbose_name_plural = 'Naliczenia'
    def __str__(self):
        return self.data_wpisu










