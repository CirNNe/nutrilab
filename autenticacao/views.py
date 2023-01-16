"""
TODO:
    Validar se o username, email e senha não foram enviados em branco;
    Validar se já existe usuário com username cadastrado;
    Salvar os dados do cadastro no BD;
"""

from django.shortcuts import render, redirect
import re
from django.contrib import messages
from django.contrib.messages import constants

def password_is_valid(request, password, confirm_password):
    """Valida a senha para cadastro"""
    if len(password) < 6:
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter 6 ou mais caracteres!')
        return False
    if not password == confirm_password:
        messages.add_message(request, constants.ERROR, 'As senhas não coincidem!')
        return False
    if not re.search('[A-Z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter ao menos uma letra maiúscula!')
        return False
    if not re.search('[a-z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter ao menos uma letra minúscula!')
        return False
    if not re.search('[1-9]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter números!')
        return False
    return True

def cadastro(request):
    """Recebe os dados do formulário de cadastro"""
    if request.method == "GET":
        return render(request, 'cadastro/cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('autenticacao/cadastro')
        return render(request, 'cadastro/cadastro.html')

def login(request):
    pass
