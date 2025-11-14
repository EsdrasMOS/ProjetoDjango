from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_funcionarios, name='lista_funcionarios'),
    path('<int:funcionario_id>/', views.detalhe_funcionario, name='detalhe_funcionario'),
    path('cadastro/', views.cadastro_funcionario, name='cadastro_funcionario'),
    path('login/', views.login_funcionario, name='login_funcionario'),
    path('dashboard/', views.dashboard_funcionario, name='dashboard_funcionario'),
]