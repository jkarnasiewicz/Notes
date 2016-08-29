# -*- coding: UTF-8 -*-
from django.shortcuts import render

from .models import Category
from .forms import MovieFilterForm, MovieForm


def movie_category_list(request):
	context = {
		'single_choice_form': MovieFilterForm(prefix='single'),
		'multiple_choice_form': MovieForm(request.POST or None, prefix='multiple'),
		'categories': Category.objects.all(),
	}
	return render(request, 'Mptt/movie_category_list.html', context)
