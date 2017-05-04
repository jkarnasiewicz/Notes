from django import forms
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

from .models import LoggedInUser

User = auth.get_user_model()


class CreateUser(UserCreationForm):
	username = forms.CharField(required=True, min_length=3, max_length=15)


def auth_chat(request):
	create_user_form = CreateUser()
	log_in_form = AuthenticationForm()
	logged_in_users = User.objects.filter(id__in=LoggedInUser.objects.values_list('user', flat=True))

	if request.method == 'POST' and 'create_user_form' in request.POST:
		create_user_form = CreateUser(data=request.POST or None)
		if create_user_form.is_valid():
			create_user_form.save()
			user = auth.authenticate(username=create_user_form.cleaned_data['username'],
								 	 password=create_user_form.cleaned_data['password1'])
			auth.login(request, user)
			return redirect('auth_chat:auth_chat')

	if request.method == 'POST' and 'log_in_form' in request.POST:
		log_in_form = AuthenticationForm(data=request.POST or None)
		if log_in_form.is_valid():
			auth.login(request, log_in_form.get_user())
		return redirect('auth_chat:auth_chat')

	if request.method == 'POST' and 'log_out' in request.POST:
		auth.logout(request)
		return redirect('auth_chat:auth_chat')

	return render(
		request,
		'auth_chat/home.html',
		{'create_user_form': create_user_form,
		 'log_in_form': log_in_form,
	     'logged_in_users': logged_in_users})


# def log_in(request):
#     form = AuthenticationForm()
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             login(request, form.get_user())
#             return redirect(reverse('example:user_list'))
#         else:
#             print(form.errors)
#     return render(request, 'example/log_in.html', {'form': form})


# @login_required(login_url='/log_in/')
# def log_out(request):
#     logout(request)
#     return redirect(reverse('example:log_in'))


# def sign_up(request):
#     form = UserCreationForm()
#     if request.method == 'POST':
#         form = UserCreationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('example:log_in'))
#         else:
#             print(form.errors)
#     return render(request, 'example/sign_up.html', {'form': form})
