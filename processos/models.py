from django.db import models

class Instrutor(models.Model):

    nome = models.CharField(('Nome'), max_length=50, null=True, blank=True)
    rg = models.IntegerField('RG')
    nascimento = models.DateField('Data de nascimento', blank=True, null=True)
    titulacao = models.IntegerField('Titulação')

    def __str__(self):
        return self.nome

class Telefone(models.Model):

    pertence = models.ForeignKey(Instrutor, on_delete=models.CASCADE, related_name='Instrutor')
    numero = models.IntegerField('Número')
    tipo = models.CharField(('Tipo'), max_length=20, null=True, blank=True)

    def __str__(self):
        return self.pertence.nome

class Atividade(models.Model):

    nomeA = models.CharField(('Nome'), max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nomeA

class Turma(models.Model):

    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, related_name='Atividade')
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    horario = models.TimeField('Horário', blank =True, null=True)
    duracao = models.IntegerField('Duração')
    dataInicio = models.DateField('Data Início', blank=True, null=True)
    dataFim = models.DateField('Data Final', blank=True, null=True)

    def __str__(self):
        return self.instrutor.nome+" "+str(self.horario)


class Aluno(models.Model):

    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='Turma')
    nomeAl = models.CharField(('Nome'), max_length=50, null=True, blank=True)
    endereco = models.TextField('Endereço', null=True, blank=True)
    telefoneA = models.IntegerField('Telefone')
    dataNasc = models.DateField('Data de nascimento', blank=True, null=True)
    altura = models.DecimalField('Altura', max_digits=3, decimal_places=2)
    peso = models.IntegerField('Peso')
    dataMat = models.DateField('Data da matrícula', blank=True, null=True)

    def __str__(self):
        return self.nomeAl



class Chamada(models.Model):

    codigoA = models.ManyToManyField(Aluno, related_name='Aluno')
    turmaId = models.ManyToManyField(Turma, related_name='T')
    dataC = models.DateField('Data')
    presenca = models.BooleanField('Presente', default=True)

    def __str__(self):
        return str(self.presenca)