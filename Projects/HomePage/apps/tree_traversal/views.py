from django.shortcuts import render

from .forms import CatalogForm, ItemForm
from .models import Catalog


def tree_traversal(request):
	ctx = {
		'nodes': Catalog.objects.all(),
		'catalog_form': CatalogForm(data=request.POST or None),
		'item_form': ItemForm(data=request.POST or None),
	}
	return render(request, 'tree_traversal/home.html', ctx)
