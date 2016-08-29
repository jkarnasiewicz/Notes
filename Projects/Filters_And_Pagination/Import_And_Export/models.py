# -*- coding: UTF-8 -*-
import os

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

class Movie(models.Model):
	title = models.CharField(max_length=100)
	url = models.URLField(max_length=200)
	release_year = models.DateField()


def upload_to(instance, filename):
	filename_base, filename_ext = os.path.splitext(filename)
	return 'tracks/%s--%s%s' % (
		slugify(instance.artist),
		slugify(instance.name),
		filename_ext.lower(),
	)


class Track(models.Model):
	name = models.CharField(_("Nazwa"), max_length=250)
	artist = models.CharField(_("Artysta"), max_length=250)
	url = models.URLField(_("URL"))
	image = models.ImageField(_("Obraz"), upload_to=upload_to, blank=True, null=True)

	class Meta:
		verbose_name = _(u"Ścieżka")
		verbose_name_plural = _(u"Ścieżki")

	def __str__(self):
		return u"%s - %s" % (self.artist, self.name)
