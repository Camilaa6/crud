from django import forms
from .models import *

class InstrutorForm(forms.ModelForm):

    class Meta:
        model= Instrutor
        fields='__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'rg': forms.TextInput(attrs={'class': 'form-control', 'id': 'Login'}),
            'nascimento': forms.TextInput(attrs={'class': 'form-control', 'id': 'Password'}),
            'titulacao': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'situacao', 'onclick': 'myFunction()'}),

        }

class AlunoForm(forms.ModelForm):

    class Meta:
        model= Aluno
        fields='__all__'
        widgets = {


        }

class TurmaForm(forms.ModelForm):

    class Meta:
        model= Turma
        fields='__all__'
        widgets = {}

class TelefoneForm(forms.ModelForm):

    class Meta:
        model= Telefone
        fields='__all__'
        widgets = {}

class AtividadeForm(forms.ModelForm):

    class Meta:
        model= Atividade
        fields='__all__'
        widgets = {}

class ChamadaForm(forms.ModelForm):

    class Meta:
        model= Chamada
        fields='__all__'
        widgets = {}

