import io

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

	# def __init__(self, name='graph', file=None, file_headers=None, custom_pattern=None, random=None, extension='pdf', style='seaborn-dark-palette', colors=None):
	def __init__(self, name='graph', file=None, custom_pattern=None, random=None, extension='pdf', style='seaborn-dark-palette', colors=None):
		self.name = name
		self.file = file
		# self.file_headers = file_headers
		self.custom_pattern = custom_pattern
		self.random = random
		self.extension = extension
		self.style = style
		# self.colors = colors
		# self.graph = 
		self.data = self.create_data()
		self.content_type = {'pdf': 'application/pdf', 'svg': 'image/svg+xml', 'png': 'image/png'}.get(self.extension, None)
		self.create_graph()

	def create_data(self):
		if self.random:
			return None
		elif self.custom_pattern:
			# TO DO
			r = range(-10, 11, 0.1)
			# y = (eval(self.custom_pattern) for x in r)
			import math
			y = (eval(self.custom_pattern, {"__builtins__":None}, {'x':x, 'sin': math.sin}) for x in r)
			print(y)
			# import ast
			# y = (ast.literal_eval(self.custom_pattern) for x in r)
			df = pd.DataFrame(data=list(zip(r, y)), columns=['X', 'Y'])
			return df
		elif self.file:
			# # with headers
			# if self.file_headers:
			return pd.read_csv(self.file)
			# # no avaiable headers
			# return pd.read_csv(self.file, header=None)
		else:
			raise ValueError('Please supply Plot class with "file", "custom_pattern" or "random" value.')

	def create_graph(self):
		print(self.style)
		plt.style.use(self.style)

		for i in range(1, len(self.data.columns)):
			plt.plot(self.data[self.data.columns[0]], self.data[self.data.columns[i]], label=self.data.columns[i])

		plt.xlabel(self.data.columns[0])
		plt.ylabel(self.data.columns[1])
		plt.title(self.name.capitalize())
		plt.grid(True)
		plt.legend()
		plt.tight_layout()
		

	def create_response(self):
		f = io.BytesIO()
		plt.savefig(f, format=self.extension, facecolor=(0.95,0.95,0.95))
		plt.clf()
		plt.close()
		response = HttpResponse(f.getvalue(), content_type=self.content_type)
		response['Content-Disposition'] = 'attachment; filename={0}.{1}'.format(self.name, self.extension)
		return response


def mpl_graph(request):
	ctx = {'form': PlotForm(data=request.POST or None, files=request.FILES or None)}
	if request.method == 'POST':
		# form = PlotForm(data=request.POST, files=request.FILES)
		# if form.is_valid():
		if ctx['form'].is_valid():
			# # print(ctx['form'].cleaned_data['custom_pattern'])
			# # print(ctx['form'].cleaned_data['random'])
			# return get_image(file=ctx['form'].cleaned_data['file'])
			return Plot(name='graph',
						file=ctx['form'].cleaned_data['file'],
						# file_headers=ctx['form'].cleaned_data['file_headers'],
						custom_pattern=ctx['form'].cleaned_data['custom_pattern'],
						random=ctx['form'].cleaned_data['random'],
						extension=ctx['form'].cleaned_data['extension'],
						style=ctx['form'].cleaned_data['style']).create_response()
	# else:
	# 	form = PlotForm()

	# return render(request, 'mpl_graph/home.html', {'form': form})
	return render(request, 'mpl_graph/home.html', ctx)




# print(plt.style.available)
# styles = ['bmh', 'classic', 'dark_background', 'fivethirtyeight', 'ggplot', 'grayscale',
#  'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark',
#  'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper',
#  'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn']
# plt.style.use(styles[8])
# 0, 1, 8

# def get_image(file):

# 	# plt.figure(1)
# 	# plt.subplot(211)
# 	# N = 50
# 	# x = np.random.rand(N)
# 	# y = np.random.rand(N)
# 	# colors = np.random.rand(N)
# 	# area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses
# 	# plt.scatter(x, y, s=area, c=colors, alpha=0.5)

# 	# plt.subplot(212)
# 	# t = np.arange(0.0, 2.0, 0.01)
# 	# s = 1 + np.sin(2*np.pi*t)
# 	# plt.plot(t, s)

# 	# t = np.arange(0.0, 2.0, 0.01)
# 	# s = 1 + np.sin(1/2*np.pi*t)
# 	# plt.plot(t, s)

# 	# t = np.arange(0.0, 100.0, 0.01)
# 	# s = -3*t + 2
# 	# plt.plot(t, s)

# 	# t = np.arange(0.0, 100.0, 0.01)
# 	# s = t**2 + 5*t + 6
# 	# plt.plot(t, s)
# 	# print(dir(file.file))
# 	# print(file.file.read())
# 	# x, y = [], []
# 	# for i in file.readlines():
# 	# 	row = i.decode('utf-8').strip().split(', ')
# 	# 	x.append(int(row[0]))
# 	# 	y.append(int(row[1]))
	

# 	df = pd.read_csv(file)
# 	# plt.plot(df[df.columns[0]], df[df.columns[1]])
# 	plt.plot(df[df.columns])
# 	# with open(file.file.read(), mode='rt', encoding='utf-8') as f:
# 	# 	print(f)
# 	# import csv
# 	# with open(file, newline='') as csv_file:
# 	# with open(file, mode='rb') as f:
# 	# for row in csv.reader(file.read(), delimiter=','):
# 	# 	print(row)

# 	# with open(file, 'wb+') as destination:
# 	# 	for chunk in f.chunks():
# 	# 		# destination.write(chunk)
# 	# 		print(chunk)

# 	plt.xlabel(df.columns[0])
# 	plt.ylabel(df.columns[1])
# 	plt.title('About as simple as it gets, folks')
# 	plt.grid(True)
# 	"""
# 	Now the redirect into the cStringIO or BytesIO object >>>
# 	"""
# 	f = io.BytesIO()
# 	plt.savefig(f, format="svg", facecolor=(0.95,0.95,0.95))
# 	plt.clf()
# 	plt.close()
# 	"""
# 	Add the contents of the StringIO or BytesIO object to the response, matching the
# 	mime type with the plot format (in this case, PNG) and return >>>
# 	"""
# 	# response = HttpResponse(f.getvalue(), content_type='application/pdf')
# 	# response['Content-Disposition'] = 'attachment; filename=graph.pdf'
# 	response = HttpResponse(f.getvalue(), content_type="image/svg+xml")
# 	# response = HttpResponse(f.getvalue(), content_type="image/png")
# 	response['Content-Disposition'] = 'attachment; filename=graph.svg'
# 	return response


	# return HttpResponse(f.getvalue(), content_type="image/png")
