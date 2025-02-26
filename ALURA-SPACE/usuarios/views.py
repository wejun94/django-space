from django.shortcuts import render, redirect

from usuarios.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User

def login(request):
     form = LoginForms()
     return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()

     # Verifica se o formulário foi submetido  e se é válido  e se as senhas coincidem  e se o nome de usuário já não existe.
    if request.method == 'POST':
        form = CadastroForms(request.POST)


        if form.is_valid(): # Se os dados são válidos, cria um novo usuário e redireciona para a página de login.
            if form["senha_1"].value() != form["senha_2"].value():
                return redirect ('cadastro')

            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')# Se o nome de usuário já existe, redireciona para a página de cadastro.

            usuario = User.objects.create_user(# Cria um novo usuário
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()# Salva o novo usuário no banco de dados e redireciona para a página de login.
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})