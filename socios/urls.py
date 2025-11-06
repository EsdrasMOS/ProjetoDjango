from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_socios, name='lista_socios'),
    path('<int:socio_id>/', views.detalhe_socio, name='detalhe_socio'),
]