from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_socios, name='lista_socios'),
    path('<int:socio_id>/', views.detalhe_socio, name='detalhe_socio'),
    path('cadastro/', views.cadastro_socio, name='cadastro_socio'),
    path('login/', views.login_socio, name='login_socio'),
    path('dashboard/', views.dashboard_socio, name='dashboard_socio'),
]