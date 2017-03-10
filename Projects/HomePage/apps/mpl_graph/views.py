from django.shortcuts import render

from .forms import PlotForm


class Plot:

	def __init__(self, name='graph', file=None, formula=None, random=None, colors=None, extension='.pdf'):
		pass


def mpl_graph(request):
	ctx = {'form': PlotForm(data=request.POST or None, files=request.FILES or None)}
	if request.method == 'POST':
		print(request.POST, request.FILES)
		print(ctx['form'].is_valid())
		# print(ctx['form'].cleaned_data['file'].read())

	return render(request, 'mpl_graph/home.html', ctx)
