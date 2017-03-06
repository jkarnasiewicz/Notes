from django.core.urlresolvers import reverse
from django.test import TestCase

from .views import codility


class ModelTest(TestCase):
	pass


class ViewTest(TestCase):
	
	def test_codility_page_uses_correct_view(self):
		response = self.client.get(reverse('codility:codility'))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.resolver_match.func, codility)

	def test_codility_page_render_correct_template(self):
		response = self.client.get(reverse('codility:codility'))

		self.assertTemplateUsed(response, 'codility/home.html')
