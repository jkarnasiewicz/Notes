# OPTIMISATION/PROFILING/DEBUGING/SECURITY/DESIGN PATTERNS/PYTHON 2VS3

# PROFILING TO FIND BOTTLENECKS

# timeit (overall time)
python -m timeit (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)							# from console

from timeit import timeit
timeit(setup='from __main__ import fun',
	   stmt='[fun(i) for i in range(1000)]',
	   number=100)



# Simple approach(time)
from functools import wraps
import time

def showtime(func):
	@wraps(func)
	def wrap(*args,**kwargs):
		st = time.time()
		result = func(*args,**kwargs)
		et = time.time()
		print("{}:{}".format(func.__name__, et-st))
	return result
return wrap

@showtime
def func_c():
	for i in range(1000):
		for j in range(1000):
			for k in range(100):
				pass

if __name__ == '__main__':
	func_c()



# cProfile (time per function)
python -m cProfile -s cumulative trash.py
python -m cProfile -s cumulative -o profile.stats trash.py 				# create file profile.stats

import cProfile
cProfile.run('fun(100)')



# Time profilers
import line_profiler

l = []

def func_c():
	global l
	for i in range(10000):
		l.append(i)
	m = list(range(100000))

if __name__ == '__main__':
	profiler = line_profiler.LineProfiler()
	profiler.add_function(func_c)
	profiler.run('func_c()')
	profiler.print_stats()



# Memory profilers
from memory_profiler import profile

@profile(precision=4)
def func_c():
	global l
	for i in range(10000):
		l.append(i)
	m = list(range(100000))

if __name__ == '__main__':
	func_c()




# Perf(Linux)
perf stat -e cycles,stalled-cycles-frontend,stalled-cycles-backend,instructions,\
cache-references,cache-misses,branches,branch-misses,task-clock,faults,\
minor-faults,cs,migrations -r 3 python file_name.py

# context-switches i CPU-migrations
Liczniki context-switches i CPU-migrations informują o sposobie wstrzymania pracy programu
w celu poczekania na zakończenie operacji jądra (np. operacji wejścia-wyjścia), umożliwienia
działania innym aplikacjom lub przekazania wykonywania do innego rdzenia procesora.
Wartość licznika CPU-migrations jest rejestrowana po zatrzymaniu programu i wznowieniu go
w innym procesorze niż ten, który był używany wcześniej, aby wszystkie procesory miały
taki sam poziom wykorzystania. Może to być postrzegane jako szczególnie niewłaściwe przełączanie
kontekstu, ponieważ nie tylko program jest tymczasowo wstrzymywany, ale też tracone
są wszelkie dane znajdujące się w pamięci podręcznej L1 (jak wspomniano, każdy proces
zawiera własną tego typu pamięć).

# Cache-references i cache-miss
Każdorazowo przy odwołaniu do danych zawartych w pamięci podręcznej
zwiększa się wartość licznika cache-references. Jeśli takich danych nie będzie jeszcze w pamięci
podręcznej i wymagane będzie pobranie ich z pamięci RAM, zmieni się wartość licznika
cache-miss. Nie dojdzie do tego, jeżeli odczytywane są dane wcześniej wczytywane (takie
dane nadal są w pamięci podręcznej) lub zlokalizowane w pobliżu danych niedawno używanych
(dane są wysyłane z pamięci RAM do pamięci podręcznej w porcjach). Chybienia
w pamięci podręcznej mogą być źródłem spowolnienia w przypadku działania powiązanego
z procesorem, ponieważ w takiej sytuacji nie tylko konieczne jest oczekiwanie na pobranie
danych z pamięci RAM, ale też przerywany jest przepływ potoku wykonywania

Ponieważ magistrala może przesyłać wyłącznie ciągłe obszary pamięci, będzie to możliwe tylko wtedy, gdy dane
siatki będą sekwencyjnie przechowywane w pamięci RAM(np. numpy.arange()). Ze względu na to, że lista(list())
przechowuje wskaźniki do danych, a nie rzeczywiste dane, faktyczne wartości w siatce są porozrzucane po całej
pamięci, przez co nie mogą być wszystkie od razu skopiowane.

# Przydziały pamięci i operacje wewnętrzne
Operacje wewnętrzne, które zmniejszają liczbę przydziałów pamięci (+=, *=)
Zamiast po prostu znaleźć właściwe dane w pamięci RAM, jeśli nie było ich w pamięci podręcznej,
operacja przydziału musi też skierować do systemu operacyjnego żądanie
dotyczące dostępnej porcji danych, a następnie zarezerwować ją. Takie żądanie generuje znacznie
większe obciążenie niż zwykłe wypełnienie pamięci podręcznej. Wypełnienie po chybieniu
w pamięci podręcznej ma postać sprzętowej funkcji zoptymalizowanej na płycie głównej,
przydzielanie pamięci natomiast wymaga do zakończenia działania komunikacji z innym
procesem, czyli jądrem.
Zmniejszenie liczby chybień w pamięci podręcznej, a w większym stopniu zredukowaniem liczby błędów stronicowania.

# instructions - określa on liczbę instrukcji procesora,
które musiały zostać wykonane w celu uruchomienia programu. Innymi słowy, licznik
informuje o liczbie operacji, które musiał wykonać procesor





# Coverage.py
Oprócz testowania jednostkowego należy też poważnie rozważyć użycie skryptu coverage.py.
Umożliwia on stwierdzenie, jakie wiersze kodu są sprawdzane przez testy, a ponadto identyfikuje
sekcje bez pokrycia

# other libraries for profiling
pip install runsnake // pip install line_profiler - procesor
pip install memory_profiler // pip install psutil - pamieć
pip install guppy - obiekty w stercie
dowser










# OPTIMISATION
# There are two major ways for logic slowdown; one is CPU(Central Processing Unit) time taken,
# and the second is the wait for results from some other entity(oczekiwanie na zasoby)

   # na czym tak naprawde nam zalezy
0. Specialize your code - store only the data you need in order to answer specific questions
1. We should pay close attention to not use loops inside loops, giving us quadratic
   behavior. We can use built-ins, such as map, ZIP, and reduce, instead of using loops
   if possible
2. Always prefer build-in functions e.g: use sum() instead of own counting algorithm
3. The order of components in logical conditions (e.g. or) its very important,
   first component should be always the 'fastest' one
4. Good __hash__ function
   # when we are inside a loop and reference an outside namespace variable, it is first
   # searched in local, then nonlocal, followed by global, and then built-in scopes
   # (global and local dictionaries - LEGB)
5. Efekty powolnych wyszukiwań w przestrzeniach nazw w pętlach
6. Specify wich function will be imported in imported statement
7. Use iterators and generators - data streaming (aka lazy evaluation)
8. If can, use tuple or numpy arrays instead of list
   # przemieszczenie powtarzającego się kodu poza obręb szybkiej pętli
9. Dislocating repeated code outside the fast loops
10. Vectorization (wektoryzacja), SIMD Single Instruction, Multiple Data
11. Ogólna zasada jest taka, że jeśli zadania cechują się zmiennym czasem
    działania, należy tworzyć wiele małych zadań w celu efektywnego wykorzystania zasobów.
12. Dziel, mnóż, dodawaj, odejmuj zamiast używać pętl lub inkrementacji(podstawowe działania są najszybsze)



# Bazowe elementy tworzące komputery można uprościć przez zaklasyfikowanie ich do trzech podstawowych grup:
# jednostek obliczeniowych, jednostek pamięci i połączeń między pierwszymi dwiema grupami.
# Jednostka obliczeniowa cechuje się liczbą obliczeń, jakie może wykonać w ciągu sekundy.
# Jednostka pamięci wyróżnia się ilością danych, jakie może przechowywać, a także szybkością odczytu i zapisu danych.
# Z kolei połączenia są określone przez to, jak szybko mogą przemieszczać dane z jednego miejsca w drugie.



# Lists and Tuples
# Listy to tablice dynamiczne. Mogą się zmieniać i możliwa jest zmiana ich wielkości (zmiana
# liczby przechowywanych elementów).
# Krotki są tablicami statycznymi. Krotki nie mogą się zmieniać, a zawarte w nich dane nie
# mogą zostać zmodyfikowane po utworzeniu krotki.
# Krotki są buforowane przez środowisko uruchomieniowe interpretera języka Python.
# Oznacza to, że nie jest wymagana komunikacja z jądrem w celu zarezerwowania pamięci
# każdorazowo, gdy ma zostać użyta



# Dictionaries and Sets
# Słowniki i zbiory używają tabel mieszających do osiągnięcia czasu O(1) dla swoich operacji wyszukiwania
# i wstawiania. Taka wydajność jest wynikiem bardzo mądrego wykorzystania
# funkcji mieszania w celu przekształcenia dowolnego klucza (np. łańcucha lub obiektu) w indeks
# listy

# hash(), __hash__() - return total number
# Wybranie złej funkcji hashującej(mieszającej) może być powodem bardzo dużego spowolnienia wyszukiwania
# kluczy/wartości w danym słowniku



# Lifo and Fifo
# Stos (ang. Stack) – liniowa struktura danych, w której dane dokładane są na wierzch stosu i z wierzchołka
# stosu są pobierane (bufor typu LIFO, Last In, First Out; ostatni na wejściu, pierwszy na wyjściu).
# Ideę stosu danych można zilustrować jako stos położonych jedna na drugiej książek –
# nowy egzemplarz kładzie się na wierzch stosu i z wierzchu stosu zdejmuje się kolejne egzemplarze

# Przeciwieństwem stosu jest kolejka, bufor typu FIFO
# (ang. First In, First Out; pierwszy na wejściu, pierwszy na wyjściu), w którym dane obsługiwane
# są w takiej kolejności, w jakiej zostały dostarczone (jak w kolejce do kasy).



# Import statements
# Należy wyraźnie określić, jakie funkcje są importowane z modułu.
# Takie podejście nie tylko zwiększa czytelność kodu, gdyż programista wie dokładnie, jakie
# funkcje są wymagane ze źródeł zewnętrznych, ale też przyspiesza wykonywanie kodu!

# Efekty powolnych wyszukiwań w przestrzeniach nazw w pętlach
from math import sin
def tight_loop_slow(iterations):
	result = 0
	for i in xrange(iterations):
		# to wywołanie funkcji sin wymaga wyszukiwania globalnego(2.21 s per loop)
		result += sin(i)

def tight_loop_fast(iterations):
	result = 0
	local_sin = sin
	for i in xrange(iterations):
		# to wywołanie funkcji local_sin wymaga wyszukiwania lokalnego(2.02 s per loop)
		result += local_sin(i)





# GIL
# If we give up GIL, atomicity for data structures is not guaranteed as there
# may be two threads working on same data structure at a given time





# Concurrency - wspolbieznosc
# Lepsze wykorzystanie czasu procesora kiedy czeka na odpowiedz, kod asynchroniczny
# AsyncIO, przeszukiwacz szeregowy(serial crawler), gevent, tornado
# Operacje wejścia-wyjścia(I/O) mogą być uciążliwe dla przepływu programu. Każdorazowo, gdy
# kod dokonuje odczytu z pliku, zapisu do gniazda sieciowego lub do bazy danych musi wstrzymać działanie
# w celu skontaktowania się z jądrem, zażądać wykonania operacji, a następnie poczekać na
# jej zakończenie.
# (czasami sumaryczny czas oczekiwania na zakończenie żądan może zabierac 90% czasu działania algorytmu)





# Multiprocessing - przetwarzanie równoległe
# from multiprocessing import Pool - przetwarzanie szeregowe
# from multiprocessing import cpu_count



# Threads and Processes
# Wątki(rywalizacja o blokadę GIL) w przypadku języka Python nadają się znakomicie na potrzeby zadań związanych
# z operacjami wejścia-wyjścia, ale stanowią kiepską opcję przy problemach, w przypadku których
# bazuje się głównie na procesorach(Procesy - każdy proces ma swój oddzielny interpreter pythona).



# Random numbers
# zagrożeń związanych z sekwencjami liczb losowych w przypadku
# przetwarzania równoległego.
# Ponieważ w wersji kodu z procesami każdy nowy proces jest rozwidleniem, wszystkie wersje
# z rozwidleniem będą współużytkować ten sam stan. Oznacza to, że w każdym procesie wywołania
# liczb losowych zwrócą identyczną sekwencję!



# Komunikacja miedzyprocesowa (współużytkowanie danych)
# Tworzymy obiekt który jest wsplny dla wszystkich procesów, np. by móc wcześniej zakończyć równoległe instrukcje
# Pool - bez współużytkowania danych
# Manager.Value jako flaga
# Redis jako flaga - redis pełni rolę szybkiego i scentralizowanego repozytorium danych,
# RawValue
# mmap



# Synchronizacja
# Pamiętaj jednak, że współużytkowanie danych może być przyczyną frustracji. Jeśli to możliwe, próbuj tego unikać
# Sensowne może być zastosowanie jedynie naiwnego wariantu przetwarzania
# równoległego (bez komunikacji międzyprocesowej IPC - inter-process communication, więcej procesorów)

# Synchronizowanie dostępu do zmiennych i plików
# import lockfile
# multiprocessing.Value/RawValue + multiprocessing.Lock





# Clusters(Klastry) - zbiór komputerów współpracujących ze sobą w celu rozwiązania typowego zadania.
# Na zewnątrz sieci klaster może wyglądać jak pojedynczy większy system.
# Parallel Python, IPython Paraller, NSQ, Celery, ZeroMQ (messageQueue)(Scaling horizontally)

# Przeprowadzono profilowanie systemu w celu poznania wąskich gardeł.
# Wykorzystano rozwiązania do kompilowania, takie jak Cython.
# Wykorzystano wiele rdzeni jednego komputera (może to być pokaźna maszyna z wieloma
# rdzeniami).
# Wykorzystano techniki zapewniające mniejsze zużycie pamięci RAM.





# Pamiec RAM

# 1. Zamiast list() użyć set()
# 2. array - Moduł array efektywnie przechowuje obiekty typów podstawowych, takie jak liczby całkowite,
# liczby zmiennoprzecinkowe i znaki, lecz nie liczby zespolone lub klasy. Do przechowywania
# bazowych danych moduł tworzy ciągły blok pamięci RAM.

# 3. numpy

# 4. Jednym z ważnych powodów przejścia na język Python w wersji 3.3 lub nowszej jest to, że
# przechowywanie obiektów Unicode powoduje znacznie mniejsze wykorzystanie pamięci niż
# w przypadku języka Python 2.7.
# Jej działanie polega na obserwacji zakresu znaków w łańcuchu i w razie możliwości użyciu
# najmniejszej liczby bajtów do reprezentowania znaków niższego stopnia

# 5. Kompresowaniem za pomocą drzewa trie

# 6. Posortowanie listy i uzycie bisect.bisect_left()

# 7. Graf słów DAWG (Directed Acyclic Word Graph) (import dawg)
# Efektywne reprezentowanie łańcuchów, które współużytkują przedrostki i przyrostki.
# Graf DAWG nie może być modyfikowany po utworzeniu

# 8. Drzewo trie Marisa (import marisa_trie)
# to statyczne drzewo trie używające powiązań kompilatora Cython do biblioteki zewnętrznej.
# Z powodu statyczności drzewo to nie może być modyfikowane po utworzeniu

# 9. Drzewo trie HAT (import hat_trie)



# Probabilistyczne struktury danych
# Odpowiednie funkcje mieszajace(hash)
# 1. Obliczenia o bardzo dużym stopniu przybliżenia z wykorzystaniem jednobajtowego licznika Morrisa

# 2. Filtry Blooma

# 3. KMinValues

# 4. Licznik LogLog/HyperLogLog



# Using C speeds
# SWIG
# C Foreign Function Interface (CFFI)
# Cython



# General informations

# Gathering requirements:

1. Talk directly to the application owners even if they are not technical savvy.
2. Make sure you listen to their needs fully and note them.
3. Dont use technical jargon such as "models". Keep it simple and use end-user
   friendly terms such as a "user profile".
4. Set the right expectations. If something is not technically feasible or difficult,
   make sure you tell them right away.
5. Sketch as much as possible. Humans are visual in nature. Websites more so.
   Use rough lines and stick figures. No need to be perfect.
6. Break down process flows such as user signup. Any multistep functionality
   needs to be drawn as boxes connected by arrows.
7. Finally, work through the features list in the form of user stories or in any
   easy way to understand the form.
8. Play an active role in prioritizing the features into high, medium,
   or low buckets.
9. Be very, very conservative in accepting new features.
10. Post-meeting, share your notes with everyone to avoid misinterpretations.

+. Single-page document that quickly tells what the site is meant to be



# Design Patterns

Each pattern describes a problem, which occurs over and over again in our environment,
and then describes the core of the solution to that problem in such a way that you can
use this solution a million times over, without ever doing it the same way twice

In the world of software, the term design pattern refers to a general repeatable
solution to a commonly occurring problem in software design

# Observer pattern - Spreading information to all listeners
This is the basic pattern in which an object tells other objects about something
interesting

# Strategy pattern - Changing the behavior of an algorithm
Sometimes, the same piece of code must have different behavior for different
invocation by different clients

# Singleton pattern - Providing the same view to all
The singleton pattern maintains the same state for all instances of a class

# Template pattern - Refining algorithm to use case(Inheritance, overide methods)

# Adaptor pattern - Bridging class interfaces
This pattern is used to adapt a given class to a new interface

    def __getattr__(self, attr):
      return getattr(self.fish, attr)

# Facade pattern - Hiding system complexity for a simpler interface

# Flyweight pattern - Consuming less memory with shared objects

# Command pattern - Easy-execution management for commands (83 Python Unlock)

# Abstract factory
class Animal(six.with_metaclass(abc.ABCMeta, object)):
 	""" clients only need to know this interface for animals"""
 	@abc.abstractmethod
 	def sound(self, ):
		pass

# Registry pattern - Adding functionality from anywhere in code to class

# State pattern - Changing execution based on state





# MODELS
# Structural patterns

# Patterns – normalized models
# denormalization(speed of the queries) and normalization(space with consistent data)
Problem: By design, model instances have duplicated data that cause data inconsistencies.
Solution: Break down your models into smaller models through normalization.
Connect these models with logical relationships between them.

# Pattern – model mixins
# Smaller mixins are better. Whenever a mixin becomes large and violates the Single
# Responsibility Principle, consider refactoring it into smaller classes. Let a mixin do
# one thing and do it well
Problem: Distinct models have the same fields and/or methods duplicated violating
the DRY principle.
Solution: Extract common fields and methods into various reusable model mixins.

# Pattern – service/utils objects
Problem: Models can get large and unmanageable. Testing and maintenance
get harder as a model does more than one thing.
Solution: Refactor out a set of related methods(e.g. @staticmethod or celery tasks)
into a specialized 'service' or 'utils' object.

# Retrieval patterns
This section contains design patterns that deal with accessing model properties or
performing queries on them.

# Pattern – property field
Problem: Models have attributes that are implemented as methods. However, these
attributes should not be persisted to the database.
Solution: Use the property decorator on such methods(@property)
# If it is an expensive calculation, we might want to cache the result(@cached_property)

# Pattern – custom model managers
Problem: Certain queries on models are defined and accessed repeatedly
throughout the code violating the DRY principle.
Solution: Define custom managers to give meaningful names to common queries

# VIEWS
# Pattern – context enhancers
Problem: Several views need the same context variable
Solution: Create a mixin or context processors(TEMPLATE_CONTEXT_PROCESSORS)
that sets the shared context variable

# Pattern – services
# This form of a service is usually called a web Application Programming Interface (API).
Problem: Information from your website is often scraped and processed by
other applications.
Solution: Create lightweight services that return data in machine-friendly formats,
such as JSON or XML(e.g. Django REST framework)

# TEMPLATES
# Pattern – template inheritance tree
Problem: Templates have lots of repeated content in several pages.
Solution: Use template inheritance wherever possible and include snippets elsewhere.

# ADMIN
# Don't give admin access to end users

# Pattern – feature flags
# selected users within a controlled experiment, performance testing for new features
Problem: Publishing of new features to users and deployment of the corresponding
code in production should be independent.
Solution: Use feature flags to selectively enable or disable features after deployment

# FORMS
# Pattern – dynamic form generation
Problem: Adding form fields dynamically or changing form fields from what
has been declared.
Solution: Add or change fields during initialization of the form.

class PersonDetailsForm(forms.Form):
	name = forms.CharField(max_length=100)
	age = forms.IntegerField()

	def __init__(self, *args, **kwargs):
		upgrade = kwargs.pop("upgrade", False)
		super().__init__(*args, **kwargs)

		if upgrade:
			self.fields["first_class"] = forms.BooleanField(
				label="Fly First Class?")

# PersonDetailsForm(upgrade=True)

# Pattern – multiple form actions per view with prefix
form = SubscribeForm(prefix="offers")





# DEBUGGING
# stop a django application in the middle of execution
# assert False


# Logging
import logging
logger = logging.getLogger(__name__)

def complicated_view():
	logger.debug("Entered the complicated_view()!")

# The Django Debug Toolbar

# The Python debugger pdb
import pdb
pdb.set_trace()

# also try:
# ipdb
# pudb => import pudb; pudb.set_trace()



# Debugging Django templates
set TEMPLATE_DEBUG to True

# debug tag(dump all the variables)
<textarea onclick="this.focus();this.select()" style="width: 100%;">
	{% filter force_escape %}
		{% debug %}
	{% endfilter %}
</textarea>



# custom template tag debug
# templatetags/debug.py
import pudb as dbg
from django.template import Library, Node

register = Library()

class PdbNode(Node):

	def render(self, context):
		dbg.set_trace() # Debugger will stop here
		return ''

@register.tag
def pdb(parser, token):
	return PdbNode()

# template.html
{% load debug %}
{% for item in items %}
	{# Some place you want to break #}
	{% pdb %}
{% endfor %}

Within the debugger
print(context["item"])





# SECURITY
# Cross-site scripting (XSS)
# considered the most prevalent web application security flaw today,
# enables an attacker to execute his malicious scripts (usually JavaScript)
# on web pages viewed by users



# Cross-Site Request Forgery (CSRF)
# is an attack that tricks a user into making
# unwanted actions on a website, where they are already authenticated, while they
# are visiting another site. Say, in a forum, an attacker can place an IMG or IFRAME tag
# within the page that makes a carefully crafted request to the authenticated site.



# SQL injection
# is the second most common vulnerability of web applications,
# after XSS. The attack involves entering malicious SQL code into a query that
# gets executed on the database. It could result in data theft, by dumping database
# contents, or the distruction of data, say, by using the DROP TABLE command.



# Clickjacking('django.middleware.clickjacking.XFrameOptionsMiddleware')
# is a means of misleading a user to click on a hidden link or button in
# the browser when they were intending to click on something else. This is typically
# implemented using an invisible IFRAME that contains the target website over a
# dummy web page(shown here) that the user is likely to click on



# Shell injection
# As the name suggests, shell injection or command injection allows an attacker
# to inject malicious code to a system shell such as bash. Even web applications use
# command-line programs for convenience and their functionality. Such processes
# are typically run within a shell.



# A handy security checklist
1. Dont trust data from a browser, API, or any outside sources: This is a
fundamental rule. Make sure you validate and sanitize any outside data.
2. Dont keep SECRET_KEY in version control: As a best practice, pick
SECRET_KEY from the environment. Check out the django-environ package.
3. Dont store passwords in plain text: Store your application password hashes
instead. Add a random salt as well.
4. Dont log any sensitive data: Filter out the confidential data such as credit
card details or API keys from your log files.
5. Any secure transaction or login should use SSL: Be aware that
eavesdroppers in the same network as you are could listen to your web
traffic if is not in HTTPS. Ideally, you ought to use HTTPS for the entire site.
6. Avoid using redirects to user-supplied URLs: If you have redirects such as
http://example.com/r?url=http://evil.com, then always check against
whitelisted domains.
7. Check authorization even for authenticated users: Before performing
any change with side effects, check whether the logged-in user is allowed
to perform it.
8. Use the strictest possible regular expressions: Be it your URLconf or
form validators, you must avoid lazy and generic regular expressions.
9. Dont keep your Python code in web root: This can lead to an accidental
leak of source code if it gets served as plain text.
10. Use Django templates instead of building strings by hand: Templates
have protection against XSS attacks.
11. Use Django ORM rather than SQL commands: The ORM offers protection
against SQL injection.
12. Use Django forms with POST input for any action with side effects: It might
seem like overkill to use forms for a simple vote button. Do it.
13. CSRF should be enabled and used: Be very careful if you are exempting
certain views using the @csrf_exempt decorator.
14. Ensure that Django and all packages are the latest versions: Plan for
updates. They might need some changes to be made to your source code.
However, they bring shiny new features and security fixes too.
15. Limit the size and type of user-uploaded files: Allowing large file uploads
can cause denial-of-service attacks. Deny uploading of executables or scripts.
16. Have a backup and recovery plan: Thanks to Murphy, you can plan for an
inevitable attack, catastrophe, or any other kind of downtime. Make sure
you take frequent backups to minimize data loss.




# PRODUCTION
# hosting options, including PaaS(platform as a service) and VPS(virtual private server)

Components of a stack
1. Which OS and distribution? For example: Debian, Red Hat, or OpenBSD.
2. Which WSGI server? For example: Gunicorn, uWSGI.
3. Which web server? For example: Apache, Nginx.
4. Which database? For example: PostgreSQL, MySQL, or Redis.
5. Which caching system? For example: Memcached, Redis.
6. Which process control and monitoring system? For example: Upstart,
   Systemd, or Supervisord.
7. How to store static media? For example: Amazon S3, CloudFront.





# PRODUCTION PERFORMANCE(DDP 175)
# profiling and finding bottleneck
# Frondend performance
1. Cache infinitely with CachedStaticFilesStorage
2. Use a static asset manager (e.g. django-pipeline or webassets)


# Backend performance
django-debug-toolbar
django-silk

enable the cached template loader in production

Reduce database hits with select_related: If you are using a
OneToOneField or a Foreign Key relationship, in forward direction,
for a large number of objects, then select_related() can perform a
SQL join and reduce the number of database hits.

Reduce database hits with prefetch_related: For accessing a
ManyToManyField method or, a Foreign Key relation, in reverse direction,
or a Foreign Key relation in a large number of objects, consider using
prefetch_related to reduce the number of database hits.

Fetch only needed fields with values or values_list: You can save time
and memory usage by limiting queries to return only the needed fields
and skip model instantiation using values() or values_list()

Denormalize models: Selective denormalization improves performance
by reducing joins at the cost of data consistency

Add an Index: If a non-primary key gets searched a lot in your queries,
consider setting that fields db_index to True in your model definition

Create, update, and delete multiple rows at once: Multiple objects can
be operated upon in a single database query with the bulk_create(),
update(), and delete() methods

Most production systems use a memory-based caching system such as Redis or
Memcached

Cached session backend
By default, Django stores its user session in the database. This usually gets
retrieved for every request. To improve performance, the session data can be
stored in memory by changing the SESSION_ENGINE setting. For instance,
add the following in settings.py to store the session data in your cache:
SESSION_ENGINE = "django.contrib.sessions.backends.cache"









# PDB
# run on module
python -m pdb file_name.py

# in code
import pdb
pdb.set_trace()
next, step, print(variable_name), where



# Monkey patching lub guerrilla patching to technika polegająca na dostarczeniu kodu rozszerzającego
# lub modyfikującego inny kod w czasie jego działania (podmiana funkcji)
from django.utils import text
from slugify import slugify_de as awesome_slugify
awesome_slugify.to_lower = True
text.slugify = awesome_slugify



