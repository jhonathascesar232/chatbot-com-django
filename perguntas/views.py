from django.shortcuts import render

from .models import Pergunta
# serve para a protecao dos formularios via token
from django.views.decorators.csrf import csrf_protect

from django.http import JsonResponse	# vamos emitir respostas Json para nossas requisições http
# assim vamos ter aqui uma api restfull

from capturas.models import Captura 	# vamos salvar os dados da captura atraves das perguntas no banco

# Create your views here.

codeUser = 0

def perguntas(request, code_user):
	data = {}

	data['titulo'] = 'Cadastro de Perguntas e Respostas'
	data['pergunta'] = Pergunta.objects.filter(code_user = code_user) # filtra todos os objetos com code_user
	global codeUser
	codeUser = code_user
	data['code_user'] = code_user

	return render(request, 'perguntas.html', data)

def pergunta(request, id):
	data = {}

	data['titulo'] = 'Cadastro de Perguntas e Respostas'
	data['pergunta'] = [Pergunta.objects.get(id = id)]
	global codeUser
	data['code_user'] = codeUser

	return render(request, 'perguntas.html', data)

def novo(request, code_user):
	data = {}
	data['titulo'] = 'Inserção de Perguntas e Respostas'
	data['todas'] = Pergunta.objects.filter(code_user = code_user)
	data['code_user'] = code_user

	return render(request, 'novoPerguntas.html', data)