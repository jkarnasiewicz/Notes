# -*- coding: UTF-8 -*-
# Programu pośredniczący ThreadLocalMiddleware (HttpRequest accessible everywhere)
from threading import local
_thread_locals = local()

def get_current_request():
	""" Zwraca obiekt HttpRequest dla tego wątku. """
	return getattr(_thread_locals, "request", None)

def get_current_user():
	""" Zwraca bieżącego użytkownika, jeśli istnieje, lub wartość None. """
	request = get_current_request()
	if request:
		return getattr(request, "user", None)


class ThreadLocalMiddleware(object):
	""" Program pośredniczący, który dodaje obiekt HttpRequest do schowka w wątku."""
	def process_request(self, request):
		_thread_locals.request = request

# Add in settings
# MIDDLEWARE_CLASSES = (
# 	# ...
# 	"Filters_And_Pagination.utils.ThreadLocalMiddleware",
# )

# Somewhere in code
# def save(self, *args, **kwargs):
# 	from utils.middleware import get_current_user
# 	if not self.creator:
# 		self.creator = get_current_user()
# 	...





# Django debug toolbar
def custom_show_toolbar(request):
	return "1" == request.COOKIES.get("DebugToolbar", False)
