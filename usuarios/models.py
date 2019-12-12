from django.db import models

# Create your models here.
class Usuario(models.Model):
	code = models.CharField(max_length = 15)
	active = models.IntegerField()
	name = models.CharField(max_length=100)		# nome
	email = models.CharField(max_length=100)	# email
	user = models.CharField(max_length=50)		# usuario
	password = models.CharField(max_length=15)	# senha

	def __str__(self):
		return self.name