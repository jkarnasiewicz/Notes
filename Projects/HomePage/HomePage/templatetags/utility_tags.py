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
	# print(field.field.widget, dir(field.field.widget), sep='\n')
	# print(field.field.widget.input_type, dir(field.field.widget), sep='\n')
	template = 'template_forms/form_field.html'
	ctx = {
		'field': field,
		'input_type': field.field.widget.input_type,
	}
	return mark_safe(render_to_string(template, ctx))
	# return ''
