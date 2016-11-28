# Profilng, Debuging and Optimisation

# Profiling to find bottlenecks

# timeit (overall time)
python -m timeit (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

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
import cProfile
cProfile.run('fun(100)')

python -m cProfile -s cumulative trash.py
python -m cProfile -s cumulative -o profile.stats trash.py 				# create file profile.stats





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





# Perf (Linux)
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

# cache-references i cache-miss
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

# przydziały pamięci i operacje wewnętrzne
Operacje wewnętrzne, które zmniejszają liczbę przydziałów pamięci (+=, *=)
Zamiast po prostu znaleźć właściwe dane w pamięci RAM, jeśli nie było ich w pamięci podręcznej,
operacja przydziału musi też skierować do systemu operacyjnego żądanie
dotyczące dostępnej porcji danych, a następnie zarezerwować ją. Takie żądanie generuje znacznie
większe obciążenie niż zwykłe wypełnienie pamięci podręcznej. Wypełnienie po chybieniu
w pamięci podręcznej ma postać sprzętowej funkcji zoptymalizowanej na płycie głównej,
przydzielanie pamięci natomiast wymaga do zakończenia działania komunikacji z innym
procesem, czyli jądrem.
Zmniejszenie liczby chybień w pamięci podręcznej, a w większym stopniu zredukowaniem liczby błędów stronicowania.

# instructions
Określa on liczbę instrukcji procesora, które musiały zostać wykonane w celu uruchomienia programu.
Innymi słowy, licznik informuje o liczbie operacji, które musiał wykonać procesor





# Coverage.py
Oprócz testowania jednostkowego należy też poważnie rozważyć użycie skryptu coverage.py.
Umożliwia on stwierdzenie, jakie wiersze kodu są sprawdzane przez testy, a ponadto identyfikuje
sekcje bez pokrycia





# Other libraries for profiling
pip install runsnake // pip install line_profiler - procesor
pip install memory_profiler // pip install psutil - pamieć
pip install guppy - obiekty w stercie
dowser










# Debugging

# Logging
import logging
logger = logging.getLogger(__name__)

def complicated_view():
	logger.debug("Entered the complicated_view()!")





# The Python debugger pdb
import pdb
pdb.set_trace()

next, step, print(variable_name), where



# run on module
python -m pdb file_name.py





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
	# Some place you want to break
	{% pdb %}
{% endfor %}

# Within the debugger
print(context["item"])





# Others:
1. ipdb
2. pudb							# import pudb; pudb.set_trace()
3. Django Debug Toolbar
4. stop a django application in the middle of execution (assert False)










# Optimisation
# There are two major ways for logic slowdown; one is CPU(Central Processing Unit) time taken,
# and the second is the wait for results from some other entity(oczekiwanie na zasoby)

   # na czym tak naprawde nam zalezy
0. Specialize your code - store only the data you need in order to answer specific questions
1. We should pay close attention to not use loops inside loops, giving us quadratic
   behavior. We can use built-ins, such as map, zip, and reduce, instead of using loops
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
jednostek obliczeniowych, jednostek pamięci i połączeń między pierwszymi dwiema grupami.
Jednostka obliczeniowa cechuje się liczbą obliczeń, jakie może wykonać w ciągu sekundy.
Jednostka pamięci wyróżnia się ilością danych, jakie może przechowywać, a także szybkością odczytu i zapisu danych.
Z kolei połączenia są określone przez to, jak szybko mogą przemieszczać dane z jednego miejsca w drugie.





# Lists and Tuples
Listy to tablice dynamiczne. Mogą się zmieniać i możliwa jest zmiana ich wielkości (zmiana
liczby przechowywanych elementów).
Krotki są tablicami statycznymi. Krotki nie mogą się zmieniać, a zawarte w nich dane nie
mogą zostać zmodyfikowane po utworzeniu krotki.
Krotki są buforowane przez środowisko uruchomieniowe interpretera języka Python.
Oznacza to, że nie jest wymagana komunikacja z jądrem w celu zarezerwowania pamięci
każdorazowo, gdy ma zostać użyta





# Dictionaries and Sets
Słowniki i zbiory używają tabel mieszających do osiągnięcia czasu O(1) dla swoich operacji wyszukiwania
i wstawiania. Taka wydajność jest wynikiem bardzo mądrego wykorzystania
funkcji mieszania w celu przekształcenia dowolnego klucza (np. łańcucha lub obiektu) w indeks
listy

# hash(), __hash__() - return total number
Wybranie złej funkcji hashującej(mieszającej) może być powodem bardzo dużego spowolnienia wyszukiwania
kluczy/wartości w danym słowniku





# Lifo and Fifo
Stos (ang. Stack) – liniowa struktura danych, w której dane dokładane są na wierzch stosu i z wierzchołka
stosu są pobierane (bufor typu LIFO, Last In, First Out; ostatni na wejściu, pierwszy na wyjściu).
Ideę stosu danych można zilustrować jako stos położonych jedna na drugiej książek –
nowy egzemplarz kładzie się na wierzch stosu i z wierzchu stosu zdejmuje się kolejne egzemplarze

Przeciwieństwem stosu jest kolejka, bufor typu FIFO
(ang. First In, First Out; pierwszy na wejściu, pierwszy na wyjściu), w którym dane obsługiwane
są w takiej kolejności, w jakiej zostały dostarczone (jak w kolejce do kasy).





# Import statements
Należy wyraźnie określić, jakie funkcje są importowane z modułu.
Takie podejście nie tylko zwiększa czytelność kodu, gdyż programista wie dokładnie, jakie
funkcje są wymagane ze źródeł zewnętrznych, ale też przyspiesza wykonywanie kodu!

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





# GIL (Global Interpreter Lock)
If we give up GIL, atomicity for data structures is not guaranteed as there
may be two threads working on same data structure at a given time





# Concurrency - wspolbieznosc
Lepsze wykorzystanie czasu procesora kiedy czeka na odpowiedz, kod asynchroniczny
AsyncIO, przeszukiwacz szeregowy(serial crawler), gevent, tornado
Operacje wejścia-wyjścia(I/O) mogą być uciążliwe dla przepływu programu. Każdorazowo, gdy
kod dokonuje odczytu z pliku, zapisu do gniazda sieciowego lub do bazy danych musi wstrzymać działanie
w celu skontaktowania się z jądrem, zażądać wykonania operacji, a następnie poczekać na
jej zakończenie.
(czasami sumaryczny czas oczekiwania na zakończenie żądan może zabierac 90% czasu działania algorytmu)





# Multiprocessing - przetwarzanie równoległe
from multiprocessing import Pool - przetwarzanie szeregowe
from multiprocessing import cpu_count





# Threads and Processes
Wątki(rywalizacja o blokadę GIL) w przypadku języka Python nadają się znakomicie na potrzeby zadań związanych
z operacjami wejścia-wyjścia, ale stanowią kiepską opcję przy problemach, w przypadku których
bazuje się głównie na procesorach(Procesy - każdy proces ma swój oddzielny interpreter pythona).





# Random numbers
zagrożenia związane z sekwencjami liczb losowych w przypadku przetwarzania równoległego.
Ponieważ w wersji kodu z procesami każdy nowy proces jest rozwidleniem, wszystkie wersje
z rozwidleniem będą współużytkować ten sam stan. Oznacza to, że w każdym procesie wywołania
liczb losowych zwrócą identyczną sekwencję!





# Komunikacja miedzyprocesowa (współużytkowanie danych)
Tworzymy obiekt który jest wsplny dla wszystkich procesów, np. by móc wcześniej zakończyć równoległe instrukcje
Pool - bez współużytkowania danych
Manager.Value jako flaga
Redis jako flaga - redis pełni rolę szybkiego i scentralizowanego repozytorium danych,
RawValue
mmap





# Synchronizacja
Współużytkowanie danych może być przyczyną frustracji. Jeśli to możliwe, próbuj tego unikać
Sensowne może być zastosowanie jedynie naiwnego wariantu przetwarzania
równoległego (bez komunikacji międzyprocesowej IPC - inter-process communication, więcej procesorów)

# Synchronizowanie dostępu do zmiennych i plików
import lockfile
multiprocessing.Value/RawValue + multiprocessing.Lock





# Clusters(Klastry)
Zbiór komputerów współpracujących ze sobą w celu rozwiązania typowego zadania.
Na zewnątrz sieci klaster może wyglądać jak pojedynczy większy system.
Parallel Python, IPython Paraller, NSQ, Celery, ZeroMQ (messageQueue)(Scaling horizontally)

# Przeprowadzono profilowanie systemu w celu poznania wąskich gardeł.
# Wykorzystano rozwiązania do kompilowania, takie jak Cython.
# Wykorzystano wiele rdzeni jednego komputera (może to być pokaźna maszyna z wieloma
# rdzeniami).
# Wykorzystano techniki zapewniające mniejsze zużycie pamięci RAM.










# Pamiec RAM
1. zamiast list() użyć set()
2. array - Moduł array efektywnie przechowuje obiekty typów podstawowych, takie jak liczby całkowite,
   liczby zmiennoprzecinkowe i znaki, lecz nie liczby zespolone lub klasy. Do przechowywania
   bazowych danych moduł tworzy ciągły blok pamięci RAM.
3. numpy
4. jednym z ważnych powodów przejścia na język Python w wersji 3.3 lub nowszej jest to, że
   przechowywanie obiektów Unicode powoduje znacznie mniejsze wykorzystanie pamięci niż
   w przypadku języka Python 2.7.
   Jej działanie polega na obserwacji zakresu znaków w łańcuchu i w razie możliwości użyciu
   najmniejszej liczby bajtów do reprezentowania znaków niższego stopnia
5. kompresowaniem za pomocą drzewa trie
6. posortowanie listy i uzycie bisect.bisect_left()
7. graf słów DAWG (Directed Acyclic Word Graph) (import dawg)
   Efektywne reprezentowanie łańcuchów, które współużytkują przedrostki i przyrostki.
   Graf DAWG nie może być modyfikowany po utworzeniu
8. drzewo trie Marisa (import marisa_trie)
   to statyczne drzewo trie używające powiązań kompilatora Cython do biblioteki zewnętrznej.
   Z powodu statyczności drzewo to nie może być modyfikowane po utworzeniu
9. Drzewo trie HAT (import hat_trie)



# Probabilistyczne struktury danych
# Odpowiednie funkcje mieszajace(hash)
1. Obliczenia o bardzo dużym stopniu przybliżenia z wykorzystaniem jednobajtowego licznika Morrisa
2. Filtry Blooma
3. KMinValues
4. Licznik LogLog/HyperLogLog



# Using C speeds
SWIG
C Foreign Function Interface (CFFI)
Cython










# Django optimisation

# Frontend performance
1. Cache infinitely with CachedStaticFilesStorage
2. Use a static asset manager (e.g. django-pipeline or webassets)


# Backend performance
django-debug-toolbar
django-silk

# Enable the cached template loader in production

# Reduce database hits with select_related:
If you are using a OneToOneField or a Foreign Key relationship,
in forward direction, for a large number of objects, then select_related()
can perform a SQL join and reduce the number of database hits.

# Reduce database hits with prefetch_related:
For accessing a ManyToManyField method or, a Foreign Key relation,
in reverse direction, or a Foreign Key relation in a large number of objects,
consider using prefetch_related to reduce the number of database hits.

# Fetch only needed fields with values or values_list:
You can save time and memory usage by limiting queries to return only the
needed fields and skip model instantiation using values() or values_list()

# Denormalize models:
Selective denormalization improves performance
by reducing joins at the cost of data consistency

# Add an Index:
If a non-primary key gets searched a lot in your queries,
consider setting that fields db_index to True in your model definition

# Create, update, and delete multiple rows at once:
Multiple objects can be operated upon in a single database query with
the bulk_create(), update(), and delete() methods

# Most production systems use a memory-based caching system such as Redis or
# Memcached

# Cached session backend
By default, Django stores its user session in the database. This usually gets
retrieved for every request. To improve performance, the session data can be
stored in memory by changing the SESSION_ENGINE setting. For instance,
add the following in settings.py to store the session data in your cache:
SESSION_ENGINE = "django.contrib.sessions.backends.cache"










# Production
# hosting options, including PaaS(platform as a service) and VPS(virtual private server)

# Components of a stack
1. Which OS and distribution? For example: Debian, Red Hat, or OpenBSD.
2. Which WSGI server? For example: Gunicorn, uWSGI.
3. Which web server? For example: Apache, Nginx.
4. Which database? For example: PostgreSQL, MySQL, or Redis.
5. Which caching system? For example: Memcached, Redis.
6. Which process control and monitoring system? For example: Upstart,
   Systemd, or Supervisord.
7. How to store static media? For example: Amazon S3, CloudFront.
