import io

import matplotlib
matplotlib.use('Agg')
matplotlib.rc('font', family='Comic Sans MS')
import matplotlib.pyplot as plt

from django.http import HttpResponse


class PlotGraph:
	""" 
		Class creates matplotlib graph and appropriate django response

		:param data_frama: Data for graph
		:type data_frame: Pandas DataFrame object
		:param title: Graph title
		:type title: 'str', default value set to 'graph'
		:param x_label: Label name for x's
		:type x_label: 'str', default value set to 'X'
		:param y_label: Label name for y's
		:type y_label: 'str', default value set to 'Y'
		:param extension: Extension for created file
		:type extension: 'str', default value set to 'svg'
		:param style: Matplotlib pyplot style, matplotlib.style.available for more examples
		:type style: 'str', default value set to 'seaborn-dark-palette'
    """

	def __init__(self, data_frame, title='graph', x_label='X', y_label='Y', extension='svg', style='seaborn-dark-palette'):
		self.data_frame = data_frame
		self.title = title
		self.x_label = x_label
		self.y_label = y_label
		self.extension = extension
		self.style = style
		self.content_type = {'pdf': 'application/pdf', 'svg': 'image/svg+xml', 'png': 'image/png'}.get(self.extension)
		self.create_graph()

	def create_graph(self):
		""" Function creates matplotlib graph from self.data_frame """

		with plt.style.context((self.style)):
			for i in range(1, len(self.data_frame.columns)):
				plt.plot(self.data_frame[self.data_frame.columns[0]], self.data_frame[self.data_frame.columns[i]], label=self.data_frame.columns[i])

		plt.xlabel(self.x_label)
		plt.ylabel(self.y_label)
		plt.title(self.title.capitalize())
		plt.grid(True)
		plt.legend()
		plt.tight_layout()
		
	def create_response(self):
		""" Function creates django response with matplotlib graph """

		f = io.BytesIO()
		plt.savefig(f, format=self.extension)
		plt.clf()
		plt.close()
		response = HttpResponse(f.getvalue(), content_type=self.content_type)
		response['Content-Disposition'] = 'attachment; filename=graph.{0}'.format(self.extension)
		return response