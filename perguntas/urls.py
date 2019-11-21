from django.urls import path # para criar enderecos

from .views import perguntas, pergunta, novo, salvarNovo, edicao, salvarEdicao, delecao, salvarDelecao, chatbot, questao, api

urlpatterns = [
	path('<int:code_user>', perguntas, name = 'perguntas'),
	path('pergunta/<int:id>', pergunta, name = 'pergunta'),
	path('novo/<int:code_user>', novo, name = 'novo'),
	path('salvarNovo', salvarNovo, name = 'salvarNovo'),
	path('edicao/<int:id>', edicao, name = 'edicao'),
	path('salvarEdicao', salvarEdicao, name = 'salvarEdicao'),
	path('delecao/<int:id>', delecao, name = 'delecao'),
	path('salvarDelecao/', salvarDelecao, name = 'salvarDelecao'),
	path('chatbot/<int:code_user>', chatbot, name = 'chatbot'),
	path('questao/<int:code_user>/<int:code_before/>/<str:question>', questao, name = 'questao'),	# code_before  para comparar
	path('api/<int:code_user>', api, name = 'api'),

]