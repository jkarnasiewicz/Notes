from django.shortcuts import render

from .forms import PlotForm


class Plot:

	def __init__(self, name='graph', file=None, formula=None, random=None, colors=None, extension='.pdf'):
		pass


def mpl_graph(request):
	ctx = {'form': PlotForm(data=request.POST or None, files=request.FILES or None)}
	if request.method == 'POST':
		# form = PlotForm(data=request.POST, files=request.FILES)
		# if form.is_valid():
		if ctx['form'].is_valid():
			# print(request.POST, request.FILES)
			# print(ctx['form'].is_valid())
			# print(ctx['form'].cleaned_data['file'].read())
			# ctx['form'] = PlotForm()
			return get_image(file=ctx['form'].cleaned_data['file'])
	# else:
	# 	form = PlotForm()

	# return render(request, 'mpl_graph/home.html', {'form': form})
	return render(request, 'mpl_graph/home.html', ctx)

# 	ONLY GET!
# def generate_graph(request):
# 	ONLY POST!





from django.http import HttpResponse, HttpResponseRedirect
import matplotlib
matplotlib.use('Agg')
matplotlib.rc('font', family='Comic Sans MS')

import matplotlib.pyplot as plt

# print(plt.style.available)
styles = ['bmh', 'classic', 'dark_background', 'fivethirtyeight', 'ggplot', 'grayscale',
 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark',
 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper',
 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn']
plt.style.use(styles[8])
# 0, 1, 8
import numpy as np
from numpy.random import rand
import io

def get_image(file):

	# plt.figure(1)
	# plt.subplot(211)
	# N = 50
	# x = np.random.rand(N)
	# y = np.random.rand(N)
	# colors = np.random.rand(N)
	# area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses
	# plt.scatter(x, y, s=area, c=colors, alpha=0.5)

	# plt.subplot(212)
	# t = np.arange(0.0, 2.0, 0.01)
	# s = 1 + np.sin(2*np.pi*t)
	# plt.plot(t, s)

	# t = np.arange(0.0, 2.0, 0.01)
	# s = 1 + np.sin(1/2*np.pi*t)
	# plt.plot(t, s)

	# t = np.arange(0.0, 100.0, 0.01)
	# s = -3*t + 2
	# plt.plot(t, s)

	# t = np.arange(0.0, 100.0, 0.01)
	# s = t**2 + 5*t + 6
	# plt.plot(t, s)
	# print(dir(file.file))
	# print(file.file.read())
	x, y = [], []
	for i in file.readlines():
		row = i.decode('utf-8').strip().split(', ')
		x.append(int(row[0]))
		y.append(int(row[1]))
		
	plt.plot(x, y)
	# with open(file.file.read(), mode='rt', encoding='utf-8') as f:
	# 	print(f)
	# import csv
	# with open(file, newline='') as csv_file:
	# with open(file, mode='rb') as f:
	# for row in csv.reader(file.read(), delimiter=','):
	# 	print(row)

	# with open(file, 'wb+') as destination:
	# 	for chunk in f.chunks():
	# 		# destination.write(chunk)
	# 		print(chunk)

	plt.xlabel('time (s)')
	plt.ylabel('voltage (mV)')
	plt.title('About as simple as it gets, folks')
	plt.grid(True)
	"""
	Now the redirect into the cStringIO or BytesIO object >>>
	"""
	f = io.BytesIO()
	plt.savefig(f, format="svg", facecolor=(0.95,0.95,0.95))
	plt.clf()
	plt.close()
	"""
	Add the contents of the StringIO or BytesIO object to the response, matching the
	mime type with the plot format (in this case, PNG) and return >>>
	"""
	# response = HttpResponse(f.getvalue(), content_type='application/pdf')
	# response['Content-Disposition'] = 'attachment; filename=graph.pdf'
	response = HttpResponse(f.getvalue(), content_type="image/svg+xml")
	# response = HttpResponse(f.getvalue(), content_type="image/png")
	response['Content-Disposition'] = 'attachment; filename=graph.svg'
	return response


	# return HttpResponse(f.getvalue(), content_type="image/png")
