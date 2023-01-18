from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	data = {
		'title': 'Main page',
		'values': ['Book', 'Pencil', 'Note'],
		'book': {
			'name': 'Unnamed',
			'status': 'In process',
			'author': 'Symon Petrikov'
		}
	}
	#return HttpResponse('<h3>Thats Alive!</h3>')
	return render(request, 'main/index.html', data)

def about(request):
	return HttpResponse('<h3>Some shit about us</h3>')