# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from FaP.models import CreationModificationDateMixin
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey, TreeManyToManyField

class Category(MPTTModel, CreationModificationDateMixin):
	parent = TreeForeignKey("self", blank=True, null=True, db_index=True)
	title = models.CharField(_(u"Title"), max_length=200)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['tree_id', 'lft']
		verbose_name = _('Category')
		verbose_name_plural = _('Categories')


class Movie(CreationModificationDateMixin):
	title = models.CharField(_(u'Title'), max_length=255)
	categories = TreeManyToManyField(Category, verbose_name=_('Categories'))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('Movie')
		verbose_name_plural = _('Movies')


'''
# MPTTModel methods
# Aby znaleźć przodków kategorii, użyj następującego kodu:
ancestor_categories = category.get_ancestors(ascending=False, include_self=False)
# Parametr ascending określa kierunek odczytywania węzłów (jego domyślna wartość
# to False ). Parametr include_self określa, czy w zbiorze wyników QuerySet uwzględnić
# też samą kategorię (domyślna wartość to False ).


# Aby pobrać tylko kategorię główną, użyj następującego kodu:
root = category.get_root()


# Jeśli trzeba pobrać bezpośrednich potomków kategorii, możesz użyć następującego kodu:
children = category.get_children()


# Aby pobrać wszystkich potomków kategorii, użyj następującego kodu:
descendants = category.get_descendants(include_self=False)


# Jeśli chcesz sprawdzić tylko liczbę potomków, bez wysyłania zapytania do bazy danych, możesz użyć poniższego kodu:
descendants_count = category.get_descendant_count()


# Do pobrania wszystkich elementów siostrzanych użyj poniższego kodu:
siblings = category.get_siblings(include_self=False)
# Kategorie główne są elementami siostrzanymi innych kategorii głównych.


# Aby pobrać tylko poprzedni i następny element siostrzany, wywołaj poniższe metody:
previous_sibling = category.get_previous_sibling()
next_sibling = category.get_next_sibling()


# Poniższych metod użyj do sprawdzania, czy kategoria jest korzeniem, dzieckiem czy liściem:
category.is_root_node()
category.is_child_node()
category.is_leaf_node()


# Do zmieniania struktury drzewa można używać metod
insert_at()
move_to()
# Więcej informacji o tych i innych metodach do pracy na drzewach można znaleźć na stronie
# http://django-mptt.github.io/django-mptt/models.html
'''