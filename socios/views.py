from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from usuarios.models import Usuario
from .models import Socio  # Importe Socio (não Funcionario)

# Views para Socios
def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, 'socios/lista_socios.html', {'socios': socios})

def detalhe_socio(request, socio_id):
    socio = get_object_or_404(Socio, id=socio_id)
    return render(request, 'socios/detalhe_socio.html', {'socio': socio})

def cadastro_socio(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.tipo_usuario = Usuario.IS_SOCIO  # Define como socio
            user.save()
            # Cria o Socio ligado ao Usuario, com campos extras
            Socio.objects.create(
                usuario=user,
                nome=request.POST.get('nome'),
                cpf=request.POST.get('cpf'),
                telefone=request.POST.get('telefone'),
                email=request.POST.get('email'),
                data_nascimento=request.POST.get('data_nascimento') or None  # Campo opcional
            )
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('lista_socios')  # Redireciona para lista de socios
    else:
        form = UserCreationForm()
    return render(request, 'socios/cad_soc.html', {'form': form})

@login_required
def login_socio(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.tipo_usuario == Usuario.IS_SOCIO:
            login(request, user)
            return redirect('lista_socios')
        else:
            messages.error(request, 'Credenciais inválidas ou acesso negado.')
    return render(request, 'socios/login_soc.html')

@login_required
def dashboard_socio(request):
    if request.user.tipo_usuario != Usuario.IS_SOCIO:
        return redirect('lista_socios')
    return render(request, 'socios/db_soc.html', {'user': request.user})