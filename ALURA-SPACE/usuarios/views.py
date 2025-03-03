from django.shortcuts import render, redirect

from usuarios.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User

from django.contrib import auth # Necessário para usar o método authenticate()

from django.contrib import messages

def login(request):
     form = LoginForms()
     
     if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():# Se os dados são válidos, tenta autenticar o usuário.
            nome = form['nome_login'].value()
            senha = form['senha'].value()
             
        usuario = auth.authenticate(#
            request,
            username=nome, 
            password=senha
        )
        # Se o nome de usuário e a senha estão corretos, autentica o usuário e redireciona para a página de index.
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"{nome}Usuário logado com sucesso!")
            return redirect('index')
        else:
            messages.error(request, "Erro ao efectuar o login!")
            return redirect('login')
     
     return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()

     # Verifica se o formulário foi submetido  e se é válido  e se as senhas coincidem  e se o nome de usuário já não existe.
    if request.method == 'POST':
        form = CadastroForms(request.POST)


        if form.is_valid(): # Se os dados são válidos, cria um novo usuário e redireciona para a página de login.
            

            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Nome de usuário já existe")
                return redirect('cadastro')# Se o nome de usuário já existe, redireciona para a página de cadastro.

            usuario = User.objects.create_user(# Cria um novo usuário
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()# Salva o novo usuário no banco de dados e redireciona para a página de login.
            messages.sucess(request, f"{nome} Usuário criado com sucesso")
            return redirect('login')
    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Usuário deslogado com Sucesso")
    return redirect('login')