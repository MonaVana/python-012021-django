from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('seznam/', views.SeznamAutView.as_view(), name='auta_list'),
    path('<int:pk>', views.VypujckaView.as_view(), name='vypujcky_list'),
    path('<int:pk>/', views.ZakaznikView.as_view(), name='zakaznik_list'),
    path('<int:pk>/detail/', views.VypujckaDetailView.as_view(), name='vypujcka_detail'),
    path('<int:pk>/detail/', views.ZakaznikDetailView.as_view(), name='zakaznik_detail'),
    path('formular/', views.VlozAuto.as_view(), name='formular_auto'),
    path('formular/potvrzeni/', views.PotvrzeniFormulare.as_view(), name='potvrzeni_formulare'),
    path('objednavka', views.ObjednejAuto.as_view(), name= 'formular_vypujcka'),
    path('objednavka/potvrzeni/', views.PotvrzeniFormulare.as_view(), name='potvrzeni_formulare'),
]
