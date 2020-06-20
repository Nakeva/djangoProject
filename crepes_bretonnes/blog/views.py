from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	"""Exemple de page non valide au niveau HTML pour que l'exemple soit concis"""
	return HttpResponse("""
		<h1>Bienvenue sur mon blog ! </h1>
		<p>Les crepes bretonnes ca tue les mouettes en plein vol ! </p>
	""")
