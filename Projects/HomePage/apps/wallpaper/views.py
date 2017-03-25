from django.shortcuts import render

from .forms import WallpaperForm

from django.http import FileResponse

from django.template.loader import render_to_string

def wallpaper(request):
	form = WallpaperForm(data=request.POST or None)
	if request.method == 'POST' and form.is_valid():

		# response = FileResponse(open('static/images/jumbotron.png', 'rb'))
		# return StreamingHttpResponse(stream_response_generator())
		# return response
		return StreamingHttpResponse(img(request, form, form.cleaned_data.get('search')))
	return render(request, 'wallpaper/home.html', {'form': form})




from concurrent.futures import ThreadPoolExecutor
import os
import time
import base64

from django.http import HttpResponse, StreamingHttpResponse


def img(request, form, keyword):
	# a = '23432'
	yield render_to_string('wallpaper/head.html', request=request, context={'form': form})
	import requests
	import re
	from random import sample
	# response = requests.get('https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-499207.jpg').content

	# a = open('static/images/jumbotron.png', 'rb')
	# data = base64.b64encode(a.read()).decode('ascii')


	# response = requests.get('https://alpha.wallhaven.cc/random').text
	response = requests.get('https://alpha.wallhaven.cc/search?q={0}&purity=100&resolutions=1920x1080&sorting=relevance&order=desc&page=1'.format(keyword)).text

	# data = re.findall('<a class="preview" href="https://alpha.wallhaven.cc/wallpaper/(.+?)"\s{0,2}?target="_blank"', response)
	data = re.findall('data-src="https://alpha.wallhaven.cc/wallpapers/thumb/small/th-(.+?)" src=', response)
	print(data)
	try:
		data = sample(data, 5)
	except ValueError:
		pass
	print(data)


	for index in data:
		response = requests.get('https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-{}'.format(index)).content
		data = base64.b64encode(response)
		# print(data)
		data = data.decode('ascii')
		# print(data)

		yield """<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12 app_thumbnail">
			<div class="thumbnail">
				<img alt="100%x200" style="height: 500px; width: 100%; display: block;" src="data:image/jpg;base64,{0}" data-holder-rendered="true">
			</div>
		</div>""".format(data)
















	# # time.sleep(5)
	# # yield open('static/images/jumbotron_blue.png', 'rb')
	# a = open('static/images/jumbotron_blue.png', 'rb')
	# # data = base64.encodebytes(a.read()).decode('ascii')
	# # data = base64.urlsafe_b64encode(a.read()).decode('ascii')
	# data = base64.b64encode(a.read()).decode('ascii')
	

	# yield """<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12 app_thumbnail">
	# 	<div class="thumbnail">
	# 		<img alt="100%x200" style="height: 400px; width: 100%; display: block;" src="data:image/png;base64,{0}" data-holder-rendered="true">
	# 	</div>
	# </div>""".format(data)


	yield render_to_string('wallpaper/footer.html', request=request, context={'form': form})


# def home(request):
#     return StreamingHttpResponse(stream_response_generator())
    # return StreamingHttpResponse(stream_response_generator_with_threads())


# def stream_response_generator():
# 	pool = ThreadPoolExecutor(8)

# 	for root, dirs, files in os.walk(os.path.dirname(__file__)):
# 		for fname in filter(lambda f: f.endswith('.py'), files):
# 			document = open(os.path.join(root, fname), mode='rt', encoding='utf-8')
# 			yield "<h1>Next File: {}</h1>".format(fname)

# 			# save element to db
# 			future = pool.submit(func, 2, 3)
# 			yield '<h1>{}</h1>'.format(future.result())

# 			for row in document:
# 				# yield "<p>{}</p><br>".format(row)
# 				yield "{}<br>".format(row)

# def func(x, y):
# 	print('FUNC')
# 	time.sleep(3)
# 	return x + y
