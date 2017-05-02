# -*- coding: utf-8 -*-

# Fluent python
# check import order in metaprograming chapter
# 717 python jargon
# raise from lambda !

# ML/25
# JS/387

# Testing JavaScript:
# jsHint
# QUnit
# Modernizr.load - feature detection(e.g. browser)
# math.js/accounting.js/numbers.js - mathematics
# Minify Your Library

# Manage browser differences for object support:
# Polyfill
# Paul Miller’s ES 6 Shim
# Google’s Traceur

# Worker threads/concurrency
# var worker = new Worker("loading.js");



# AMD - Asynchronous Module Definition

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

# jak prawidłowo 'renderować' pliki javascript (var name = {% var %}; => but you can replace that from js)?

# chcialbym przyspieszyc testy, poprzez uzycie mockow, czy to ma sens w przypadku gdy testujemy zewnetrzne zrodlo?
# Mockowe testy przejda szybko i pomyslnie lecz aplikacja bedzie chodzic blednie



# Algorytm deterministyczny – algorytm, którego działanie jest całkowicie zdeterminowane przez warunki początkowe (wejście).
# Oznacza to, że kilkukrotne uruchomienie takiego algorytmu doprowadzi za każdym razem do takiego samego wyniku.
# Algorytmy deterministyczne stanowią główny obszar badań informatycznych i są najczęściej stosowane, ponieważ mogą być
# łatwo realizowane na współczesnych komputerach.


# RAZORHILL MUSIC
# Stop making scv-s from one base at 22

# django channels with simple customized authentication
# SQLite
# Kivy



# Dodge Challenger and Mclaren P1 in wallpapers app

# (.*) 	-> Greedy!
# /[^crnld]ope/							// any character but those within brackets range
# (?m)
# reference substitution, r'\1 \2'

# (?=expression)  : Look Ahead
# (?<=expression) : Look Behind

# (?!expression)  : Negative Look Ahead
# (?<!expression) : Negative Look Behind



import re
# print(re.sub("/Filmy", "j", "/Filmyk"))

# regexp = re.compile('[\w_%+.-]{1,20}@[\w.-]{2,20}\.[a-zA-Z]{2,3}')

# print(re.search(regexp,'asd@wp.pl'))

# rand_str = 'https://www.youtube.com http://www.google.com'
# regex = re.compile(r'https?://([\w.]*)')

# print(re.sub(regex, r'<a href="https://\1">\1</a>\n', rand_str))


rand_str = '12345 12345-1234 1234 12346-333'
regex = re.compile(r'(\d{5})(-\d{4})?')
regex = re.compile(r'(\d{5}-\d{4}|\d{5}\s)')

print(re.findall(regex, rand_str))

r'\(?\d{3}\)?'