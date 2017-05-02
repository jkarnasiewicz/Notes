from django.shortcuts import render


def auth_chat(request):
	return render(request, 'auth_chat/home.html')
