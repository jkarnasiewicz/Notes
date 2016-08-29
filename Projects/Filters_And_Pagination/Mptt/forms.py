from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.html import mark_safe

from mptt.forms import TreeNodeChoiceField

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap

from .models import Category, Movie


class MovieFilterForm(forms.Form):
	category = TreeNodeChoiceField(
		label=_("Category"),
		queryset=Category.objects.all(),
		required=False,
		level_indicator=mark_safe("&nbsp;&nbsp;&nbsp;&nbsp;"),
	)


class MultipleChoiceTreeField(forms.ModelMultipleChoiceField):
	widget = forms.CheckboxSelectMultiple

	# Gdy potrzebujemy innych własności kategorii, nie tylko wartości wyboru i tekstu wyboru,
	# możemy przesłonić metodę label_from_instance, która zwraca samą kategorię, a nie tylko
	# jej reprezentację Unicode
	def label_from_instance(self, obj):
		return obj


class MovieForm(forms.ModelForm):
	categories = MultipleChoiceTreeField(
		label=_("Kategorie"),
		required=False,
		queryset=Category.objects.all())

	class Meta:
		model = Movie
		exclude = ['created', 'modified']

	def __init__(self, *args, **kwargs):
		super(MovieForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_action = ""
		self.helper.form_method = "POST"
		self.helper.layout = layout.Layout(
			layout.Field("title"),
			layout.Field(
				"categories",
				template="Mptt/checkbox_select_multiple_tree.html"),
			bootstrap.FormActions(
				layout.Submit("submit", _("Zapisz")),
			)
		)
