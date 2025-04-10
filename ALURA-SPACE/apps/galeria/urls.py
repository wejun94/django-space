from django.urls import path
from apps.galeria.views import index, imagem, buscar

urlpatterns = [
    path('', index, name="index"),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("buscar", buscar, name="buscar"),#nome do path | aponta para a rota no views | name buscar
    
]