
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    
    #páginas de álbum p/ cada sessão
    path('cozinha',views.cozinha, name='cozinha'),
    path('sala',views.sala, name='sala'),
    path('quartos',views.quartos, name='quartos'),
    path('lazer',views.lazer, name='lazer'),
    
    #urubici & duvidas frequentes
    path('urubici',views.urubici, name='urubici'),
    path('duvidas',views.duvidas, name='duvidas'),
    
    
]
