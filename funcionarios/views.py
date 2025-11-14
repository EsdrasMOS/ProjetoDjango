from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from usuarios.models import Usuario  
from .models import Funcionario 

def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'lista_funcionarios.html', {'funcionarios': funcionarios})

def detalhe_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    return render(request, 'detalhe_funcionario.html', {'funcionario': funcionario})

@login_required 
def cadastro_funcionario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.tipo_usuario = Usuario.IS_FUNCIONARIO 
            user.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('lista_funcionarios') 
    else:
        form = UserCreationForm()
    return render(request, 'funcionarios/cad_func.html', {'form': form})

@login_required 
def login_funcionario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.tipo_usuario == Usuario.IS_FUNCIONARIO:
            login(request, user)
            return redirect('lista_funcionarios')
        else:
            messages.error(request, 'Credenciais inválidas ou acesso negado.')
    return render(request, 'funcionarios/login_func.html')

@login_required
def dashboard_funcionario(request):
    if request.user.tipo_usuario != Usuario.IS_FUNCIONARIO:
        return redirect('lista_funcionarios')
    return render(request, 'funcionarios/db_func.html', {'user': request.user})