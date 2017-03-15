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
		min_value=-1000000,
		max_value=1000000)
	max_value = forms.FloatField(
		required=False,
		label='Max value of x',
		widget=forms.NumberInput(attrs={'placeholder': 'Default value is 100'}),
		min_value=-1000000,
		max_value=1000000)
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
	title = forms.CharField(
		required=False,
		max_length=32,
		label='Title of the graph and file name',
		widget=forms.TextInput(attrs={'placeholder': 'Default title is "graph"'}))

	def clean_title(self):
		title = self.cleaned_data['title']
		if title:
			return title
		title = 'graph'
		return title

	def clean_min_value(self):
		min_value = self.cleaned_data.get('min_value')
		if min_value:
			return min_value
		min_value = -100
		return min_value

	def clean_max_value(self):
		max_value = self.cleaned_data.get('max_value')
		if max_value:
			return max_value
		max_value = 100 # FROM INITIAL VALUE! FADING WARRNINGS
		return max_value

	def clean_step(self):
		step = self.cleaned_data.get('step')
		if step:
			return step
		step = 0.1
		return step		

	def clean(self):
		cleaned_data = super(PlotForm, self).clean()
		# print('asdas!!!', cleaned_data['file'], cleaned_data['custom_pattern'], cleaned_data['random'])
		# if not cleaned_data['file'] and not cleaned_data['custom_pattern'] and not cleaned_data['random']:
		# 	pass
		# 	# TO DO
		# return cleaned_data
		import math
		import numpy as np
		import pandas as pd
		random = cleaned_data.get('random')
		custom_pattern = cleaned_data.get('custom_pattern')
		file = cleaned_data.get('file')

		min_value = cleaned_data.get('min_value')
		max_value = cleaned_data.get('max_value')
		step = cleaned_data.get('step')


		eval_globals = {"__builtins__": None}
		eval_locals = {func: getattr(math, func) for func in dir(math) if not func.startswith('__')}
		if random:
			x_range = np.arange(np.random.randint(-100, 0), np.random.randint(0, 100), np.random.choice((0.1, 0.01, 1)))
			sample_functions = np.random.choice((
				'0.5*x - 4',
				'-x**2 + 7*x + 12',
				'5*sin(0.5*x)',
				'floor(x)',
				'tanh(x)',
				'0.5*exp(x) - 7',
				'cosh(x)',
				'-sqrt(sqrt(fabs(x)))'))
			y = (eval(sample_functions, eval_globals, eval_locals) for x in x_range if not eval_locals.update({'x': x}))
			df = pd.DataFrame(data=list(zip(x_range, y)), columns=['X', sample_functions])
			# self.data_frame = df
		elif custom_pattern:
			x_range = np.arange(min_value, max_value + step, step)
			y = (eval(custom_pattern, eval_globals, eval_locals) for x in x_range if not eval_locals.update({'x': x}))
			df = pd.DataFrame(data=list(zip(x_range, y)), columns=['X', custom_pattern])
			# self.data_frame = df
		elif file:
			df = pd.read_csv(file)			
		else:
			raise forms.ValidationError('Please choose one plotting option, "file", "custom pattern" or "random" option.')

		self.data_frame = df
		return cleaned_data
