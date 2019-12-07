from django.shortcuts import render

from .models import Captura
# Create your views here.
def capturas(request, code_user):
	data = {}

	data['titulo'] = 'Capturas de Informação'
	data['capturas'] = Capturas.objects.filter(code_user = code_user)
	data['code_user'] = code_user

	return render(request, 'capturas.html', data)