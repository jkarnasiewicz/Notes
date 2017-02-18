from django.shortcuts import redirect, render

from .forms import CatalogForm, ItemForm
from .models import Catalog


def tree_traversal(request):
	print(request.POST)
	ctx = {
		'nodes': Catalog.objects.all(),
		'catalog_form': CatalogForm(prefix='catalog_form', data=request.POST or None),
		'item_form': ItemForm(prefix='item_form', data=request.POST or None),
	}
	return render(request, 'tree_traversal/home.html', ctx)


# def add_catalog(request):
# 	return redirect('tree_traversal:tree_traversal')


# def add_file(request):
# 	return redirect('tree_traversal:tree_traversal')
