from django.db import models

from datetime import datetime

from django.contrib.auth.models import User

# classe que é igual a um model, pois ela representa uma tabela no banco de dados
class Fotografia(models.Model):
    #colunas (nome, legenda, descrição, foto)
    #Parametro max_length=100, indica o máximo de caracteres que teremos dentro de nome
    #null == false, ou seja, nao pode ser um campo vazio
    #blank==False, ou seja, não pode ser um campo blank, desta forma -> ''
    
    OPCOES_CATEGORIA = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True) #para evitar conflitos de imagens, dentro da pasta de fotos tera outra pasta com o ano, mês e dia onde sera cadastradro os items 
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(#relacionando a fotografia com o usuario
        to=User,
        on_delete=models.SET_NULL,#se o usuario for deletado, não deletamos a fotografia
        null=True,#não podemos deletar o usuario caso a fotografia exista
        blank=False,
        related_name="fotos",#esta relacionando a fotografia com o usuario
    )
    
    
    def _str_(self):
        return self.nome
    