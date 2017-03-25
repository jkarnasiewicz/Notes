from django import forms


class WallpaperForm(forms.Form):
	search_phrase = forms.CharField(
		required=False,
		max_length=64)
	random = forms.BooleanField(
		required=False,
		label='<span class="glyphicon glyphicon-alert" aria-hidden="true"></span> Random')
