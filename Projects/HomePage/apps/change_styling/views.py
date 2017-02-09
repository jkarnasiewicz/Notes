from django.shortcuts import render

def change_styling(request):
	return render(request, 'change_styling/home.html')
