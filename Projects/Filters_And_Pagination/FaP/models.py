# -*- coding: UTF-8 -*-
import os

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import FieldError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now as timezone_now


RATING_CHOICES = (
	(1, u"☆"),
	(2, u"☆☆"),
	(3, u"☆☆☆"),
	(4, u"☆☆☆☆"),
	(5, u"☆☆☆☆☆"),
)

def upload_to(instance, filename):
	now = timezone_now()
	filename_base, filename_ext = os.path.splitext(filename)
	return 'movies/{0}/{1}{2}'.format(
		instance.movie.title,
		now.strftime("%Y%m%d%H%M%S"),
		filename_ext.lower(),
	)


class Genre(models.Model):
	title = models.CharField(_(u"Tytuł"), max_length=100)

	def __str__(self):
		return self.title


class Director(models.Model):
	first_name = models.CharField(_(u"Imię"), max_length=40)
	last_name = models.CharField(_("Nazwisko"), max_length=40)

	def __str__(self):
		return self.first_name + ' ' + self.last_name


class Actor(models.Model):
	first_name = models.CharField(_(u"Imię"), max_length=40)
	last_name = models.CharField(_("Nazwisko"), max_length=40)

	def __str__(self):
		return self.first_name + ' ' + self.last_name


class Movie(models.Model):
	title = models.CharField(max_length=255)
	genres = models.ManyToManyField(Genre, blank=True)
	directors = models.ManyToManyField(Director, blank=True)
	actors = models.ManyToManyField(Actor, blank=True)
	rating = models.PositiveIntegerField(choices=RATING_CHOICES)

	def __str__(self):
		return self.title


class MoviePhoto(models.Model):
	movie = models.ForeignKey(Movie)
	photo = models.ImageField(_('photo'), upload_to=upload_to)

	class Meta:
		verbose_name = _(u'Zdjęcie')
		verbose_name_plural = _(u'Zdjęcia')

	def __str__(self):
		return self.photo.name


class Serials(models.Model):
	title = models.CharField(_(u"Tytuł"), max_length=255)

	def __str__(self):
		return self.title


# LIKES #


class CreationModificationDateMixin(models.Model):
	"""
	Abstrakcyjna klasa bazowa z datą utworzenia i modyfikacji
	"""
	created = models.DateTimeField(_("Data i godzina utworzenia"), editable=False)
	modified = models.DateTimeField(_("Data i godzina modyfikacji"), null=True, editable=False)

	def save(self, *args, **kwargs):
		if not self.pk:
			self.created = timezone_now()
		else:
			# dodajemy to, aby zawsze mieć datę utworzenia
			if not self.created:
				self.created = timezone_now()
			self.modified = timezone_now()

		super(CreationModificationDateMixin, self).save(*args, **kwargs)

	save.alters_data = True

	class Meta:
		abstract = True


# Jest to funkcja generującą domieszkę do modelu. Dynamicznie tworzona domieszka
# dodaje pola content_type i object_id oraz generyczny klucz obcy content_object
# wskazujący powiązany egzemplarz.
# Dynamicznie generowana klasa abstrakcyjna umożliwia utworzenie przedrostków dla nazwy
# każdego pola, dzięki czemu możemy utworzyć więcej niż jedną generyczną relację w tym samym
# modelu
def object_relation_mixin_factory(
		prefix=None,
		prefix_verbose=None,
		add_related_name=False,
		limit_content_type_choices_to={},
		limit_object_choices_to={},
		is_required=False,
	):
	"""
	Zwraca klasę domieszkową dla generycznych kluczy obcych przy użyciu "Content type - id. obiektu"
	z dynamicznymi nazwami pól. Funkcja ta jest tylko generatorem klas.
	Parametry:
	prefix : przedrostek dodawany na początku pól
	prefix_verbose : pełna nazwa przedrostka, używana do generowania tytułu dla kolumny
	pola obiektu treści w panelu administracyjnym.
	add_related_name : wartość logiczna wskazująca, że należy dodać powiązaną nazwę wygenerowanego
	klucza obcego typu treści. Powinna to być wartość true, jeśli w modelu używany jest więcej niż jeden
	egzemplarz domieszki ObjectRelationMixin.
	Pola modelu tworzy się następująco:
	<<prefix>>_content_type : nazwa pola dla „typu treści”
	<<prefix>>_object_id : nazwa pola dla „identyfikatora obiektu”
	<<prefix>>_content_object : nazwa pola dla „obiektu treści”
	"""
	if prefix:
		p = "%s_" % prefix
	else:
		p = ""

	content_type_field = "%scontent_type" % p
	object_id_field = "%sobject_id" % p
	content_object_field = "%scontent_object" % p

	class TheClass(models.Model):
		class Meta:
			abstract = True

	if add_related_name:
		if not prefix:
			raise FieldError(u"Jeśli add_related_name ma wartość True, należy podać przedrostek.")
		related_name = prefix
	else:
		related_name = None

	content_type = models.ForeignKey(
		ContentType,
		verbose_name=(prefix_verbose and _(u"Typ (model) %s") % \
			prefix_verbose or _(u"Typ (model) powiązanego obiektu")),
		related_name=related_name,
		blank=not is_required,
		null=not is_required,
		help_text=_(u"Wybierz typ (model) relacji, którą chcesz zbudować."),
		limit_choices_to=limit_content_type_choices_to,
	)

	object_id = models.CharField(
		(prefix_verbose or _(u"Powiązany obiekt")),
		blank=not is_required,
		null=False,
		help_text=_(u"Podaj identyfikator powiązanego obiektu."),
		max_length=255,
		default="", # dla migracji South
	)

	object_id.limit_choices_to = limit_object_choices_to
	# można pobrać za pomocą
	# MyModel._meta.get_field("object_id").limit_choices_to
	content_object = GenericForeignKey(
		ct_field=content_type_field,
		fk_field=object_id_field,
	)

	TheClass.add_to_class(content_type_field, content_type)
	TheClass.add_to_class(object_id_field, object_id)
	TheClass.add_to_class(content_object_field, content_object)

	return TheClass


class Like(CreationModificationDateMixin, object_relation_mixin_factory(is_required=True)):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)

	class Meta:
		verbose_name = _("polubienie")
		verbose_name_plural = _("polubienia")
		ordering = ('-created',)

	def __str__(self):
		return _(u"{user}s lubi {obj}s".format({'user': self.user, 'obj': self.content_object}))
