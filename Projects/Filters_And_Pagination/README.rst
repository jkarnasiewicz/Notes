Book:
Aplikacje internetowe z django - najlepsze receptury (Web Development with Django Cookbook)




Additional apps informations:
FaP - filtry, paginacja, implementacja ciągłego przewijania, widżet polubień(content_type and mixins),
	  zmiany w standardowym adminie(zmiany w polach, filtrach, dodawanie obrazów, pola z kluczami obcymi)


AdminMap - google maps in admin


Mptt - struktury hierarchiczne (modified preorder tree traversal — MPTT)
	   (django-mpt, django-mptt-admin, django-mptt-tree-editor)
	   zmodyfiko-wany algorytm przeglądania wzdłużnego drzewa,
	   crispy_forms z szablonami html


Import_And_Export - management(tworzenie komend), import i eksport danych z i do pliku
					Jeśli chcesz mieć możliwość diagnozowania błędów podczas pracy nad poleceniem zarządzania, możesz
					przekazać do niego parametr --traceback. Jeżeli wystąpi błąd, zostanie wyświetlony cały stos wywołań.


Programu pośredniczący ThreadLocalMiddleware - HttpRequest dostępny wszędzie (utils.py)


Django debug toolbar (pip install django-debug-toolbar) - settings, utils.py, and in browser bookmarks:
	1) Nazwa: Debug Toolbar on
	   URL: javascript:(function(){document.cookie="DebugToolbar=1;path=/";location.href=location.href;})();
	2) Nazwa: Debug Toolbar off
	   URL: javascript:(function(){document.cookie="DebugToolbar=0;path=/";location.href=location.href;})();


Wysyłanie raportów o błędach na adres e-mail(z HTML-em)(https://docs.djangoproject.com/en/1.9/topics/logging/)
Działa tylko dla DEBUG=False
	settings.py:
	LOGGING = {
		"version": 1,
		"disable_existing_loggers": False,
		"filters": {
			"require_debug_false": {
				"()": "django.utils.log.RequireDebugFalse",
			},
			"require_debug_true": {
				"()": "django.utils.log.RequireDebugTrue",
			},
		},
		"handlers": {
			"console": {
				"level": "INFO",
				"filters": ["require_debug_true"],
				"class": "logging.StreamHandler",
			},
			"null": {
				"class": "django.utils.log.NullHandler",
			},
			"mail_admins": {
				"level": "ERROR",
				"filters": ["require_debug_false"],
				"class": "django.utils.log.AdminEmailHandler",
				"include_html": True,
			}
		},
		"loggers": {
			"django": {
				"handlers": ["console"],
			},
			"django.request": {
				"handlers": ["mail_admins"],
				"level": "ERROR",
				"propagate": False,
			},
			"django.security": {
				"handlers": ["mail_admins"],
				"level": "ERROR",
				"propagate": False,
			},
			"py.warnings": {
				"handlers": ["console"],
			},
		}
	}



Additional book information:
1) Tworzenie kanałów RSS z możliwością filtrowania
2) Tastypie
3) Zastępowanie modelu administracji(wielojęzyczne pola)
4) Wdrażanie aplikacji na serwerze Apache przy użyciu modułu mod_wsgi
5) Tworzenie i używanie skryptu wdrażania Fabric
