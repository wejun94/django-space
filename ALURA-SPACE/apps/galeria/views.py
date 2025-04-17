from django.shortcuts import render, get_object_or_404, redirect

from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para ver a galeria"  )
        return redirect('login')
    
    #fotografias = Fotografia.objects.all() puxando todos os objetos do banco de dados, do modo fotopgrafia
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    #puxando somente as fotografias que estao como pulicadas
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para ver a galeria"  )
        return redirect('login')
     
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
            
    return render (request, "galeria/buscar.html", {"cards": fotografias})

def nova_imagem(request):
    #somente as pessoas com credencias terão acesso
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para ver a galeria"  )
        return redirect('login')
    
    #o usuario deve preencher o formulario, as informações serão salvas no banco de dados. se a requisição for igual a POST, sera instanciado um novo formulario e vamos passar as informações para dentro deste novo formulario.
    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid(): #se o formulário for válido, ele será salvo. 
            form.save()
            messages.success(request, 'Nova fotografia cadastrada')
            return  redirect('index')
    
    #para passar o formulario para a pagina de html nova imagem, devemos fazer a chamada aqui do formulario e depois chama-lo dentro do return entre os parenteses.
    return render(request, 'galeria/nova_imagem.html', {'form':form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)
    
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid(): #se o formulário for válido, ele será salvo. 
            form.save()
            messages.success(request, 'Fotografia editada com sucesso')
            return  redirect('index')
    
    return render(request, 'galeria/editar_imagem.html', {'form':form, 'foto_id':foto_id})

def deletar_imagem(request):
    pass
