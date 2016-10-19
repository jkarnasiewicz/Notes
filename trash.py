# # Itertools
# # imap, ireduce, ifilter i izip === map, reduce, filter, zip (python 3)
# # islice - umożliwia podział potencjalnie nieskończonego generatora.
# # chain - laczy w łańcuch wiele generatorów.
# # takewhile - dodaje warunek, który powoduje zakończenie działania generatora.
# # cycle - rzez ciągłe powtarzanie skończonego generatora powoduje, że staje się on nieskończony.

# # numpy.show_config()
# # numpy.arange()
# # numpy.array()

# # Django - Najlepsze receptury
# # To Do
# # Tworzenie domieszek do modeli do obsługi relacji generycznych (46)
# # Wysyłanie obrazów na serwer i tworzenie miniatur obrazow (66)





# # 0. pep-8 (http://legacy.python.org/dev/peps/pep-0008/)
# # 1. Tworzenie domieszek do modeli do obsługi metaznaczników i url-ow (43)
# # 2. Dynamiczne ustawianie wartości zmiennej STATIC_URL dla użytkowników systemu Git
# # 3. Tworzenie i dołączanie ustawień lokalnych (ustawienia lokalne, a ustwienia produkcyjne)(settings-local.py)
# # 4. Konfigurację JavaScript - dobrym pomysłem jest dodanie dynamicznie generowanego pliku
# # 	 konfiguracyjnego do szablonu bazowego
# # 5. Paginator, infinitive scroll, boostrap modals
# # 5. Kodowanie bazy danych (utf-8)
# # 6. Tworzenie pliku z informacjami o ignorowanych zasobach w systemie Git (.gitignore)
# # 7. Usuwanie skompilowanych plików Pythona (.bash_profile)
# # 8. Base models (e.g. for Mixins, base_models.py)





# # W systemie Django wyróżnia się trzy typy dziedziczenia modeli: abstrakcyjne klasy bazowe (Abstract base classes),
# # dziedziczenie wielotabelowe (Multi-table inheritance) oraz modele proxy (Proxy models).

# # Domieszki(Mixins) modeli są abstrakcyjnymi klasami modeli z określonymi polami, własnościami i metodami.
# # Mixins encourage code reuse. A mixin can also be viewed as an interface with implemented methods.

# # Each model corresponds to its own database table and can be queried and created individually.
# # The inheritance relationship introduces links between the child model and each of its parents
# # (via an automatically-created OneToOneField)

# # Creating a proxy for the original model. You can create, delete and update instances of the proxy model
# # and all the data will be saved as if you were using the original (non-proxied) model

# class Meta:
# 	verbose_name = _(u"Pomysł")
# 	verbose_name_plural = _(u"Pomysły")
# 	abstract = True
# 	proxy = True





# # Przekazywanie całego reqesta do formularza
# # forms.py
# class MessageForm(forms.Form):
# 	# ...
# 	def __init__(self, request, *args, **kwargs):
# 		super(MessageForm, self).__init__(*args, **kwargs)
# 		self.request = request					# mozemy z niej skorzystać później
# 		self.fields['recipient'].queryset = self.fields['recipient'].queryset.exclude(pk=request.user.pk)

# # views.py
# @login_required
# def message_to_user(request):
# 	if request.method == "POST":
# 		form = MessageForm(request, data=request.POST)
# 		if form.is_valid():
# 			# ...
# 			return redirect("message_to_user_done")
# 	else:
# 		form = MessageForm(request)
# 	return render(request, "email_messages/message_to_user.html", { 'form': form })



# # Try Django 1.9
# # 26 - Bootstrap(html offset),
# # 27 - Pagination
# # 30 - social share links
# # 34 - using facebook comments
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eds.settings.dev")

# # Imported modules
# import sys
# sys.modules

# # REST - representational state transfer
# Podejście REST sugeruje przygotowanie struktury adresu URL dopasowanej do struktury danych

# # API - Application Programming Interface

# from django.test import TestCase, RequestFactory, modify_settings, override_settings



# # Python Unlocked

# delete method from Class
# del Class.method

# from itertools import chain

# def longest_chain(x):
# 	return chain(range(1, x + 1), range(x - 1, 0, -1))

# def num(x):
# 	longest_len = len(' '.join(str(t) for t in longest_chain(x)))
# 	for row in (longest_chain(i) for i in longest_chain(x)):
# 		s = ' '.join(str(t) for t in tuple(row))
# 		print('{0: ^{1}}'.format(s, longest_len))
	

# num(14)

# Design Patterns:

# Observer pattern - Spreading information to all listeners
# This is the basic pattern in which an object tells other objects about something
# interesting

# Strategy pattern - Changing the behavior of an algorithm
# Sometimes, the same piece of code must have different behavior for different
# invocation by different clients

# Singleton pattern - Providing the same view to all
# The singleton pattern maintains the same state for all instances of a class

# Template pattern - Refining algorithm to use case(Inheritance, overide methods)

# Adaptor pattern - Bridging class interfaces
# This pattern is used to adapt a given class to a new interface

	# def __getattr__(self, attr):
	# 	return getattr(self.fish,attr)

# Facade pattern - Hiding system complexity for a simpler interface

# Flyweight pattern - Consuming less memory with shared objects

# Command pattern - Easy-execution management for commands (83 Python Unlock)

# Abstract factory
# class Animal(six.with_metaclass(abc.ABCMeta, object)):
# 	""" clients only need to know this interface for animals"""
# 	@abc.abstractmethod
# 	def sound(self, ):
# 		pass

# Registry pattern - Adding functionality from anywhere in code to class

# State pattern - Changing execution based on state


# TDD
# self.assertLess(i, 4, "not less")



# # Stubs and Mocks
# class TestWorkerReporting(unittest.TestCase):

# 	def test_worker_busy(self,):
# 		mworker = create_autospec(IWorker)
# 		mworker.configure_mock(**{'is_busy.return_value':True})
# 		self.assertFalse(assign_if_free(mworker, {}))



# # Parameterization - Manageable inputs to tests(subTest)
# import unittest
# from itertools import combinations
# from functools import wraps

# def convert(alpha):
# 	return ','.join([str(ord(i)-96) for i in alpha])


# class TestOne(unittest.TestCase):
# 	def test_system(self,):
# 		cases = [("aa","1,1"),("bc","2,3"),("jk","4,5"),("xy","24,26")]
# 		for case in cases:
# 			with self.subTest(case=case):
# 				self.assertEqual(convert(case[0]),case[1])

# if __name__ == '__main__':
# 	unittest.main(verbosity=2)



# # Creating custom test runners (Python Unlock(99))
# unittest.main(verbosity=2, testRunner=XMLRunner)



# Running test cases in parallel
# The py.test library has an xdist plugin, which adds the capability to run tests in parallel



# OPTIMIZATION TECHNIQUES
# There are two major ways for logic slowdown; one is CPU(Central Processing Unit) time taken,
# and the second is the wait for results from some other entity(oczekiwanie na zasoby)

# We should pay close attention to not use loops inside loops, giving us quadratic
# behavior. We can use built-ins, such as map, ZIP, and reduce, instead of using loops
# if possible

# When we are inside a loop and reference an outside namespace variable, it is first
# searched in local, then nonlocal, followed by global, and then built-in scopes

# GIL
# If we give up GIL, atomicity for data structures is not guaranteed as there
# may be two threads working on same data structure at a given time

# Simple approach(time)
from functools import wraps
import time

def showtime(func):
	@wraps(func)
	def wrap(*args,**kwargs):
		st = time.time() #time clock can be used too
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




# Using C speeds
SWIG
C Foreign Function Interface (CFFI)
Cython
