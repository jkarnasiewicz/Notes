# -*- coding: UTF-8 -*-
import json
import os
import glob
from random import sample

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.contrib.contenttypes.models import ContentType


from .models import Genre, Director, Actor, Movie, Serials, Like, RATING_CHOICES
from .forms import MovieFilterForm

from Filters_And_Pagination.templatetags.utility_tags import get_likes_count


def home(request):
	qs = Movie.objects.order_by('title')
	form = MovieFilterForm(data=request.GET)
	facets = {
		'selected': {},
		'categories': {
			'genres': Genre.objects.all(),
			'directors': Director.objects.all(),
			'actors': Actor.objects.all(),
			'ratings': RATING_CHOICES,
		},
	}
	
	if form.is_valid():
		# Filters
		facets, qs = form.filter(facets, qs)

	# Pagination
	paginator = Paginator(qs, 3)			# queryset and limit per page
	page_number = request.GET.get('page')
	try:
		page = paginator.page(page_number)
	except PageNotAnInteger:
		# jeśli numer strony nie jest liczbą całkowitą, wyświetla pierwszą stronę
		page = paginator.page(1)
	except EmptyPage:
		# jeśli numer jest za duży, wyświetla ostatnią stronę
		page = paginator.page(paginator.num_pages)


	# Infinite scroll
	serials_qs = Serials.objects.order_by('title')
	serials_paginator = Paginator(serials_qs, 5)
	serials_page_number = request.GET.get('serial_page')
	try:
		serials_page = serials_paginator.page(serials_page_number)
	except PageNotAnInteger:
		# jeśli numer strony nie jest liczbą całkowitą, wyświetla pierwszą stronę
		serials_page = serials_paginator.page(1)
	except EmptyPage:
		# jeśli numer jest za duży, wyświetla ostatnią stronę
		serials_page = serials_paginator.page(serials_paginator.num_pages)

	context = {
		'form': form,
		'facets': facets,
		'serials_page': serials_page,
		'object_list': page,
	}
	return render(request, 'FaP/home.html', context)


def movie_detail_modal(request, pk):
	movie = get_object_or_404(Movie, pk=pk)
	genres = movie.genres.get_queryset()
	wall_url = sample(
			os.listdir(os.path.join(settings.BASE_DIR, 'Filters_And_Pagination', 'static', 'img')), 3)

	return render(request, 'FaP/movie_detail_modal.html', {'movie': movie, 'genres': genres, 'wall_url': wall_url})


@never_cache
@csrf_exempt
def json_set_like(request, content_type_id, object_id):
	"""
	Ustawia obiekt jako ulubiony obiekt bieżącego użytkownika.
	"""
	json_str = "false"
	if request.user.is_authenticated() and request.method == "POST":
		content_type = ContentType.objects.get(id=content_type_id)
		obj = content_type.get_object_for_this_type(pk=object_id)
		like, is_created = Like.objects.get_or_create(
			content_type=ContentType.objects.get_for_model(obj),
			object_id=obj.pk,
			user=request.user,
		)
		if not is_created:
			like.delete()

		result = {
			'obj': str(obj),
			'action': is_created and "added" or "removed",
			'count': get_likes_count(obj),
		}
		json_str = json.dumps(result, ensure_ascii=False)
	return HttpResponse(json_str, content_type='application/json')
	# return JsonResponse({'json_str': json_str})
