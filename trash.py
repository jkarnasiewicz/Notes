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
