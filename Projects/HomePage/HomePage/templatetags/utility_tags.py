from django import template
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def attr_list(obj):
	'''
	In templates
	{% load utility_tags %}
	{% attr_list object_to_inspect %}
	'''
	html = ''
	for item in dir(obj):
		if not item.startswith('__'):
			html += '<p>{0}</p>'.format(item)
	return mark_safe(html)


@register.simple_tag
def form_field(field, *args, **kwargs):
	# print(field.field.__class__.__name__)
	# print(field.field.widget)
	# from pprint import pprint
	# print(field.field.widget.__class__.__name__)
	# pprint(dir(field.field))
	# pprint(field.field.widget.build_attrs())
	# print(field.field.widget.input_type, dir(field.field.widget), sep='\n')

	template = 'forms/form_field.html'
	ctx = {
		'field': field,
	}

	field_type = field.field.widget.__class__.__name__
	if field_type in ('TextInput', 'URLInput'):
		ctx['input_type'] = field.field.widget.input_type
	elif field_type in ('Textarea', ):
		ctx['textarea'] = True
	elif field_type in ('Select', ):
		ctx['select'] = True

	
	return mark_safe(render_to_string(template, ctx))
