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

def getCODE():
	from datetime import datetime

	dataHora = datetime.now()
	code = str(dataHora.year)
	code += str(dataHora.month)
	code += str(dataHora.day)
	code += str(dataHora.hour)
	code += str(dataHora.minute)
	code += str(dataHora.second)
# converte pra int, faz o arredondamento com zero casas decimais, converte pra int, converte pra str
	code = str(int(round(int(code) /2, 0)))

	return code

@csrf_protect
def salvarNovo(request):
	code = getCODE()
	code_user = request.POST.get('code_user')
	active = 1
	code_relation = request.POST.get('code_relation')
	question = request.POST.get('question')
	answer = request.POST.get('answer')

	p = Pergunta(
		code = code,
		code_user = code_user,
		active = active,
		code_relation = code_relation,
		question = question,
		answer = answer,
	)

	data = {}
	data['code_user'] = code_user

	return render(request ,'redirecionar.html', data)

def edicao(request, id):
	data = {}

	data['titulo'] = 'Edição de Perguntas e Respostas'
	data['todas'] = Pergunta.objects.filter(code_user = code_user)
	data['perguntas'] = Pergunta.objects.get(id = id)
	global codeUser
	data['code_user'] = codeUser

	return render(request, 'edicaoPerguntas.html', data)

# salvar edicao
@csrf_protect
def salvarNovo(request):
	id = int(request.POST.get('id'))
	code_user = request.POST.get('code_user')
	code_relation = request.POST.get('code_relation')
	question = request.POST.get('question')
	answer = request.POST.get('answer')

	Pergunta.objects.filter(id=id).update(
		code = code,
		code_user = code_user,
		active = active,
		code_relation = code_relation,
		question = question,
		answer = answer,
	)

	data = {}
	data['code_user'] = code_user

	return render(request ,'redirecionar.html', data)

# delecao
def delecao(request):
	global codeUser
	data = {}

	data['titulo'] = 'Deleção de Perguntas e Respostas'
	data['todas'] = Pergunta.objects.filter(code_user = code_user)
	data['perguntas'] = Pergunta.objects.get(id = id)
	data['code_user'] = codeUser

	return render(request, 'edicaoPerguntas.html', data)

# salvar delecao
@csrf_protect
def salvarDelecao(request):
	data = {}

	id = int(request.POST.get('id'))
	data['code_user'] = request.POST.get('code_user')
	Pergunta.objects.filter(id = id).delete()

	return render(request ,'redirecionar.html', data)

# chatboot
def chatbot(request, code_user):
	data = {}

	data['titulo'] = 'Chatbot'
	data['code_user'] = code_user

	return render(request, 'chatbot.html', data)

# nlp - processamento de linguagem natural
def questao(request, code_user, code_before, question):