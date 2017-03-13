from django import forms


class PlotForm(forms.Form):
	file = forms.FileField(
		required=False,
		max_length=256,
		label='Plot from file',
		help_text='Try selecting one or more files and watch the feedback')
	custom_pattern = forms.CharField(
		required=False,
		max_length=64,
		label='Plot from custom pattern (e.g. x**2 - 6*x + 5)',
		help_text='Have fun and good luck')
	min_value = forms.FloatField(
		required=False,
		label='Min value of x',
		widget=forms.NumberInput(attrs={'placeholder': 'Default value is -100'}),
		min_value=-10000000,
		max_value=10000000)
	max_value = forms.FloatField(
		required=False,
		label='Max value of x',
		widget=forms.NumberInput(attrs={'placeholder': 'Default value is 100'}),
		min_value=-10000000,
		max_value=10000000)
	step = forms.FloatField(
		required=False,
		widget=forms.NumberInput(attrs={'placeholder': 'Default value is 0.1', 'step': 0.001}),
		min_value=0.001,
		max_value=10)
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
