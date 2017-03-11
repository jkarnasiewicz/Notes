from django import forms


class PlotForm(forms.Form):
	file = forms.FileField(
		required=False,
		max_length=256,
		label='Plot from file',
		help_text='Try selecting one or more files and watch the feedback')
	custom_pattern = forms.CharField(
		required=False,
		max_length=256,
		label='Plot from custom pattern (e.g. f(x) = x**2 - 6*x + 5, f(x, y) = x**2 + y**2)',
		help_text='Have fun and good luck')
	random = forms.BooleanField(
		required=False,
		label='Plot from random data')
	extension = forms.ChoiceField(
		required=True,
		initial='svg',
		label='Choose file format of the graph (extension)',
		choices=(('pdf', 'pdf'), ('svg', 'svg'), ('png', 'png')),
		widget=forms.RadioSelect)
	style = forms.ChoiceField(
		required=True,
		initial='seaborn-dark-palette',
		label='Choose matplotlib(pyplot) style',
		choices=(('bmh', 'bmh'), ('classic', 'classic'), ('seaborn-dark-palette', 'seaborn-dark-palette')),
		widget=forms.RadioSelect)

	def clean(self):
		cleaned_data = super(PlotForm, self).clean()
		# print('asdas!!!', cleaned_data['file'], cleaned_data['custom_pattern'], cleaned_data['random'])
		if not cleaned_data['file'] and not cleaned_data['custom_pattern'] and not cleaned_data['random']:
			pass
			# TO DO
		return cleaned_data
