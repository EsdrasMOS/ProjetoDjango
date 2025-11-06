from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario
from socios.models import Socio
from funcionarios.models import Funcionario

class RegistroSocioForm(UserCreationForm):
    cpf = forms.CharField(max_length=14, required=True, help_text='Digite seu CPF')

    class Meta:
        model = Usuario
        fields = ('username', 'cpf', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.tipo_usuario = Usuario.IS_SOCIO
        if commit:
            user.save()
            Socio.objects.create(usuario=user, cpf=self.cleaned_data['cpf'])
        return user

class RegistroFuncionarioForm(UserCreationForm):
    nome = forms.CharField(max_length=100, required=True, help_text='Nome completo')

    class Meta:
        model = Usuario
        fields = ('username', 'nome', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.tipo_usuario = Usuario.IS_FUNCIONARIO
        if commit:
            user.save()
            Funcionario.objects.create(usuario=user)
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='ID de Entrada', max_length=254)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)