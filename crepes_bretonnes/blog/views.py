from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404


# Create your views here.

def home(request):
    """Exemple de page non valide au niveau HTML pour que l'exemple soit concis"""
    return HttpResponse("""
		<h1>Bienvenue sur mon blog ! </h1>
		<p>Les crepes bretonnes ca tue les mouettes en plein vol ! </p>
	""")


def view_article(request, id_article):
    """
	Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
	"""

    if id_article > 100:
        raise Http404

    return redirect(
        view_redirection
    )


def list_article(request, month, year):
    return redirect("https://www.djangoproject.com")


def view_redirection(request):
    return HttpResponse(
        'Vous avez ete redirige'
    )


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})

def addition(request, nombre1, nombre2):
	total = nombre1 + nombre2

# Retourne nombre1, nombre2 et la somme des deux au tpl
	return render(request, 'blog/addition.html', locals())

def mapage(request):
    return render(request, "blog/mapage.html")
