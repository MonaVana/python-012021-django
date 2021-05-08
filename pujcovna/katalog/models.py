from django.db import models


class Auto(models.Model):
  registracni_znacka = models.CharField(max_length=100)
  znacka_auta = models.CharField(max_length=100)
  typ_auta = models.CharField(max_length=100)
  najeto_v_km = models.IntegerField()
  datum_STK = models.DateField()

  def __str__(self):
    return self.znacka_auta + " " + self.typ_auta


class Zakaznik(models.Model):
  jmeno = models.CharField(max_length=100)
  prijmeni = models.CharField(max_length=100)
  cislo_rp = models.CharField(max_length=100)
  datum_narozeni= models.DateField()

  def __str__(self):
    return self.prijmeni + " " + self.jmeno


class Vypujcka(models.Model):
  zahajeni_vypujcky = models.DateTimeField()
  konec_vypujcky = models.DateTimeField()
  cena = models.IntegerField()
  auto = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True)
  zakaznik = models.ForeignKey(Zakaznik, on_delete=models.SET_NULL, null=True)


class FormularAuto(models.Model):
  registracni_znacka = models.CharField(max_length=100)
  znacka_auta = models.CharField(max_length=100)
  typ_auta = models.CharField(max_length=100)
  najeto_v_km = models.IntegerField()
  datum_STK = models.DateField()


class FormularVypujcka(models.Model):
  jmeno = models.CharField(max_length=100)
  prijmeni = models.CharField(max_length=100)
  cislo_rp = models.CharField(max_length=100)
  datum_narozeni = models.DateField()
  zahajeni_vypujcky = models.DateTimeField()
  konec_vypujcky = models.DateTimeField()
  auto = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True)