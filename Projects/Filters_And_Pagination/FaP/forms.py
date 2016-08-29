# -*- coding: UTF-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Genre
from .models import Director
from .models import Actor
from .models import RATING_CHOICES


class MovieFilterForm(forms.Form):
	genre = forms.ModelChoiceField(
		label=_("Gatunek"),
		required=False,
		queryset=Genre.objects.all(),
	)
	director = forms.ModelChoiceField(
		label=_(u"Reżyser"),
		required=False,
		queryset=Director.objects.all(),
	)
	actor = forms.ModelChoiceField(
		label=_("Aktor"),
		required=False,
		queryset=Actor.objects.all(),
	)
	rating = forms.ChoiceField(
		label=_("Ocena"),
		required=False,
		choices=RATING_CHOICES,
	)

	def filter(self, facets, qs):
		genre = self.cleaned_data['genre']
		if genre:
			facets['selected']['genre'] = genre
			qs = qs.filter(genres=genre).distinct()
		director = self.cleaned_data['director']
		if director:
			facets['selected']['director'] = director
			qs = qs.filter(directors=director).distinct()
		actor = self.cleaned_data['actor']
		if actor:
			facets['selected']['actor'] = actor
			qs = qs.filter(actors=actor).distinct()
		rating = self.cleaned_data['rating']
		if rating:
			facets['selected']['rating'] = (int(rating), dict(RATING_CHOICES)[int(rating)])
			qs = qs.filter(rating=rating).distinct()
		return facets, qs
