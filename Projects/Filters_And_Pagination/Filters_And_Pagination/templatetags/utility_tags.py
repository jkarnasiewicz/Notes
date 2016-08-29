# -*- coding: UTF-8 -*-
### Znacznik - tag ###
### Filtr - filter ###
import re
import urllib
from datetime import datetime

from django import template
from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import now as tz_now
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe
from django.template import loader
from django.template.loader import get_template
from django.apps import apps

from FaP.models import Like

register = template.Library()


# Modyfikacja i tworzenie zapytania get
# =====================================
@register.simple_tag(takes_context=True)
def append_to_query(context, **kwargs):
	""" Renderuje odnośnik ze zmodyfikowanymi zapytaniami bieżącego zapytania. """
	query_params = context['request'].GET.copy()
	for key, value in kwargs.items():
		query_params[key] = value
	query_string = u""
	if len(query_params):
		query_string += u"?{}".format('&amp;'.join(
			['{}={}'.format(key, force_str(value)) for key, value in query_params.items() if value]))
	return query_string

# In html
# {% load utility_tags %}
# {% append_to_query serial_page=serials_page.next_page_number %}




# Pobieranie pierwszego obiektu mediów
# ====================================
media_file_regex = re.compile(r"<iframe .+?</iframe>|"
							  r"<audio .+?</audio>|<video .+?</video>|"
							  r"<object .+?</object>|<(img|embed) [^>]+>")

@register.filter
def get_first_media(content):
	""" Zwraca pierwszy obraz lub plik Flash z treści HTML. """
	m = media_file_regex.search(content)
	media_tag = ""
	if m:
		media_tag = m.group()
	return mark_safe(media_tag)

# In html
# {% load utility_tags %}
# {{ object.content|get_first_media }}




# Adresy URL bez protokołu i końcowego ukośnika
# =============================================
@register.filter
def humanize_url(url, letter_count):
	""" Zwraca skrócony czytelny adres URL. """
	letter_count = int(letter_count)
	re_start = re.compile(r'^https?://')
	re_end = re.compile(r'/$')
	url = re_end.sub("", re_start.sub("", url))
	if len(url) > letter_count:
		url = u"%s…¦" % url[:letter_count - 1]
	return url

# In html
# {% load utility_tags %}
# <a href="{{ object.website }}" target="_blank"> {{ object.website|humanize_url:30 }} </a>




# Przelicznik liczby dni
# =============================================
# @register.filter(name="humanized_days_since")
@register.filter
def days_since(value):
	""" Zwraca liczbę dni między aktualną datą a podaną wartością. """
	today = tz_now().date()
	if isinstance(value, datetime.datetime):
		value = value.date()
	diff = today - value
	if diff.days > 1:
		return _("%s dni temu") % diff.days
	elif diff.days == 1:
		return _("wczoraj")
	elif diff.days == 0:
		return _(u"dziś")
	else:
		# Podano przyszłą datę, zwraca sformatowaną datę.
		return value.strftime("%B %d, %Y")

# In html
# {% load utility_tags %}
# {{ object.created|days_since }}




# Like widget
# ===========
@register.tag
def like_widget(parser, token):
	try:
		# funkcja split_contents() nie dzieli łańcuchów w cudzysłowie
		tag_name, for_str, obj = token.split_contents()
	except ValueError:
		raise (template.TemplateSyntaxError,
			"Znacznik %r ma następującą składnię:{%% %r for <object> %%}" % (token.contents[0],
				token.contents[0]))
	return ObjectLikeWidget(obj)



@register.filter
def get_likes_count(obj):
	ct = ContentType.objects.get_for_model(obj)
	return Like.objects.filter(
		content_type=ct,
		object_id=obj.pk,
	).count()



class ObjectLikeWidget(template.Node):
	def __init__(self, obj):
		self.obj = obj

	def render(self, context): 
		obj = template.resolve_variable(self.obj, context)
		ct = ContentType.objects.get_for_model(obj)

		is_liked_by_user = bool(Like.objects.filter(
			user=context['request'].user,
			content_type=ct,
			object_id=obj.pk,
		))

		context.push()
		context['object'] = obj
		context['content_type_id'] = ct.pk
		context['is_liked_by_user'] = is_liked_by_user
		context['count'] = get_likes_count(obj)
		output = loader.render_to_string("FaP/like.html", context)
		context.pop()
		return output



# Dołączanie szablonu, jeśli istnieje
# ===================================
@register.tag
def try_to_include(parser, token):
	""" Sposób użycia: {% try_to_include "szablon.html" %}
	Jeśli szablon nie istnieje, nastąpi cicha awaria. Jeśli szablon istnieje,
	zostanie wygenerowany przy użyciu bieżącego kontekstu."""
	try:
		tag_name, template_name = token.split_contents()
	except ValueError:
		raise (template.TemplateSyntaxError,
			   "Znacznik %r wymaga pojedynczego argumentu." % token.contents.split()[0])
	return IncludeNode(template_name)


class IncludeNode(template.Node):
	def __init__(self, template_name):
		self.template_name = template_name

	def render(self, context):
		try:
			# Ładowanie i renderowanie szablonu.
			template_name = template.resolve_variable(self.template_name, context)
			included_template = get_template(template_name).render(context)
		except template.TemplateDoesNotExist:
			included_template = ""
		return included_template


# 1) Dołączanie szablonu, którego ścieżka jest zdefiniowana przy użyciu znacznika
#    szablonowego {% with %} gdzieś wysoko w zakresie zmiennej kontekstowej szablonu
# 2) Dołączanie szablonu, którego ścieżka jest zdefiniowana w modelu, na przykład:
# In html
# {% load utility_tags %}
# {% try_to_include object.template_path %}

# or

# {% load utility_tags %}
# {% for object in object_list %}
#     {% try_to_include "artists/includes/artist_item.html" %}
# {% endfor %}




# Ładowania zestawu obiektów do szablonu(context)
# ==========================================================================================
# Znacznik szablonowy {% get_objects %} ładuje obiekt QuerySet zdefiniowany przez metodę
# manager z określonych aplikacji i modelu, ogranicza wyniki do podanej ilości oraz zapisuje
# wynik w zmiennej kontekstowej
@register.tag
def get_objects(parser, token):
	"""
	Pobiera zbiór obiektów modelu określonego przez aplikację i nazwy modeli.
	Sposób użycia:
	{% get_objects [<manager>.]<method> from <app_name>.<model_name> [limit <amount>] as <var_name> %}
	Przykład:
	{% get_objects latest_published from people.Person limit 3 as people %}
	{% get_objects site_objects.all from articles.Article limit 3 as articles %}
	{% get_objects site_objects.all from articles.Article as articles %}
	"""
	amount = None
	try:
		tag_name, manager_method, str_from, appmodel, str_limit, amount, str_as, var_name = token.split_contents()
	except ValueError:
		try:
			tag_name, manager_method, str_from, appmodel, str_as, var_name = token.split_contents()
		except ValueError:
			raise (
				template.TemplateSyntaxError,
				"Znacznik get_objects ma następującą składnię: "
				"{% get_objects [<manager>.]<method> from <app_name>.<model_name> [limit <amount>] as <var_name> %}")
	try:
		app_name, model_name = appmodel.split(".")
	except ValueError:
		raise (template.TemplateSyntaxError, "Znacznik get_objects wymaga nazwy aplikacji i modelu rozdzielonych kropką.")
	model = apps.get_model(app_name, model_name)
	return ObjectsNode(model, manager_method, amount, var_name)


class ObjectsNode(template.Node):
	def __init__(self, model, manager_method, amount, var_name):
		self.model = model
		self.manager_method = manager_method
		self.amount = amount
		self.var_name = var_name

	def render(self, context):
		if "." in self.manager_method:
			manager, method = self.manager_method.split(".")
		else:
			manager = "_default_manager"
			method = self.manager_method
			qs = getattr(
				getattr(self.model, manager),
				method,
				self.model._default_manager.none,
			)()
		if self.amount:
			amount = template.resolve_variable(self.amount, context)
			context[self.var_name] = qs[:amount]
		else:
			context[self.var_name] = qs
		return ""


# In html
# {% load utility_tags %}
# {% get_objects all from news.Article limit 5 as latest_articles %}
# {% for article in latest_articles %}
# 	<a href="{{ article.get_url_path }}">{{ article.title }}</a>
# {% endfor %}

# or

# {% get_objects custom_manager.random_published from artists.Artist limit 1 as random_artists %}
# {% for artist in random_artists %}
# 	{{ artist.first_name }} {{ artist.last_name }}
# {% endfor %}




# Znacznik do przetwarzania treści jako szablonu
# ==============================================
@register.tag
def parse(parser, token):
	"""
	Przetwarza wartość jako szablon i ją drukuje lub zapisuje w zmiennej.
	Sposób użycia:
	{% parse <template_value> [as <variable>] %}
	Przykłady:
	{% parse object.description %}
	{% parse header as header %}
	{% parse "{{ MEDIA_URL }}js/" as js_url %}
	"""
	bits = token.split_contents()
	tag_name = bits.pop(0)
	try:
		template_value = bits.pop(0)
		var_name = None
		if len(bits) == 2:
			bits.pop(0) # usuń słowo „as”
			var_name = bits.pop(0)
	except ValueError:
		raise (template.TemplateSyntaxError, "Znacznik parse ma następującą składnię: {% parse <template_value> [as <variable>] %}")
	return ParseNode(template_value, var_name)


class ParseNode(template.Node):
	def __init__(self, template_value, var_name):
		self.template_value = template_value
		self.var_name = var_name

	def render(self, context):
		template_value = template.resolve_variable(self.template_value, context)
		t = template.Template(template_value)
		context_vars = {}
		for d in list(context):
			for var, val in d.items():
				context_vars[var] = val
		result = t.render(template.RequestContext(context['request'], context_vars))
		if self.var_name:
			context[self.var_name] = result
			return ""
		return result


# 1) Jeśli mamy obiekt z polem description, które może zawierać zmienne szablonowe lub logikę,
# to możemy go przetwarzać i renderować przy użyciu poniższego kodu:
# {% load utility_tags %}
# {% parse object.description %}

# 2) Można też zdefiniować wartość do przetworzenia przy użyciu łańcucha w cudzysłowie:
# {% load utility_tags %}
# {% parse "{{ STATIC_URL }}site/img/" as img_path %}
# <img src="{{ img_path }}someimage.png" alt="" />
