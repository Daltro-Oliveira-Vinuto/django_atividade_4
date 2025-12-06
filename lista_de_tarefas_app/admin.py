from django.contrib import admin
from .models import Tarefa
# Register your models here.

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'prazo', 'concluida', 'prazo_vencido')
	list_filter = ('concluida', 'prazo')
	search_fields = ('titulo', )
	date_hierarchy = 'prazo'
