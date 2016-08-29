# Każdy piksel jest obliczany przez zastosowanie pętli, która
# może być wykonywana nieokreśloną liczbę razy.

# Współrzędne powodujące niewiele iteracji mają ciemny kolor. Z kolei współrzędne,
# które powodują dużą liczbę iteracji, mają biały kolor.


"""Generator zbioru Julii z rysowaniem obrazów na bazie biblioteki PIL"""
import time
from PIL import Image
# obszar przestrzeni zespolonej do przeanalizowania
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
# c_real, c_imag = -0.62772, -.42193
# c_real, c_imag = -0.835, -0.2321			# dragon
# c_real, c_imag = 0.0523, 0.65  			# snowflake
c_real, c_imag = 0.285, 0.01				# snail

def calc_pure_python(desired_width, max_iterations):
	"""Tworzenie listy współrzędnych zespolonych (zs) i parametrów
	zespolonych (cs), budowanie zbioru Julii i wyświetlanie danych"""
	x_step = (float(x2 - x1) / float(desired_width))
	y_step = (float(y1 - y2) / float(desired_width))
	x = []
	y = []
	ycoord = y2
	while ycoord > y1:
		y.append(ycoord)
		ycoord += y_step
	xcoord = x1
	while xcoord < x2:
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
			cs.append(complex(c_real, c_imag))
	print("Długość dla x:", len(x))
	print("Łączna liczba elementów:", len(zs))
	start_time = time.time()
	output = calculate_z_serial_purepython(max_iterations, zs, cs)
	end_time = time.time()
	secs = end_time - start_time
	print("Działanie funkcji " + calculate_z_serial_purepython.__name__ + " trwało", secs, "s")
	# Suma ta jest oczekiwana dla siatki 1000^2 z 300 iteracjami
	# Przechwytywane są drobne błędy, które mogą się pojawić
	# podczas przetwarzania ustalonego zbioru wejść
	# assert sum(output) == 33219980
	return output 

def calculate_z_serial_purepython(maxiter, zs, cs):
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

def draw_image(values_list):
	img = Image.new('RGB', (3000, 3000), 'black')
	pixel_map = img.load()

	for i in range(img.size[0]):
		for j in range(img.size[1]):
			value = values_list[3000*i+j]
			color = int((255/300)*value)
			pixel_map[i, j] = (color, color, color)

	img.save('fractal.bmp')
	img.close()


# 0, 0, 0 - black
# 255, 255, 255 - white

if __name__ == "__main__":
	# Obliczanie zbioru Julii za pomocą czystego rozwiązania opartego na języku Python
	# z wykorzystaniem wartości domyślnych rozsądnych dla laptopa
	values_list = calc_pure_python(desired_width=3000, max_iterations=255)
	draw_image(values_list)

