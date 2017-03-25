from django.shortcuts import render

from .forms import WallpaperForm

from django.http import JsonResponse 

from django.template.loader import render_to_string

def wallpaper(request):
	form = WallpaperForm(data=request.POST or None)
	if request.method == 'POST' and form.is_valid():
		return StreamingHttpResponse(img(request, form, form.cleaned_data.get('search_phrase'), form.cleaned_data.get('random')))
	return render(request, 'wallpaper/home.html', {'form': form})


# from concurrent.futures import ThreadPoolExecutor
from concurrent import futures
import os
import time
import base64

from django.http import HttpResponse, StreamingHttpResponse
import requests
import re
from random import sample

def img(request, form, search_phrase, random=None):
	yield render_to_string('wallpaper/head.html', request=request, context={'form': form})

	if random:
		response = requests.get('https://alpha.wallhaven.cc/random?page=2').text
	else:
		response = requests.get('https://alpha.wallhaven.cc/search?q={0}&purity=100&resolutions=1920x1080&sorting=relevance&order=desc&page=1'.format(search_phrase)).text

	data = re.findall('data-src="https://alpha.wallhaven.cc/wallpapers/thumb/small/th-(.+?)" src=', response)
	# try:
	# 	data = sample(data, 8)
	# except ValueError:
	# 	pass


	# Creating 8 workers
	pool = futures.ThreadPoolExecutor(len(data))				# ProcessPoolExecutor(os.cpu_count())

	to_do_list = []
	for index in data:
		# submit schedules the callable to be executed, and returns a future representing this pending operation
		future = pool.submit(make_html, index)
		to_do_list.append(future)

	# result = []
	# as_completed yields futures as they are completed
	for future in futures.as_completed(to_do_list):
		yield future.result()
		# res = future.result()
		# result.append(res)

	# for index in data:
	# 	_, extension = index.split('.')
	# 	response = requests.get('https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-{}'.format(index)).content
	# 	# check extension here
	# 	data = base64.b64encode(response)
	# 	data = data.decode('ascii')
	# 	if 'PGh' in data:
	# 		# broken pictures ?!
 # 			continue

	# 	# yield """<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12 app_thumbnail">
	# 	# 	<div class="thumbnail">
	# 	# 		<img alt="100%x200" style="height: 500px; width: 100%; display: block;" src="data:image/{0};base64,{1}" data-holder-rendered="true">
	# 	# 	</div>
	# 	# </div>""".format(extension, data)
	# 	yield """<div class="col-sm-6 col-md-4 col-lg-4 app_thumbnail">
	# 		<div class="thumbnail">
	# 			<img data-src="" alt="100%x200" style="height: 200px; width: 100%; display: block;" src="data:image/{0};base64,{1}" data-holder-rendered="true">
	# 		</div>
	# 	</div>""".format(extension, data)

	# yield render_to_string('wallpaper/footer.html', request=request, context={'form': form})
	yield render_to_string('wallpaper/footer.html')



def make_html(index):
	_, extension = index.split('.')
	response = requests.get('https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-{}'.format(index)).content
	# check extension here
	data = base64.b64encode(response)
	data = data.decode('ascii')
	# if 'PGh' in data:
	# 	# broken pictures ?!
	# 		continue

	# yield """<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12 app_thumbnail">
	# 	<div class="thumbnail">
	# 		<img alt="100%x200" style="height: 500px; width: 100%; display: block;" src="data:image/{0};base64,{1}" data-holder-rendered="true">
	# 	</div>
	# </div>""".format(extension, data)
	return """<div class="col-xs-12 col-sm-6 col-md-4 col-lg-4 app_thumbnail">
		<div class="thumbnail">
			<img data-src="" alt="100%x200" style="height: 200px; width: 100%; display: block;" src="data:image/{0};base64,{1}" data-holder-rendered="true">
		</div>
	</div>""".format(extension, data)








# import os
# from concurrent import futures


# def wallpaper(request):
# 	form = WallpaperForm(data=request.POST or None)
# 	if request.method == 'POST' and form.is_valid() and request.is_ajax():
# 		template = convert_images(form.cleaned_data.get('search_phrase'), form.cleaned_data.get('random'))
# 		return JsonResponse({'template': template})
# 	return render(request, 'wallpaper/home.html', {'form': form})


# def convert_images(search_phrase, random=None):
# 	if random:
# 		response = requests.get('https://alpha.wallhaven.cc/random?page=2').text
# 	else:
# 		response = requests.get('https://alpha.wallhaven.cc/search?q={0}&purity=100&resolutions=1920x1080&sorting=relevance&order=desc&page=1'.format(search_phrase)).text
	

# 	data = re.findall('data-src="https://alpha.wallhaven.cc/wallpapers/thumb/small/th-(.+?)" src=', response)
# 	# try:
# 	# 	data = sample(data, 9)
# 	# except ValueError:
# 	# 	pass

# 	# Creating 8 workers
# 	# pool = futures.ThreadPoolExecutor(8)				# ProcessPoolExecutor(os.cpu_count())

# 	# to_do_list = []
# 	# for index in data:
# 	# 	# submit schedules the callable to be executed, and returns a future representing this pending operation
# 	# 	future = pool.submit(make_base64_image, index)
# 	# 	to_do_list.append(future)

# 	# result = []
# 	# # as_completed yields futures as they are completed
# 	# for future in futures.as_completed(to_do_list):
# 	# 	res = future.result()
# 	# 	result.append(res)

# 	with futures.ThreadPoolExecutor(len(data)) as executor:
# 		# create generator
# 		result = executor.map(make_base64_image, data)
		

# 	# result = []
# 	# for index in data:
# 	# 	_, extension = index.split('.')
# 	# 	response = requests.get('https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-{}'.format(index)).content
# 	# 	data = base64.b64encode(response)
# 	# 	result.append((extension, data.decode('ascii')))

# 	result = filter(bool, result)
# 	return render_to_string('wallpaper/search_results.html', context={'result': result})



# def make_base64_image(index):
# 	_, extension = index.split('.')
# 	response = requests.get('https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-{}'.format(index)).content
# 	data = base64.b64encode(response)
# 	data = data.decode('ascii')
# 	if 'PGh' in data:
# 		return None
# 	# print(extension, data[:10])
# 	return extension, data
