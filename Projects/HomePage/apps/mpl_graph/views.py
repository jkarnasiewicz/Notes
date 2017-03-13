import io
import math

import matplotlib
matplotlib.use('Agg')
matplotlib.rc('font', family='Comic Sans MS')
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand
import pandas as pd


from django.http import HttpResponse
from django.shortcuts import render

from .forms import PlotForm


class Plot:

	def __init__(self, name='graph', file=None, custom_pattern=None, min_value=-100, max_value=100, step=0.1, random=None, extension='pdf', style='seaborn-dark-palette'):
		self.name = name
		self.file = file
		self.custom_pattern = custom_pattern
		self.min_value = min_value if min_value is not None else -100
		self.max_value = max_value if max_value is not None else 100
		self.step = step if step is not None else 0.1
		self.random = random
		self.extension = extension
		self.style = style
		self.data = self.create_data()
		self.content_type = {'pdf': 'application/pdf', 'svg': 'image/svg+xml', 'png': 'image/png'}.get(self.extension)
		self.create_graph()

	def create_data(self):
		if self.random:
			x_range = np.arange(np.random.randint(-1000, 0), np.random.randint(0, 1000))
		elif self.custom_pattern:
			x_range = np.arange(self.min_value, self.max_value + self.step, self.step)
			eval_globals = {"__builtins__":None}
			eval_locals = {func: getattr(math, func) for func in dir(math) if not func.startswith('__')}
			y = (eval(self.custom_pattern, eval_globals, eval_locals) for x in x_range if not eval_locals.update({'x': x}))
			df = pd.DataFrame(data=list(zip(x_range, y)), columns=['X', 'Y'])
			return df
		elif self.file:
			return pd.read_csv(self.file)
		else:
			raise ValueError('Please supply Plot class with "file", "custom_pattern" or "random" value.')

	def create_graph(self):
		plt.style.use(self.style)

		for i in range(1, len(self.data.columns)):
			plt.plot(self.data[self.data.columns[0]], self.data[self.data.columns[i]], label=self.data.columns[i])


		# N = 50
		# x = np.random.rand(N)
		# y = np.random.rand(N)
		# colors = np.random.rand(N)
		# area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses
		# plt.scatter(x, y, s=area, c=colors, alpha=0.5)

		plt.xlabel(self.data.columns[0])
		plt.ylabel(self.data.columns[1])
		plt.title(self.name.capitalize())
		plt.grid(True)
		plt.legend()
		plt.tight_layout()
		

	def create_response(self):
		f = io.BytesIO()
		plt.savefig(f, format=self.extension)
		plt.clf()
		plt.close()
		response = HttpResponse(f.getvalue(), content_type=self.content_type)
		response['Content-Disposition'] = 'attachment; filename={0}.{1}'.format(self.name, self.extension)
		return response


def mpl_graph(request):
	ctx = {'form': PlotForm(data=request.POST or None, files=request.FILES or None)}
	if request.method == 'POST':
		if ctx['form'].is_valid():
			return Plot(name='graph',
						file=ctx['form'].cleaned_data['file'],
						custom_pattern=ctx['form'].cleaned_data['custom_pattern'],
						min_value=ctx['form'].cleaned_data['min_value'],
						max_value=ctx['form'].cleaned_data['max_value'],
						step=ctx['form'].cleaned_data['step'],
						random=ctx['form'].cleaned_data['random'],
						extension=ctx['form'].cleaned_data['extension'],
						style=ctx['form'].cleaned_data['style']).create_response()

	return render(request, 'mpl_graph/home.html', ctx)

# styles = ['bmh', 'classic', 'dark_background', 'fivethirtyeight', 'ggplot', 'grayscale',
#  'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark',
#  'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper',
#  'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn']

# plt.figure(figsize=(15, 10), dpi=300)
# plt.savefig(f, format=self.extension, facecolor=(0.95, 0.95, 0.95))
# df = pd.DataFrame(data=np.array(list(zip(r, y)), dtype='int64'), columns=['X', 'Y'])
