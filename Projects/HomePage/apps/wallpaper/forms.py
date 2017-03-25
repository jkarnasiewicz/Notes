from django import forms


class WallpaperForm(forms.Form):
	search = forms.CharField(
		required=False,
		max_length=64,
		label='')
