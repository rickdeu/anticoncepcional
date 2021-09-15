from django.conf.urls import include, url
from django.urls import path
from core import views


app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('seconde_home/', views.second_home, name='seconde_home'),
    path('choose/', views.choose, name='choose'),
    path('second_choose/', views.second_choose, name='second_choose'), 
    path('resultado_teste', views.resultado_teste, name='resultado_teste'), 
    path('detalhes_resultado_teste/<int:pk>forca_suprema_pra_sempre_meus_pensadelos', views.detalhes_resultado_teste, name='detalhes_resultado_teste'), 


]
