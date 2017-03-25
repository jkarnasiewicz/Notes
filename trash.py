# -*- coding: utf-8 -*-

# Fluent python
# check import order in metaprograming chapter
# 717 python jargon
# raise from lambda !

# ML/25
# JS/124

# End
# unittest module
# regexp



# ?! - annotation
# Tests
# try to not create database instances(no save()), try to focuse on full_clean()



# aplikacja 'zapytania'

# self.assertIn('__all__', form.errors)
# self.assertIn('Please correct min, max or step value.', form.errors['__all__'])
# Czy jest sens testować dosłowne wiaomości błędów?

# django forms
# ?! In cases when field validators detect error that clean_field is omitted
# błąd(niścisłość) w dokumentacji? 

# czy jest mozliwe dodać dodatkowe informacje podczas wysyłania HttpResponse z plikiem do ściągnięcia np. reset formularza?

# from PIL import Image, ImageChops

# img1 = Image.open('fractal.bmp')
# img2 = Image.open('fractal_2.bmp')

# img3 = ImageChops.add(img2, img1, 1, 0)
# img3.save('fractal_merge_3.bmp')

# RAZORHILL MUSIC

# from urllib.request import urlopen, urlretrieve
# url = 'https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-499207.jpg'

# # response = urlretrieve('https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-499207.jpg')
# response = urlopen('https://python.org')
# print(response)
# print(dir(response))

import requests
# response = requests.get('https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-499207.jpg')
# response = requests.get('https://alpha.wallhaven.cc/random').content
response = requests.get('https://alpha.wallhaven.cc/random').text

print(response)
# <a class="preview" href="https://alpha.wallhaven.cc/wallpaper/176854"  target="_blank"  >
import re
# data = re.findall('<a class="preview" href="https://alpha.wallhaven.cc/wallpaper/(.+?)"\s{0,2}?target="_blank"', response)
data = re.findall('data-src="https://alpha.wallhaven.cc/wallpapers/thumb/small/th-(.+?)" src=', response)
print(data)

# https://alpha.wallhaven.cc/wallpaper/183121
# https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-183121.jpg
