# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

COUNTRY_CHOICES = (
	("PL", _("Polska")),
	("DE", _("Niemcy")),
	("FR", _("Francja")),
	("LT", _("Litwa")),
)

class Location(models.Model):
	title = models.CharField(_(u"tytuł"), max_length=255, unique=True)
	description = models.TextField(_("opis"), blank=True)
	street_address = models.CharField(_("adres"), max_length=255, blank=True)
	street_address2 = models.CharField(_("adres (kontynuacja)"), max_length=255, blank=True)
	postal_code = models.CharField(_("kod pocztowy"), max_length=10, blank=True)
	city = models.CharField(_("miasto"), max_length=255, blank=True)
	country = models.CharField(_("kraj"), max_length=2, blank=True, choices=COUNTRY_CHOICES)
	latitude = models.FloatField(
		_(u"szerokość geograficzna"),
		help_text=_(u"Szerokość geograficzna to kąt zawarty między dowolnym punktem a równikiem"
					"(biegun północny maszerokość geograficzną 90, a południowy — -90)."),
		blank=True,
		null=True)
	longitude = models.FloatField(
		_(u"długość geograficzna"), 
		help_text=_("Długość geograficzna to kąt zawarty między dowolnnym punktem na Ziemi a południkiem 0"
					"przechodzącym przez park w Greenwich w Wielkiej Brytanii. Na wschód od południka 0 położone"
					" są punkty o długości geograficznej wschodniej, a na zachód — punkty o długości geograficznej zachodniej."),
		blank=True,
		null=True)

	class Meta:
		verbose_name = _("Miejsce")
		verbose_name_plural = _("Miejsca")

	def __str__(self):
		return self.title
