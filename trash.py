# -*- coding: utf-8 -*-

# Fluent python
# check import order in metaprograming chapter
# 717 python jargon
# raise from lambda !

# ML/25
# JS/517

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

# At the End learn:
# unittest module
# regexp
# hash tables
# https vs http/wss vs ws
# mptt conception
# monte-carlo info
# make-files



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
# łatwo realizowane na współczesnych komputerach



# WebSockets 101
# Normally, Django uses HTTP to communicate between the client and server:
# The client sends an HTTP request to the server.
# Django parses the request, extracts a URL, and then matches it to a view.
# The view processes the request and returns an HTTP response to the client.

# Unlike HTTP, the WebSockets protocol allows bi-directional communication,
# meaning that the server can push data to the client without being prompted by the user.
# With HTTP, only the client that made a request receives a response. With WebSockets,
# the server can communicate with multiple clients simultaneously. As we will see later
# on in this tutorial, we send WebSockets messages using the ws:// prefix, as opposed to http://.


python manage.py loaddata search_app.json codility.json tree_traversal.json
python manage.py collectstatic

daphne HomePage.asgi:channel_layer --port 8000 --bind 0.0.0.0 -v2
python manage.py runworker -v2
python manage.py runworker -v2 --settings=HomePage.local_settings

heroku addons:create heroku-redis




# (.*) 	-> Greedy!
# /[^crnld]ope/							// any character but those within brackets range
# (?m)
# reference substitution, r'\1 \2'

# (?=expression)  : Look Ahead
# (?<=expression) : Look Behind

# (?!expression)  : Negative Look Ahead
# (?<!expression) : Negative Look Behind


# add to S1
# times = int(os.environ.get('TIMES',3))



Jack speaking, how may I help you?

‘May I ask who’s calling please?’
‘Can I ask whom I’m speaking to please?’
‘Where are you calling from?’
‘Is that definitely the right name/number?’
‘Could I speak to someone who ___?’
‘I would like to make a reservation please’
‘Could you put me through to extension number ___ please?’



# scikit-learn
scikit-learn, machine Learning in Python and javascript highcharts
Supervised learning(we told/train machine what the classes of features are)
Regression (predict a continuous response)
Linear Regression(Regresja liniowa)(best fitting line)/Coefficient of determination(Współczynnik determinacji)
Classification (predict a categorical response)
Classification k-Nearest Neighbors(not scaling well)/Accuracy(dokładność/trafność)
Classification Support Vector Machine(SVM)/Best separated hyperplane/Convex optimization problem/Kernels/RBF(Radial basic function)




PageSpeed Insights
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# back button
There is a better way—a much better way: using HTML5’s history.pushState and
history.replaceState methods to persist a state object, and the window.onpope
vent to restore the page state:

window.history.pushState({ page : page}, "Page " + page, "?page=" + page);

window.onpopstate = function(event) {
	check for event.state, if found, reload state
	if (!event.state) return;
	var page = event.state.page;
}



# session storage (DOM Storage techniques)
sessionStorage.setItem(key, value);
sessionStorage.getItem(key)
sessionStorage.removeItem(key);

# vs cookies(persistent through tab windows)
document.cookie;

# local storage
localStorage.setItem("key","value");
localStorage.key = value;

localStorage.clear();

# The sessionStorage object only stores data for the session, but the localStorage object stores data on the client forever, or until specifically removed.

# indexedDB


# github account
# https://www.linkedin.com account
