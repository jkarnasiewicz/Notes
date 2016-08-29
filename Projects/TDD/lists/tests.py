# Testy jednostkowe
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template import RequestContext
from django.template.loader import render_to_string

from lists.models import Item
from lists.views import home_page


class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		context = RequestContext(request)
		response = home_page(request)
		expected_html = render_to_string('lists/home.html', context)
		self.assertEqual(response.content.decode(), expected_html)				# decode converts bytes to string(unicode)

		# self.assertTrue(response.content.strip().startswith(b'<html>'))		# response.content return bytes so we need use b'' syntax
		# self.assertIn(b'<title>Listy rzeczy do zrobienia</title>', response.content)
		# self.assertTrue(response.content.strip().endswith(b'</html>'))

	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'Nowy element listy'
		context = RequestContext(request)

		response = home_page(request)

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'Nowy element listy')

		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

		# self.assertIn('Nowy element listy', response.content.decode())
		# expected_html = render_to_string(
		# 	'lists/home.html',
		# 	{'new_item_text': 'Nowy element listy'},
		# 	context
		# )
		# self.assertEqual(response.content.decode(), expected_html)

	# def test_home_page_displays_all_list_items(self):
	# 	Item.objects.create(text='itemey 1')
	# 	Item.objects.create(text='itemey 2')

	# 	request = HttpRequest()
	# 	response = home_page(request)

	# 	self.assertIn('itemey 1', response.content.decode())
	# 	self.assertIn('itemey 2', response.content.decode())


class ItemModelTest(TestCase):

	def test_saving_and_retriving_items(self):
		first_item = Item()
		first_item.text = 'Absolutnie pierwszy element listy'
		first_item.save()

		second_item = Item()
		second_item.text = 'Drugi element'
		second_item.save()

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		self.assertEqual(saved_items[0].text, 'Absolutnie pierwszy element listy')
		self.assertEqual(saved_items[1].text, 'Drugi element')


class ListViewTest(TestCase):

	def test_uses_list_template(self):
		response = self.client.get('/lists/the-only-list-in-the-world')
		self.assertTemplateUsed(response, 'lists/list.html')				# response.template_name

	def test_displays_all_items(self):
		Item.objects.create(text='itemey 1')
		Item.objects.create(text='itemey 2')

		response = self.client.get('/lists/the-only-list-in-the-world')

		self.assertContains(response, 'itemey 1')
		self.assertContains(response, 'itemey 2')
