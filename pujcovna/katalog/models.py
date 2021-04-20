from django.db import models

class Auto(models.Model):
  registracni_znacka = models.CharField(max_length=100)
  znacka_auta = models.CharField(max_length=100)
  typ_auta = models.CharField(max_length=100)
  najeto_v_km = models.IntegerField()
  datum_STK = models.DateField()

class Vypujcka(models.Model):
  zahajeni_vypujcky = models.DateTimeField()
  konec_vypujcky = models.DateTimeField()
  cena = models.IntegerField()
