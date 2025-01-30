from django.db import models
from datetime import datetime

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
    foto = models.CharField(max_length=150, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    
    
    def _str_(self):
        return f"Fotografia [nome={self.nome}]"
    