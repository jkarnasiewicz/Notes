from django.core.urlresolvers import reverse
from django.test import TestCase

from .views import auth_chat

class Viewest(TestCase):

	def test_auth_chat_page_uses_correct_view(self):
		response = self.client.get(reverse('auth_chat:auth_chat'))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.resolver_match.func, auth_chat)

	def test_auth_chat_page_render_correct_template(self):
		response = self.client.get(reverse('auth_chat:auth_chat'))

		self.assertTemplateUsed(response, 'auth_chat/home.html')

	def test_auth_chat_page_uses_correct_forms(self):
		pass
