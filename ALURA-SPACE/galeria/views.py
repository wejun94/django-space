from django.shortcuts import render, get_object_or_404, redirect

from galeria.models import Fotografia

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