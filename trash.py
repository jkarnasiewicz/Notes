# -*- coding: utf-8 -*-
# design pattern
# facade
# iterators
# decoartors

# Make the capturing pattern optional, and remember to deal with a trailing slash appropriately.
# Id find a noncapturing group around the capturing group the safest way to do that:

# url(r'^(?:(?P<book_id>\w+)/)?$', 'pro.views.book', name='book'),


# from django.contrib.auth.decorators import user_passes_test
# @user_passes_test(lambda user: user.is_anonymous)

# checking if dervied class has needed method at import module time
# class BaseMeta(type):

# 	def __new__(cls, name, bases, body):
# 		if not 'bar' in body:
# 			raise TypeError('Bad user class')
# 		return super().__new__(cls, name, bases, body)


# class Base(metaclass=BaseMeta):

# 	def foo(self):
# 		return self.bar()

# 	def __init_subclass__(self, *args, **kwargs):
# 		print(args, kwargs)

# 	def bar(self):
# 		raise NotImplemented


# class Derrived(Base):
# 	'user class'

# 	def bar(self):
# 		raise NotImplemented



# Every app is different and has a unique balance of I/O, CPU, and memory use.

# Bufor – obszar pamięci służący do tymczasowego przechowywania danych przesyłanych między dwoma systemami
# TLS Handshake

# DB Queries
# EXPLAIN

# partial indexes
CREATE INDEX products_published ON product_product (id) WHERE published = true;

Use TCP health checks instead of HTTP, to call WSGI without entering the request queue

'Cache invalidation' is a process in a computer system whereby entries in a cache are replaced or removed.


# Object-oriented programming (OOP)
# core oop objects --> classes, objectes, inheritance and polymorphism

# Polymorphism
1. relies on inheritance
2. allows child classes to be instantiated and treated as the same type as its parent
3. enables a parent class to be manifested into any of its child classes


# Make class attributes global
class Borg:
	_shared_state = {}

	def __inti__(self):
		self.__dict__ = self._shared_state


class Singleton(Borg):

	def __init__(self, **kwargs):
		print(kwargs, type(kwargs))
		Borg.__init__(self)
		self._shared_state.update(kwargs)

	def __str__(self):
		return str(self._shared_state)


print(Singleton(name='bzzz'))
print(Singleton(second='uff'))
