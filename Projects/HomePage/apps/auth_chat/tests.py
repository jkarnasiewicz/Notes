from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.test import TestCase

from .forms import CreateUser
from .views import auth_chat


User = auth.get_user_model()


class ModelTest(TestCase):
	pass


class FormTest(TestCase):
	pass




class ViewTest(TestCase):

	def test_auth_chat_page_uses_correct_view(self):
		response = self.client.get(reverse('auth_chat:auth_chat'))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.resolver_match.func, auth_chat)

	def test_auth_chat_page_render_correct_template(self):
		response = self.client.get(reverse('auth_chat:auth_chat'))

		self.assertTemplateUsed(response, 'auth_chat/home.html')

	def test_auth_chat_page_uses_correct_forms(self):
		response = self.client.get(reverse('auth_chat:auth_chat'))

		self.assertIsInstance(response.context['create_user_form'], CreateUser)
		self.assertIsInstance(response.context['log_in_form'], AuthenticationForm)

	def test_auth_chat_page_valid_POST_for_create_user_form(self):
		response = self.client.post(
			reverse('auth_chat:auth_chat'),
			data={
				'username': 'imaginary_name',
				'password1': 'fake_password_123',
				'password2': 'fake_password_123',
				'create_user_form': 'Create User',
			},
			follow=True)


		# from pprint import pprint
		# pprint(response.client.session.items())
		self.assertEqual(response.status_code, 200)

		user = auth.get_user(self.client)
		self.assertEqual(user.username, 'imaginary_name')

	def test_auth_chat_page_invalid_POST_for_create_user_form(self):
		response = self.client.post(
			reverse('auth_chat:auth_chat'),
			data={
				'username': 'I',
				'password1': 'I',
				'password2': 'J',
				'create_user_form': 'Create User',
			})

		self.assertEqual(response.status_code, 200)
		self.assertIn('username', response.context['create_user_form'].errors)
		self.assertIn('password2', response.context['create_user_form'].errors)

	def test_auth_chat_page_valid_POST_for_log_in_form(self):
		new_user = User.objects.create_user(username='imaginary_name', email='test@test.com', password='fake_password_123')
		self.client.login(username='imaginary_name', password='fake_password_123')

		response = self.client.post(
			reverse('auth_chat:auth_chat'),
			data={
				'username': 'imaginary_name',
				'password': 'fake_password_123',
				'log_in_form': 'Log in',
			},
			follow=True)

		self.assertEqual(response.status_code, 200)

		logged_in_user = auth.get_user(self.client)
		self.assertEqual(logged_in_user.username, new_user.username)

	def test_auth_chat_page_invalid_POST_for_log_in_form(self):
		new_user = User.objects.create_user(username='imaginary_name', email='test@test.com', password='fake_password_123')
		self.client.login(username='imaginary_name', password='fake_password_123')

		response = self.client.post(
			reverse('auth_chat:auth_chat'),
			data={
				'username': 'imaginary',
				'password': 'fake_password_123',
				'log_in_form': 'Log in',
			},
			follow=True)

		self.assertEqual(response.status_code, 200)
		self.assertIn('__all__', response.context['log_in_form'].errors)

	def test_auth_chat_page_valid_POST_for_logging_out_user(self):
		new_user = User.objects.create_user(username='imaginary_name', email='test@test.com', password='fake_password_123')
		self.client.login(username='imaginary_name', password='fake_password_123')

		response = self.client.post(
			reverse('auth_chat:auth_chat'),
			data={
				'log_out': 'Log out',
			},
			follow=True)

		self.assertEqual(response.status_code, 200)
		self.assertIsInstance(auth.get_user(self.client), auth.models.AnonymousUser)
