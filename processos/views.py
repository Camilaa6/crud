from datetime import date
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
######## Cliente



def instrutor(request):
    instrutor = Instrutor.objects.all()
    if request.method == 'POST':
        form = InstrutorForm(request.POST)

        if form.is_valid():
            form.save()
            #messages.success(request, 'Aluno cadastrado com sucesso')
            return redirect('instrutor')

    form = InstrutorForm()

    context = {
        'form': form,
        #Chave/Valor
        'instrutor': instrutor
    }

    return render(request, 'instrutor.html', context)


def instrutor_edit(request, pk):
    instrutor = Instrutor.objects.get(pk=pk)
    instrutor1 = Instrutor.objects.get(nome='Abc')
    print(instrutor1)

    form = InstrutorForm(request.POST or None, instance=instrutor)

    if form.is_valid():
        form.save()
       # messages.success(request, 'Cadastro alterado com sucesso')
        return redirect('instrutor')

    context = {
        'form': form,
        'instrutor': instrutor
    }

    return render(request, 'instrutor_edit.html', context)

def instrutor_delete(request, pk):
    instrutor = Instrutor.objects.get(pk=pk)
    instrutor.delete()
  #  messages.error(request, 'Cadastro removido com sucesso')

    return redirect('instrutor')

def aluno(request):
    aluno = Aluno.objects.all()

    if request.method == 'POST':
        form = AlunoForm(request.POST)

        if form.is_valid():
            form.save()
            #messages.success(request, 'Aluno cadastrado com sucesso')
            return redirect('aluno')

    form = AlunoForm()

    context = {
        'form': form,
        #Chave/Valor
        'aluno': aluno
    }

    return render(request, 'aluno.html', context)

def aluno_edit(request, pk):
    aluno = Aluno.objects.get(pk=pk)


    form= AlunoForm(request.POST or None, instance=aluno)

    if form.is_valid():
        form.save()
       # messages.success(request, 'Cadastro alterado com sucesso')
        return redirect('aluno')

    context = {
        'form': form,
        'aluno': aluno
    }

    return render(request, 'aluno_edit.html', context)

def aluno_delete(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    aluno.delete()
  #  messages.error(request, 'Cadastro removido com sucesso')

    return redirect('aluno')

def turma(request):
    turma = Turma.objects.all()
    if request.method == 'POST':
        form = TurmaForm(request.POST)

        if form.is_valid():
            form.save()
            #messages.success(request, 'Aluno cadastrado com sucesso')
            return redirect('turma')

    form = TurmaForm()

    context = {
        'form': form,
        #Chave/Valor
        'turma': turma
    }

    return render(request, 'turma.html', context)

def turma_edit(request, pk):
    turma = Turma.objects.get(pk=pk)

    form= TurmaForm(request.POST or None, instance=turma)

    if form.is_valid():
        form.save()
       # messages.success(request, 'Cadastro alterado com sucesso')
        return redirect('turma')

    context = {
        'form': form,
        'turma': turma
    }

    return render(request, 'turma_edit.html', context)

def turma_delete(request, pk):
    turma = Turma.objects.get(pk=pk)
    turma.delete()
  #  messages.error(request, 'Cadastro removido com sucesso')

    return redirect('turma')

def telefone(request):
    telefone = Telefone.objects.all()
    if request.method == 'POST':
        form = TelefoneForm(request.POST)

        if form.is_valid():
            form.save()
            #messages.success(request, 'Aluno cadastrado com sucesso')
            return redirect('telefone')

    form = TelefoneForm()

    context = {
        'form': form,
        #Chave/Valor
        'telefone': telefone
    }

    return render(request, 'telefone.html', context)

def telefone_edit(request, pk):
    telefone = Telefone.objects.get(pk=pk)

    form= TelefoneForm(request.POST or None, instance=telefone)

    if form.is_valid():
        form.save()
       # messages.success(request, 'Cadastro alterado com sucesso')
        return redirect('telefone')

    context = {
        'form': form,
        'telefone': telefone
    }

    return render(request, 'telefone_edit.html', context)

def telefone_delete(request, pk):
    telefone = Telefone.objects.get(pk=pk)
    telefone.delete()
  #  messages.error(request, 'Cadastro removido com sucesso')

    return redirect('telefone')

def atividade(request):
    atividade = Atividade.objects.all()
    if request.method == 'POST':
        form = AtividadeForm(request.POST)

        if form.is_valid():
            form.save()
            #messages.success(request, 'Aluno cadastrado com sucesso')
            return redirect('atividade')

    form = AtividadeForm()

    context = {
        'form': form,
        #Chave/Valor
        'atividade': atividade
    }

    return render(request, 'atividade.html', context)

def atividade_edit(request, pk):
    atividade = Atividade.objects.get(pk=pk)

    form= AtividadeForm(request.POST or None, instance=atividade)

    if form.is_valid():
        form.save()
       # messages.success(request, 'Cadastro alterado com sucesso')
        return redirect('atividade')

    context = {
        'form': form,
        'atividade': atividade
    }

    return render(request, 'atividade_edit.html', context)

def atividade_delete(request, pk):
    atividade = Atividade.objects.get(pk=pk)
    atividade.delete()
  #  messages.error(request, 'Cadastro removido com sucesso')

    return redirect('atividade')

def chamada(request):
    chamada = Chamada.objects.all()
    data = date.today()
   # print(chamada[1])
    if request.method == 'POST':
        form = ChamadaForm(request.POST)

        if form.is_valid():
            form.save()
            #messages.success(request, 'Aluno cadastrado com sucesso')
            return redirect('chamada')

    form = ChamadaForm()

    context = {
        'form': form,
        #Chave/Valor
        'chamada': chamada,
        'data': data
    }

    return render(request, 'chamada.html', context)

def chamada_edit(request, pk):
    chamada = Chamada.objects.get(pk=pk)
    print(chamada)

    form= ChamadaForm(request.POST or None, instance=chamada)

    if form.is_valid():
        form.save()
       # messages.success(request, 'Cadastro alterado com sucesso')
        return redirect('chamada')

    context = {
        'form': form,
        'chamada': chamada
    }

    return render(request, 'chamada_edit.html', context)