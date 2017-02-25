from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.test import TestCase

from .forms import CatalogFormAdd, CatalogFormRemove, ItemFormAdd, ItemFormRemove
from .models import Catalog, Item


class ModelTest(TestCase):

	def setUp(self):
		self.catalog = Catalog.objects.create(name='Root')
		self.item = Item.objects.create(name='Item 1', catalog=self.catalog)

	def test_tree_relationships(self):
		cat = Catalog.objects.create(name='Documents', parent=self.catalog)
		self.assertIn(cat, self.catalog.get_children())
		self.assertIn(self.catalog, cat.get_ancestors())

		Item.objects.create(name='File 1', catalog=cat)
		Item.objects.create(name='File 2', catalog=cat)
		Item.objects.create(name='File 3', catalog=cat)
		self.assertEqual(len(cat.item_set.all()), 3)

	def test_delete_branch(self):
		Item.objects.create(name='Item 2', catalog=self.catalog)
		self.assertEqual(len(Item.objects.all()), 2)

		self.catalog.delete()
		self.assertEqual(len(Item.objects.all()), 0)

	def test_unique_names(self):
		# problem with transactions and intentionally triggering an exception
		with transaction.atomic(), self.assertRaises(IntegrityError):
			Catalog.objects.create(name='Root')

		with transaction.atomic(), self.assertRaises(IntegrityError):
			Item.objects.create(name='Item 1', catalog=self.catalog)

	def test_required_catalog_field(self):
		with transaction.atomic(), self.assertRaises(IntegrityError):
			Item.objects.create(name='Item 2')

	# test model methods
	def test_string_representation(self):
		self.assertEqual(str(self.catalog), 'Root')
		self.assertEqual(str(self.item), 'Item 1')


class FormTest(TestCase):

	def setUp(self):
		self.catalog = Catalog.objects.create(name='Root')
		self.item = Item.objects.create(name='Item 1', catalog=self.catalog)

	def test_save_CatalogFormAdd_valid_form(self):
		form = CatalogFormAdd(data={'name': 'Trash', 'parent': self.catalog.pk})
		self.assertTrue(form.is_valid())
		form.save()
		self.assertEqual(len(Catalog.objects.all()), 2)

	def test_save_CatalogFormAdd_invalid_form(self):
		form = CatalogFormAdd(data={})
		self.assertFalse(form.is_valid())
		with self.assertRaises(ValueError):
			form.save()
		self.assertEqual(len(Catalog.objects.all()), 1)

	def test_save_CatalogFormRemove_valid_form(self):
		form = CatalogFormRemove(data={'parent': self.catalog.pk})
		self.assertTrue(form.is_valid())
		self.assertIn(self.catalog, Catalog.objects.all())
		form.save()
		self.assertNotIn(self.catalog, Catalog.objects.all())

	def test_save_CatalogFormRemove_invalid_form(self):
		form = CatalogFormRemove(data={'parent': -1})
		self.assertFalse(form.is_valid())
		with self.assertRaises(KeyError):
			form.save()
		self.assertIn(self.catalog, Catalog.objects.all())

	def test_save_ItemFormAdd_valid_form(self):
		form = ItemFormAdd(data={'name': 'Item 2',
								 'catalog': self.catalog.pk,
								 'description': '...',
								 'link': 'www.google.com'})
		self.assertTrue(form.is_valid())
		item_instance = form.save()
		self.assertIn(item_instance, Item.objects.all())

	def test_save_ItemFormAdd_invalid_form(self):
		form = ItemFormAdd(data={'name': 'Item 2',
								 'catalog': -1,
								 'description': '...',
								 'link': 'com'})
		self.assertFalse(form.is_valid())
		with self.assertRaises(ValueError):
			form.save()
		self.assertEqual(len(Item.objects.all()), 1)

	def test_save_ItemFormRemove_valid_form(self):
		form = ItemFormRemove(data={'item': self.item.pk})
		self.assertTrue(form.is_valid())
		self.assertIn(self.item, Item.objects.all())
		form.save()
		self.assertNotIn(self.item, Item.objects.all())

	def test_save_ItemFormRemove_invalid_form(self):
		form = ItemFormRemove(data={'item': -1})
		self.assertFalse(form.is_valid())
		with self.assertRaises(KeyError):
			form.save()
		self.assertIn(self.item, Item.objects.all())

class ViewTest(TestCase):
	pass
