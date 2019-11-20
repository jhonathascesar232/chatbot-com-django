from django.db import models

# Create your models here.

class Captura(models.Model):
	code = models.CharField(max_length=15)
	code_user = models.CharField(max_length=15)
	active = models.IntegerField()
	code_ralation = models.CharField(max_length=15) # irá relacio a resposta atual com a pergunta anterior
	question = models.CharField(max_length=500)		# pergunta
	answer = models.CharField(max_length=500)		# resposta

	def __str__(self):
		return self.question