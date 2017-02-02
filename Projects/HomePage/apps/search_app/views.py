from django.shortcuts import render
from .models import Applications

def search_app_home(request):
	ctx = {}
	ctx['applications'] = Applications.objects.filter(visible=True)
	return render(request, 'search_app/home.html', ctx)
