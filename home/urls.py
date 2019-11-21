from django.urls import path # para criar enderecos

from .views import home

urlpatterns = [
	path('', home, name = 'home'),
]