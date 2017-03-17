import io

from django.core.urlresolvers import reverse
from django.test import TestCase

from .forms import PlotForm
from .views import mpl_graph


class FormTest(TestCase):
	'FORM TESTS AND PLOT CLASS'
	pass


class ViewTest(TestCase):

	def test_mpl_graph_page_uses_correct_view(self):
		response = self.client.get(reverse('mpl_graph:mpl_graph'))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.resolver_match.func, mpl_graph)

	def test_mpl_graph_page_render_correct_template(self):
		response = self.client.get(reverse('mpl_graph:mpl_graph'))

		self.assertTemplateUsed(response, 'mpl_graph/home.html')

	def test_mpl_graph_page_uses_correct_form(self):
		response = self.client.get(reverse('mpl_graph:mpl_graph'))

		self.assertIsInstance(response.context['form'], PlotForm)

	def test_mpl_graph_form_valid_POST_headers(self):
		response = self.client.post(
			reverse('mpl_graph:mpl_graph'),
			data={
				'file': '',
				'custom_pattern': '-x**2',
				'min_value': '',
				'max_value': '',
				'step': '',
				'random': '',
				'extension': 'svg',
				'style': 'seaborn-dark-palette',
				'title': '',
				'x_label': '',
				'y_label': '',
				'file_input': 'Generate Graph'
			})

		self.assertEqual(response.status_code, 200)
		self.assertIn('image/svg+xml', response['Content-Type'])
		self.assertIn('attachment;', response['Content-Disposition'])

	def test_mpl_graph_form_valid_POST_file(self):
		f = io.StringIO('X, Y\n1, 3\n7, 23')
		response = self.client.post(
			reverse('mpl_graph:mpl_graph'),
			data={
				'file': f,
				'custom_pattern': '',
				'min_value': '',
				'max_value': '',
				'step': '',
				'random': '',
				'extension': 'pdf',
				'style': 'classic',
				'title': '',
				'x_label': '',
				'y_label': '',
				'file_input': 'Generate Graph'})

		self.assertEqual(response.status_code, 200)
		self.assertIn('application/pdf', response['Content-Type'])
		self.assertIn('attachment;', response['Content-Disposition'])

	def test_mpl_graph_form_valid_POST_random_data(self):
		response = self.client.post(
			reverse('mpl_graph:mpl_graph'),
			data={
				'file': '',
				'custom_pattern': '',
				'min_value': '',
				'max_value': '',
				'step': '',
				'random': True,
				'extension': 'png',
				'style': 'classic',
				'title': '',
				'x_label': '',
				'y_label': '',
				'file_input': 'Generate Graph'})

		self.assertEqual(response.status_code, 200)
		self.assertIn('image/png', response['Content-Type'])
		self.assertIn('attachment;', response['Content-Disposition'])

	def test_mpl_graph_form_invalid_POST_no_data(self):
		response = self.client.post(
			reverse('mpl_graph:mpl_graph'),
			data={
				'file': '',
				'custom_pattern': '',
				'min_value': '',
				'max_value': '',
				'step': '',
				'random': '',
				'extension': 'svg',
				'style': 'seaborn-dark-palette',
				'title': '',
				'x_label': '',
				'y_label': '',
				'file_input': 'Generate Graph'
			})

		self.assertEqual(response.status_code, 200)
		self.assertTrue(response.context['form'].non_field_errors())

	def test_mpl_graph_form_invalid_POST_fields(self):
		response = self.client.post(
			reverse('mpl_graph:mpl_graph'),
			data={
				'file': '',
				'custom_pattern': 'x',
				'min_value': '-90000000',
				'max_value': '90000000',
				'step': '-100',
				'random': '',
				'extension': 'imaginary_extension',
				'style': 'imaginary_style',
				'title': '',
				'x_label': '',
				'y_label': '',
				'file_input': 'Generate Graph'
			})

		self.assertIn('style', response.context['form'].errors)
		self.assertIn('extension', response.context['form'].errors)
		self.assertIn('step', response.context['form'].errors)
		self.assertIn('min_value', response.context['form'].errors)
		self.assertIn('max_value', response.context['form'].errors)

		# from pprint import pprint
		# print(len(response.context['form'].errors))
		# print('alert alert-danger' in response.content.decode('utf-8'))
		# pprint('alert alert-danger' in response.content)
		# pprint(dir(response.context['form'].non_field_errors))
		# pprint(dir(response))
		# pprint(response._headers)
		# pprint(response['Content-Type'])
		# pprint(response['Content-Disposition'])

		# pprint(response.wsgi_request)
		# pprint(response.status_code)
		# pprint(response.content)
		# pprint(response.context['form']._errors)
		# pprint(response.context['form'].error_class)
		# pprint(response.context['form'].non_field_errors())
		# self.assertTrue([])
		# self.assertEqual(response.status_code, 200)
		# self.assertTrue(response.context['form'].non_field_errors())
		# self.assertEqual(
		# 	response.context['form'].non_field_errors(),
		# 	['Change a few things up and try submitting again.'])
		# pprint(response.context['form'])
