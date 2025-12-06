from django.db import models
from django.utils import timezone
# Create your models here.

class Tarefa(models.Model):
	titulo = models.CharField(max_length=200)

	descricao = models.TextField(blank=True, null=True)
	concluida = models.BooleanField(default=False)
	data_criacao = models.DateTimeField("Criada em", auto_now_add=True)

	prazo = models.DateField("Prazo", null=True, blank="True")

	def __str__(self):
		# aparecera no painel Admin
		return self.titulo

	def prazo_vencido(self):
		if self.prazo and not self.concluida:
			return self.prazo < timezone.now().date()
		return False


	class Meta:
		ordering = ['prazo', '-data_criacao']
		verbose_name = "Tarefa"
		verbose_name_plural = "Tarefas"
