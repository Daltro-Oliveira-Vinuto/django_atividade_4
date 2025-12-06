from django.urls import path
from . import views

urlpatterns = [
	path('', views.lista_de_tarefas, name='lista_de_tarefas'),
	path('toggle/<int:pk>/', views.toggle_concluida, name='toggle_concluida'),
	path('deletar/<int:pk>', views.deletar_tarefa, name='deletar_tarefa')
]

