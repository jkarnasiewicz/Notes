from tempfile import NamedTemporaryFile

import pandas as pd

from django import forms
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from django.template import Template, Context
from django.test import TestCase

from .context_processors import current_app
from .utilities import PlotGraph

from apps.search_app.models import Applications


class ImaginaryForm(forms.Form):
	'Imaginary form for testing purpose'
	name = forms.CharField(max_length=10, required=True)

	def fake_method(self):
		'fake method for testing purpose'


class ContextProcessorTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		cls.image = NamedTemporaryFile(suffix=".png").name
		cls.app = Applications.objects.create(name='App 1', description='...', image=cls.image,
			tags='python, django', url_source='http://example.com', url_name='search_app', visible=True)

	def test_current_app_function_valid(self):
		response = self.client.get(reverse('search_app:search_app'))
		self.assertEqual(current_app(response.wsgi_request).get('current_app', None), self.app)

	def test_current_app_function_invalid(self):
		response = self.client.get('/imaginary_url')
		self.assertEqual(current_app(response.wsgi_request).get('current_app', None), None)


class TemplatetagTest(TestCase):

	def test_form_field_tag(self):
		form = ImaginaryForm(prefix='imaginary_form')
		template = Template('{% load utility_tags %} {% form_field form.name %}')
		render_temp = template.render(Context({'form': form}))

		self.assertIn('class="form-group"', render_temp)
		self.assertIn('<label for="id_imaginary_form-name"', render_temp)
		self.assertIn('class="form-control"', render_temp)
		self.assertIn('type="text"', render_temp)
		self.assertIn('<span>*</span>', render_temp)
		self.assertNotIn('error', render_temp)
		# TO DO - each field in separete function

	def test_form_field_tag_with_error(self):
		form = ImaginaryForm(prefix='imaginary_form', data={'imaginary_form-name': 'Incorrect long name'})
		template = Template('{% load utility_tags %} {% form_field form.name %}')
		render_temp = template.render(Context({'form': form}))

		self.assertIn('error_1', render_temp)
		self.assertIn('<strong>Ensure this value has at most 10 characters', render_temp)

	def test_attr_list_tag(self):
		template = Template('{% load utility_tags %} {% attr_list form %}')
		render_temp = template.render(Context({'form': ImaginaryForm}))

		self.assertIn('<p>is_valid</p>', render_temp)
		self.assertIn('<p>as_table</p>', render_temp)
		self.assertIn('<p>fake_method</p>', render_temp)


class UtilitiesTest(TestCase):

	def test_PlotGraph_valid_default_data(self):
		data_frame = pd.DataFrame(data=[(-1, 1), (0, 0), (1, 1)], columns=['X', 'Y'])
		response = PlotGraph(data_frame).create_response()

		self.assertEqual(response.status_code, 200)
		self.assertEqual('image/svg+xml', response['Content-Type'])
		self.assertIn('attachment;', response['Content-Disposition'])

	def test_PlotGraph_valid_data(self):
		data_frame = pd.DataFrame(data=[(-1, 1), (0, 0), (1, 1)], columns=['X', 'Y'])
		response = PlotGraph(
			data_frame,
			title='Imaginary title',
			x_label='fake X',
			y_label='fake Y',
			extension='pdf',
			style='classic').create_response()

		self.assertEqual(response.status_code, 200)
		self.assertEqual('application/pdf', response['Content-Type'])
		self.assertIn('attachment;', response['Content-Disposition'])

	def test_PlotGraph_invalid_data(self):
		data_frame = pd.DataFrame(data=[(-1, 'k'), (0, 0), (1, 'm')], columns=['X', 'Y'])
		with self.assertRaises(ValueError):
			response = PlotGraph(data_frame).create_response()


class StaticFilesTest(TestCase):
	'Check if application contains required static files'

	def test_base_css(self):
		abs_path = finders.find('css/base.css', all=True)
		# self.assertTrue(staticfiles_storage.exists(abs_path))
		self.assertTrue(abs_path)

	def test_bootstrap_css(self):
		abs_path = finders.find('css/bootstrap.min.css', all=True)
		self.assertTrue(abs_path)

	def test_bootstrap_js(self):
		abs_path = finders.find('js/bootstrap.min.js', all=True)
		self.assertTrue(abs_path)

	def test_jumbotron_png(self):
		abs_path = finders.find('images/jumbotron.png', all=True)
		self.assertTrue(abs_path)
