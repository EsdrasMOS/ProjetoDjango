from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistroSocioForm, RegistroFuncionarioForm

def pagina_inicial(request):
    return render(request, '../template/index.html')

def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.tipo_usuario == 'socio':
                return redirect('dashboard_socio')
            else:
                return redirect('dashboard_funcionario')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registro_socio(request):
    if request.method == 'POST':
        form = RegistroSocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroSocioForm()
    return render(request, 'registro_socio.html', {'form': form})

def registro_funcionario(request):
    if request.method == 'POST':
        form = RegistroFuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroFuncionarioForm()
    return render(request, 'registro_funcionario.html', {'form': form})

@login_required
def dashboard_socio(request):
    return render(request, 'dashboard_socio.html')

@login_required
def dashboard_funcionario(request):
    return render(request, 'dashboard_funcionario.html')

def logout_view(request):
    logout(request)
    return redirect('pagina_inicial')
