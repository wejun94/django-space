from django import forms

from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        #esta classe se refere ao model fotografia
        model = Fotografia
        exclude = ['publicada',] #lista dos que eu nao quero que apareça
        labels = {
            'descricao':'Descrição',
            'data_fotografia':'Data de Registo',
            'usuario':'Usuário',
        }
        
        widgets = {
            #adicionando atributos (attrs)
            'nome': forms.TextInput(attrs={'class':'forms-control'}), 
            'legenda': forms.TextInput(attrs={'class':'forms-control'}),
            'categoria': forms.Select(attrs={'class':'forms-control'}),
            'descrição': forms.Textarea(attrs={'class':'forms-control'}),
            'foto': forms.FileInput(attrs={'class':'forms-control'}),
            'data_fotografia': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'forms-control'
                    }
                ),
            'usuario': forms.Select(attrs={'class':'forms-control'}),
               
        }
        
        