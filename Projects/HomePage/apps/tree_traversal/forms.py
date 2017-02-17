from django import forms
from django.utils.html import mark_safe

from mptt.forms import TreeNodeChoiceField

from .models import Catalog, Item

class CatalogForm(forms.ModelForm):
	parent = TreeNodeChoiceField(
		label='Parent',
		queryset=Catalog.objects.all(),
		required=False,
		level_indicator=mark_safe('&nbsp;&nbsp;&nbsp;&nbsp;'),
	)

	class Meta:
		model = Catalog
		fields = ('name', 'parent')


class ItemForm(forms.ModelForm):
	catalog = TreeNodeChoiceField(
		label='Catalog',
		queryset=Catalog.objects.all(),
		required=False,
		level_indicator=mark_safe('&nbsp;&nbsp;&nbsp;&nbsp;'),
	)

	class Meta:
		model = Item
		fields = ('name', 'link', 'description', 'catalog')
