# -*- coding: UTF-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from .models import Location

class LocationAdmin(admin.ModelAdmin):
	save_on_top = True
	list_display = ("title", "street_address", "description")
	search_fields = ("title", "street_address", "description")
	# pola grupujemy w zestawy pól
	fieldsets = [
		(_(u"Dane główne"), {'fields': ('title', 'description')}),
		(_("Adres"), {'fields': ('street_address', 'street_address2', 'postal_code', 'city', 'country', 'latitude', 'longitude')}),
	]

admin.site.register(Location, LocationAdmin)