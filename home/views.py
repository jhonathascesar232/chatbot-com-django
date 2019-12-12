from django.shortcuts import render

# Create your views here.
def home(request):
	data = {}

	data['titulo'] = 'HOME'
	return render(request, 'home.html', data)