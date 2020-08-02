from django.urls import path, include
from . import views
from .views import *
urlpatterns = [
   # path('cliente/', views.cliente, name='cliente')
    # Cliente
    path('aluno/', views.aluno, name='aluno'),
    path('aluno_edit/<int:pk>/', views.aluno_edit, name='aluno_edit'),
    path('aluno_delete/<int:pk>/', views.aluno_delete, name='aluno_delete'),
    path('instrutor/', views.instrutor, name='instrutor'),
    path('instrutor_editado/<int:pk>/', views.instrutor_edit, name='instrutor_edit'),
    path('instrutor_delete/<int:pk>/', views.instrutor_delete, name='instrutor_delete'),
    path('turma/', views.turma, name='turma'),
    path('turma_edit/<int:pk>/', views.turma_edit, name='turma_edit'),
    path('turma_delete/<int:pk>/', views.turma_delete, name='turma_delete'),
    path('telefone/', views.telefone, name='telefone'),
    path('telefone_edit/<int:pk>/', views.telefone_edit, name='telefone_edit'),
    path('telefone_delete/<int:pk>/', views.telefone_delete, name='telefone_delete'),
    path('atividade/', views.atividade, name='atividade'),
    path('atividade_edit/<int:pk>/', views.atividade_edit, name='atividade_edit'),
    path('atividade_delete/<int:pk>/', views.atividade_delete, name='atividade_delete'),
    path('chamada/', views.chamada, name='chamada'),
    path('chamada_edit/<int:pk>/', views.chamada_edit, name='chamada_edit'),
]