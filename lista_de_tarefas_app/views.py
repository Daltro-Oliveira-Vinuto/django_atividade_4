from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Tarefa
# Create your views here.


def lista_de_tarefas(request):
	if request.method == "POST":

		titulo = request.POST.get('titulo')
		prazo_str = request.POST.get('prazo')
		prazo = None
		if prazo_str:
			from datetime import datetime
			prazo = datetime.strptime(prazo_str, '%Y-%m-%d').date()
		if titulo:
			Tarefa.objects.create(titulo=titulo, prazo = prazo)

		return redirect('lista_de_tarefas')

	else:

		query_tarefas = Tarefa.objects.all()

		context = {
			'all_tasks': query_tarefas,
			'today_object': timezone.now().date(),
		}

		return render(request, "lista_de_tarefas_app/lista_de_tarefas.html", context)

	

@require_POST
def toggle_concluida(request, pk):
	tarefa = get_object_or_404(Tarefa, pk=pk)
	tarefa.concluida = not tarefa.concluida
	tarefa.save()

	return redirect('lista_de_tarefas')

@require_POST
def deletar_tarefa(request, pk):
	tarefa = get_object_or_404(Tarefa,pk=pk)
	tarefa.delete()

	return redirect('lista_de_tarefas')
	



