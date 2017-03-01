from tempfile import NamedTemporaryFile

from django import forms
from django.core.urlresolvers import reverse
from django.template import Template, Context
from django.test import TestCase

from .context_processors import current_app

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
