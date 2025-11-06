from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_funcionarios, name='lista_funcionarios'),
    path('<int:funcionario_id>/', views.detalhe_funcionario, name='detalhe_funcionario'),
]