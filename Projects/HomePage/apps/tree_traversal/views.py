from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.template.loader import render_to_string

from .forms import CatalogFormAdd, CatalogFormRemove, ItemFormAdd, ItemFormRemove
from .models import Catalog


def tree_traversal(request):
	ctx = {
		'nodes': Catalog.objects.all(),
		'catalog_form_add': CatalogFormAdd(prefix='catalog_form_add'),
		'catalog_form_remove': CatalogFormRemove(prefix='catalog_form_remove'),
		'item_form_add': ItemFormAdd(prefix='item_form_add'),
		'item_form_remove': ItemFormRemove(prefix='item_form_remove'),
	}
	print(request.POST)
	form_dict = {'catalog_form_add': CatalogFormAdd, 'catalog_form_remove': CatalogFormRemove, 'item_form_add': ItemFormAdd, 'item_form_remove': ItemFormRemove}
	if request.method == 'POST' and request.is_ajax():
		form_name = request.POST['form_name']
		form = form_dict.get(form_name, None)
		if form:
			form = form(prefix=form_name, data=request.POST)
			if form.is_valid():
				form.save()
				# renderujemy cala zawartosc
				# request_context = RequestContext(request)
				# print(request_context)
				# template = render_to_string('tree_traversal/tree_forms.html', ctx, request_context.get('request'))
				template = render_to_string('tree_traversal/tree_forms.html', request=request, context=ctx)
				return JsonResponse({'template': template, 'form_name': form_name})
			else:
				ctx[form_name] = form
				template = render_to_string('tree_traversal/tree_forms.html', request=request, context=ctx)
				return JsonResponse({'template': template, 'form_name': form_name})


	
	return render(request, 'tree_traversal/home.html', ctx)
