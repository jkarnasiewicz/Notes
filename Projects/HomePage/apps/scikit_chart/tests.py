import json

from django.core.urlresolvers import reverse
from django.test import TestCase

from .views import scikit_chart


class ViewTest(TestCase):
	
	def test_scikit_chart_page_uses_correct_view(self):
		response = self.client.get(reverse('scikit_chart:scikit_chart'))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.resolver_match.func, scikit_chart)

	def test_scikit_chart_page_render_correct_template(self):
		response = self.client.get(reverse('scikit_chart:scikit_chart'))

		self.assertTemplateUsed(response, 'scikit_chart/home.html')

	def test_regresion_line_view_invalid_request_method(self):
		response = self.client.get(reverse('scikit_chart:regression_line'))

		self.assertEqual(response.status_code, 404)

	def test_regresion_line_view_valid_POST_request(self):
		data = json.dumps({
			'observations_x': [-86.86635944700461, -68.4331797235023,
							   -52.764976958525345, -41.013824884792626,
							   -32.718894009216584, -23.27188940092165,
							   -12.21198156682027, -5.299539170506904,
							   10.599078341013822, 24.193548387096783],
			'observations_y': [-77.02127659574468, -67.65957446808511,
							   -56.17021276595745, -49.787234042553195,
							   -42.97872340425532, -38.297872340425535,
							   -29.361702127659584, -26.382978723404264,
							   -18.297872340425542, -9.361702127659584]})
		response = self.client.post(
			reverse('scikit_chart:regression_line'),
			HTTP_X_REQUESTED_WITH='XMLHttpRequest',
			content_type='application/json',
			data=data)

		self.assertEqual(response.status_code, 200)
		self.assertIn('regression_line', response.content.decode('utf-8'))
		self.assertIn('application/json', response['Content-Type'])

	def test_regresion_line_view_invalid_POST_request(self):
		data = json.dumps({
			'observations_x': [-86.86635944700461],
			'observations_y': [-77.02127659574468]})

		with self.assertRaises(ValueError):
			response = self.client.post(
				reverse('scikit_chart:regression_line'),
				HTTP_X_REQUESTED_WITH='XMLHttpRequest',
				content_type='application/json',
				data=data)

	def test_k_nearest_neighborns_view_invalid_request_method(self):
		response = self.client.get(reverse('scikit_chart:k_nearest_neighborns'))

		self.assertEqual(response.status_code, 404)
 
	def test_k_nearest_neighborns_view_valid_POST_request(self):
		pass

	def test_k_nearest_neighborns_view_valid_POST_request(self):
		pass
