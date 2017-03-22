from io import BytesIO

from PIL import Image

from django.http import HttpResponse
from django.shortcuts import render

from .forms import JuliaSetForm


class GenerateJuliaSet:
	"""
		Each pxel is calculated in loop, which can be run unknown amount of times
		Każdy piksel jest obliczany przez zastosowanie pętli, która
		może być wykonywana nieokreśloną liczbę razy

		Coordinates with few iterations have darker color, on the other hand coordinates
		with many iterations have white color
		Współrzędne powodujące niewiele iteracji mają ciemny kolor. Z kolei współrzędne,
		które powodują dużą liczbę iteracji, mają biały kolor
	"""
	examples = {'fern': (-0.62772, -0.42193), 'snowflake': (0.0523, 0.65), 'snail': (0.285, 0.01), 'cracks': (0, -0.8)}

	def __init__(self, real_part, imaginary_part, width=1000, max_iterations=255,  sample=None):
		# obszar przestrzeni zespolonej do przeanalizowania
		self.x1, self.x2, self.y1, self.y2 = -1.8, 1.8, -1.8, 1.8
		self.real_part = real_part
		self.imaginary_part = imaginary_part
		self.width = width
		self.max_iterations = max_iterations
		if sample:
			coordinates = GenerateJuliaSet.examples.get(sample, None)
			if coordinates:
				self.real_part, self.imaginary_part = coordinates

		self.values_list = self.calculate_coordinates(width, max_iterations)

	def calculate_coordinates(self, width, max_iterations):
		"""Tworzenie listy współrzędnych zespolonych (zs) i parametrów
		zespolonych (cs), budowanie zbioru Julii i wyświetlanie danych"""
		x_step = (float(self.x2 - self.x1) / float(width))
		y_step = (float(self.y1 - self.y2) / float(width))
		x = []
		y = []
		ycoord = self.y2
		while ycoord > self.y1:
			y.append(ycoord)
			ycoord += y_step
		xcoord = self.x1
		while xcoord < self.x2:
			x.append(xcoord)
			xcoord += x_step
			# Utwórz listę współrzędnych i warunek początkowy dla każdej komórki
			# Zauważ, że warunek początkowy to stała, która z łatwością może zostać usunięta
			# Stała służy do symulowania rzeczywistego scenariusza z kilkoma wejściami
			# przekazanymi przykładowej funkcji
		zs = []
		cs = []
		for ycoord in y:
			for xcoord in x:
				zs.append(complex(xcoord, ycoord))
				cs.append(complex(self.real_part, self.imaginary_part))

		output = self.calculate_z_serial(max_iterations, zs, cs)
		# Suma ta jest oczekiwana dla siatki 1000^2 z 300 iteracjami
		# Przechwytywane są drobne błędy, które mogą się pojawić
		# podczas przetwarzania ustalonego zbioru wejść
		# assert sum(output) == 33219980
		return output 

	def calculate_z_serial(self, maxiter, zs, cs):
		"""Obliczanie listy output przy użyciu reguły aktualizacji zbioru Julii"""
		output = [0] * len(zs)
		for i in range(len(zs)):
			n = 0
			z = zs[i]
			c = cs[i]
			while abs(z) < 2 and n < maxiter:
				z = z * z + c
				n += 1
			output[i] = n
		return output

	def create_response(self):
		img = Image.new('RGB', (self.width, self.width), 'black')
		pixel_map = img.load()

		for i in range(img.size[0]):
			for j in range(img.size[1]):
				value = self.values_list[self.width*i+j]
				color = int((255/self.max_iterations)*value)
				print(color)
				pixel_map[i, j] = (color, color, color)

		f = BytesIO()
		img.save(f, format='BMP')

		response = HttpResponse(f.getvalue(), content_type='image/bmp')
		response['Content-Disposition'] = 'attachment; filename=fractal(real_{})(imag_{}).bmp'.format(self.real_part, self.imaginary_part)
		return response




def julia_set(request):
	form = JuliaSetForm(data=request.POST or None)
	if request.method == 'POST' and form.is_valid():
		response = GenerateJuliaSet(
			real_part=form.cleaned_data['real_part'],
			imaginary_part=form.cleaned_data['imaginary_part'],
			width=form.cleaned_data['width'],
			max_iterations=form.cleaned_data['max_iterations'],
			sample=form.cleaned_data['sample']).create_response()
		return response
	return render(request, 'julia_set/home.html', {'form': form})
