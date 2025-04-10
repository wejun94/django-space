from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )
    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )
    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com',
            }
        )
    )
    senha_1=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )
    senha_2=forms.CharField(
        label='Confirme a sua senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha novamente',
            }
        ),
    )
    
    def clean_nome_cadastro(self):#Após clean, adiciona o nome que quer validar, nesse caso nome_cadastro
        nome = self.cleaned_data.get('nome_cadastro')
        
        if nome:
            nome = nome.strip()#Método strip Remove espaços em branco no início e fim do nome
            if " " in nome: #Verifica se o nome contém espaço
                raise forms.ValidationError("Nome não pode conter espaço")
            else:
                return nome
            
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")#Pega a senha digitada pelo usuário no primeiro campo de senha
        senha_2 = self.cleaned_data.get("senha_2")
        
        if senha_1 and senha_2 and senha_1!= senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("Senhas não coincidem")
            else:
                return senha_2
        