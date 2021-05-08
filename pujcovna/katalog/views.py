from django.shortcuts import render

from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from . import models
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


class IndexView (View):
    def get(self, request):
        return HttpResponse("""<h1>Vítejte v naší autopůjčovně!</h1>
<a href='http://localhost:8000/katalog/seznam/'>Jaká auta půjčujeme?</a><br>
<a href='http://localhost:8000/katalog/1'>Jaká auta jsou momentálně vypůjčená?</a><br>
<h2>O naší autopůjčovně</h2>
<p>Naše půjčovna vznikla v roce 2011 a dnes nabízí přibližně 30 aut.</p>
"""
)


class SeznamAutView(ListView):
  model = models.Auto
  template_name = "auta_list.html"


class VypujckaView(ListView):
    model = models.Vypujcka
    template_name = "vypujcky_list.html"


class ZakaznikView(ListView):
    model = models.Zakaznik
    template_name = "zakaznici_list.html"


class VypujckaDetailView(DetailView):
    model = models.Vypujcka
    template_name = "vypujcka_detail.html"


class ZakaznikDetailView(DetailView):
    model = models.Zakaznik
    template_name = "zakaznik_detail.html"


class VlozAuto(CreateView):
    model = models.FormularAuto
    template_name = "formular_auto.html"
    fields = ["registracni_znacka", "znacka_auta", "typ_auta", "najeto_v_km", "datum_STK", "auto"]
    success_url = reverse_lazy("potvrzeni_formulare")


class PotvrzeniFormulare(TemplateView):
    template_name = "potvrzeni_formulare.html"


class ObjednejAuto(CreateView):
    model = models.FormularVypujcka
    template_name = "formular_vypujcka.html"
    fields = ["jmeno", "prijmeni", "cislo_rp", "datum_narozeni", "zahajeni_vypujcky", "konec_vypujcky", "auto"]
    success_url = reverse_lazy("potvrzeni_formulare")








