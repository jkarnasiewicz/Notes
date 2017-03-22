from django.core.urlresolvers import reverse
from django.test import TestCase

from .views import julia_set


class ViewTest(TestCase):

	def test_julia_set_page_usess_correct_view(self):
		response = self.client.get(reverse('julia_set:julia_set'))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.resolver_match.func, julia_set)

	def test_julia_set_page_render_correct_tamplates(self):
		response = self.client.get(reverse('julia_set:julia_set'))

		self.assertTemplateUsed(response, 'julia_set/home.html')
