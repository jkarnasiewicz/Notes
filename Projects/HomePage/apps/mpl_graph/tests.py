from django.core.urlresolvers import reverse
from django.test import TestCase

from .views import mpl_graph


class ViewTest(TestCase):

	def test_mpl_graph_page_uses_correct_view(self):
		response = self.client.get(reverse('mpl_graph:mpl_graph'))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.resolver_match.func, mpl_graph)

	def test_mpl_graph_page_render_correct_template(self):
		response = self.client.get(reverse('mpl_graph:mpl_graph'))

		self.assertTemplateUsed(response, 'mpl_graph/home.html')
