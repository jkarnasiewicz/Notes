# Classes, Descriptors, Function Factories, Decorators, Special Methods and Metaprogramming

# Callable objects: regular functions, lambdas expressions, classes(constructor),
# methods, instance objects with __call__

# Classes define the structure and behavior of objects
# Instance method - functions which can be called on objects(with self argument)
# instance.method() == Class.method(instance)

# Metaprogramming - in a nutshell, code that manipulates code(e.g. decorators, metaclasses, descriptors)
# (extensively used in frameworks and libraries)

# Metaclasses propagate down hierarchies (genetic mutation - wszystkie klasy które dziedziczą po Base będą mieć 'metaclass=mytype')
# class Base(metaclasses=mytype):
#     pass

# @staticmethod - without 'self' in method args. Code organization(like free function)
# @classmethod - first arg 'cls'. Refere to class object within the method class, e.g. class attribute
import random
class ShippingContainer:
	next_serial = 1337						# class attribute

	@staticmethod							# static method
	def get_code(owner, serial):
		return '{0}/{1}/{2}'.format(owner.upper(), random.randint(0, 100), serial)

	@classmethod							# class method
	def get_serial(cls):
		result = cls.next_serial
		cls.next_serial += 1
		return result

	@classmethod
	def create_empty_container(cls, owner):
		return cls(owner, content=None)		# create new class instance

	def __init__(self, owner, content):     # instance method
		self.owner = owner					# instance attribute
		self.content = content
		self.serial = ShippingContainer.get_serial()
		# or
		# self.serial = ShippingContainer.next_serial
		# ShippingContainer.next_serial += 1
		self.code = ShippingContainer.get_code(owner, self.serial)


a = ShippingContainer("John", "mix")
print(a.__dict__)
b = ShippingContainer("Ivy", "all")
print(b.__dict__)
c = ShippingContainer.create_empty_container("Yuri")
print(c.__dict__)










# Interface

# abstract classes are available via the standard abc library package
# they are useful for the definition of interfaces and common functionality

# from abc import ABCMeta, abstractmethod
# class Worker(metaclass=ABCMeta):
from abc import ABC, abstractmethod
class Worker(ABC):

	@abstractmethod
	def do(self, func, args, kwargs):
		"work on function"

	@abstractmethod
	def is_busy(self):
		"tell if busy"










# Properties

# Properties are class attributes designed to manage instance attributes
# Properties override instance attributes(instance attribute does not shadow class property)

# An expression like obj.attr does not search for attr starting with obj. The search actually
# starts at obj.__class__, and only if there is no property named attr in the class, python
# looks in the obj instance itself

# Defining only getter(@property) make attribute read only

# Properties gracefully convert public attributes to private

# Property function, property(fget=None, fset=None, fdel=None, doc=None)

# New class property shadows existing instance attribute
# Class.property_value = property(lambda self: 'the new property value')

class Example:

	def __init__(self, name):
		self.name = name

	@property
	def name(self):
		"Documentation for the name property, e.g. help(Example.name)"
		print('get')
		return self._name

	@name.setter
	def name(self, value):
		print('set')
		self._name = value

	@name.deleter
	def name(self):
		print('del')
		self._name = None


e = Example('John')
print(e.__dict__)
del e.name
print(e.name)



# Property factory
def quantity(storage_name):

	def qty_getter(instance):
		# qty_getter references storage_name, so it will be preserved in the closure of
		# this function; the value is retrieved directly from the instance.__dict__ to
		# bypass the property and avoid an infinite recursion
		return instance.__dict__[storage_name]

	def qty_setter(instance, value):
		if value > 0:
			instance.__dict__[storage_name] = value
		else:
			raise ValueError('value must be > 0')
	return property(qty_getter, qty_setter, doc='quantity property factory')


class LineItem:
	# Remember: the right side of an assignment is evaluated first, so when
	# quantity() is invoked, the weight/price class attribute doesn’t even exist
	weight = quantity('weight')
	price = quantity('price')

	def __init__(self, description, weight, price):
		self.description = description
		self.weight = weight
		self.price = price

	def subtotal(self):
		return self.weight * self.price


q = quantity('help')
print(q.fset.__closure__[0].cell_contents)

nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)










# Descriptors

# Attribute Descriptors are a way of reusing the same access logic in multiple attributes

# Descriptors - customized processing of attribute access (dostosowany/zindywidualizowany proces dostępu do atrybutu)
# Descriptor is an object attribute with 'binding behavior'(wiążącym zachowaniem),
# one whose attribute access has been overridden by methods in the descriptor protocol
# Those methods are __get__(), __set__(), and __delete__()
# If any of those methods are defined for an object, it is said to be a descriptor

# Descriptor works only in a class. Storing attribute data directly in a descriptor means sharing between instances

# Class.descriptor_name triggers the descriptor __get__ method, passing None as the second argument (instance)

# Descriptors are a great solutions for attributes with common behavior across multiple classes
# - reusable propertise (e.g. database fields, attached to many different classes with many different names)

# Descriptors are the mechanism behind properties, methods, static methods, class methods, super(),
# field types in ORMs such as the Django ORM or SQL Alchemy, managing the flow of data from the fields
# in a database record to Python object attributes and vice-versa


# Descriptor Protocol
descr.__get__(self, instance, type=None) --> value          # type == cls
descr.__set__(self, instance, value) --> None
descr.__delete__(self, instance) --> None


class RevealAccess(object):
	"A data descriptor that sets and returns values normally and prints a message logging their access."

	def __init__(self, initval=None, name='var'):
		self.val = initval
		self.name = name

	def __get__(self, instance, objtype):
		print('Retrieving', self.name)
		return self.val

	def __set__(self, instance, val):
		print('Updating', self.name)
		self.val = val


class MyClass(object):
	x = RevealAccess(10, 'var "x"')
	y = 5


m = MyClass()
print(m.x)
m.x = 20
print(m.x, m.y)



# Accessing an attribute on an instance like instance.foo gets you:
#   1. The result of the __get__ method of the data descriptor of the same name attached to the class if it exists
#   2. The corresponding value in instance.__dict__ if it exists
#   3. The result of the __get__ method of the non-data descriptor of the same name on the class
#   4. It falls back to look in the type(instance).__dict__
#   5. Repeating for each type in the mro until it find a match
#   6. Assignment always creates an entry in instance.__dict__
#   7. Unless there was a setter property(which is a descriptor) in which case we're calling a function



# Descriptor version of LineItem class
class Quantity:
	def __init__(self, storage_name):
		self.storage_name = storage_name

	def __set__(self, instance, value):
		if value > 0:
			instance.__dict__[self.storage_name] = value
		else:
			raise ValueError('value must be > 0')


class LineItem:
	weight = Quantity('weight')
	price = Quantity('price')

	def __init__(self, description, weight, price):
		self.description = description
		self.weight = weight
		self.price = price

	def subtotal(self):
		return self.weight * self.price

# instance.__dict__[self.storage_name] = value
# the tempting but bad alternative would be:
# self.__dict__[self.storage_name] = value

# To understand why this would be wrong, think about the meaning of the first two arguments
# to __set__: self and instance. Here, self is the descriptor instance, which is actually a
# class attribute of the managed class. You may have thousands of LineItem instances in memory
# at one time, but you’ll only have two instances of the descriptors: LineItem.weight and
# LineItem.price. So anything you store in the descriptor instances themselves is actually
# part of a LineItem class attribute, therefore it is shared among all LineItem instances

# Overriding descriptor/data descriptors
# A descriptor that implements the __set__ method it called an overriding descriptor, because
# although it is a class attribute, a descriptor implementing __set__ will override attempts to
# assign to instance attributes. Properties are also overriding descriptors: if you don’t provide
# a setter function, the default __set__ from the property class will raise AttributeError to
# signal that the attribute is read-only

# Overriding descriptor without __get__/data descriptors without __get__
# Usually, overriding descriptors implement both __set__ and __get__, but it’s also possible to
# implement only __set__. In this case, only writing is handled by the descriptor. Reading the
# descriptor through an instance will return the descriptor object itself because there is no
# __get__ to handle that access. If a namesake instance attribute is created with a new value via
# direct access to the instance __dict__, the __set__ method will still override further attempts
# to set that attribute, but reading that attribute will simply return the new value from the
# instance, instead of returning the descriptor object. In other words, the instance attribute
# will shadow the descriptor, but only when reading

# Non-overriding descriptor/non-data descriptors
# If a descriptor does not implement __set__, then it’s a non-overriding descriptor. Setting an
# instance attribute with the same name will shadow the descriptor, rendering it ineffective for
# handling that attribute in that specific instance. Methods are implemented as non-overriding
# descriptors

# The bound method object also has a __call__ method, which handles the actual invocation. This
# method calls the original function referenced in __func__, passing the __self__ attribute of the
# method as the first argument. That’s how the implicit binding of the conventional self argument
# works



# Implement advanced attribute access patterns like 'cached fields'
# lazy evaluation
class LazyProperty(object):

	def __init__(self, func):
		self._func = func
		self.__name__ = func.__name__

	def __get__(self, instance, klass):
		print('Called the func')
		result = self._func(instance)
		instance.__dict__[self.__name__] = result
		return result

class MyClass(object):

	@LazyProperty
	def x(self):
		return 42

m = MyClass()
m.x
m.x



# Descriptor usage tips
# 1. Use property to keep it simple
# The property built-in actually creates overriding descriptors implementing both
# __set__ and __get__, even if you do not define a setter method. The default __set__
# of a property raises AttributeError: can't set attribute, so a property is the easiest
# way to create a read-only attribute, avoiding the issue described next

# 2. Read-only descriptors require __set__
# If you use a descriptor class to implement a read-only attribute you must remember to
# code both __get__ and __set__, otherwise setting a namesake attribute on an instance
# will shadow the descriptor. The __set__ method of a read-only attribute should just
# raise AttributeError with a suitable message

# 3. Validation descriptors can work with __set__ only
# In a descriptor designed only for validation, the __set__ method should check the value
# argument it gets, and if valid, set it directly in the instance __dict__ using the descriptor
# instance name as key. That way, reading the attribute with the same name from the instance
# will be as fast as possible, as it will not require a __get__

# 4. Caching can be done efficiently with __get__ only
# If you code just the __get__ method you have a non-overriding descriptor. These are useful to
# make some expensive computation and then cache the result by setting an attribute by the same
# name on the instance. The namesake instance attribute will shadow the descriptor, so subsequent
# access to that attribute will fetch it directly from the instance __dict__ and not trigger the
# descriptor __get__ anymore

# 5. Non-special methods can be shadowed by instance attributes
# Because functions and methods only implement __get__, they do not handle attempts at setting
# instance attributes with the same name, so a simple assignment like my_obj.the_method = 7 means
# that further access to the_method through that instance will retrieve the number 7 — without
# affecting the class or other instances. However, this issue does not interfere with special
# methods. The interpreter only looks for special methods in the class itself, in other words,
# repr(x) is executed as x.__class__.__repr__(x), so a __repr__ attribute defined in x has no effect
# of repr(x). For the same reason, the existence of an attribute named __getattr__ in an instance
# will not subvert the usual attribute access algorithm










# Function Factories, Closures and Decorators

# Function Factories - function that returns new, specialized functions
def sequence_class(immutable):
	if immutable:
		cls = tuple
	else:
		cls = list
	return cls

seq = sequence_class(immutable=True)
print(seq("ivy"))





# Closures (functions with state) - maintain reference to objects from earlier scopes
# A closure is a function that has access to variables in an enclosing scope, which has
# completed its execution. This means that referenced objects are kept alive until the
# function is in memory.
# We can do the same by creating a class and using the instance object to save state.
# e.g. __init__ and __call__
def raise_to(exp):
	y = 0
	def raise_to_exp(x):
		return pow(x, exp) - y
	return raise_to_exp

square = raise_to(2)
# show 2 values remembered by fun, exp and y
print(square.__closure__)
print(square(11))


import time
def make_timer():
	last_called = None

	def elapsed():
		nonlocal last_called
		now = time.time()
		if last_called is None:
			last_called = now
			return None
		result = now - last_called
		last_called = now
		return result

	return elapsed

t1 = make_timer()
print(t1())
time.sleep(3)
print(t1())





# Decorator is a function that creates a wrapper around another function
# Decorators - modify or enhance functions without changing their definition
# Function decorators are executed as soon as the module is imported,
# but the decorated functions only run when they are explicitly invoked
def escape_unicode(func):
	def wrap(*args, **kwargs):
		x = func(*args, **kwargs)
		return ascii(x)

	return wrap

# equivalent using class as decorator
# class escape_unicode:
#   def __init__(self, f):
#       self.f = f

#   def __call__(self, *args, **kwargs):
#       x = self.f(*args, **kwargs)
#       return ascii(x)

@escape_unicode
def string(s):
	return s

# the same as
# string = escape_unicode(string)

print(string("ałó€"))



# Decorating Callables
def closure_deco(prefix):
	def deco(func):
		return lambda x:x+prefix
return deco

@closure_deco(2)
def func(x):
	return x



# Class Decorators
class CallCount:
	def __init__(self, f):
		self.f = f
		self.count = 0

	def __call__(self, *args, **kwargs):
		self.count += 1
		return self.f(*args, **kwargs)

@CallCount
def hello(name):
	return('Hello, {}'.format(name))

print(hello('John'))
print(hello('Ivy'))
print(hello.count)
print(hello.f.__name__)



# Class instance as decorator(in __call__ method we have decorator)
@AnotherDec()



# Multiple decorators
# decorator3 will return callable to decorator2, and decorator 2 will return callable to decorator 1
@decorator1
@decorator2
@decorator3
def some_function():
	pass



# "Decorator with argument"
# Factory functions which produce decorator functions which make
# wrapper functions which wrap functions(with added closures)
def check_non_negative(index):
	def validator(f):
		def wrap(*args):
			if args[index] < 0:
				raise ValueError(
					'Argument {} must be non-negative.'.format(index))
			return f(*args)
		return wrap
	return validator

@check_non_negative(1)
def creat_list(value, size):
	return [value] * size

print(creat_list('a', 3))
print(creat_list(123, -6))



# Important metadata with Decorators
# functools.wrap() - naive decorators can lose important metadata
#                    e.g. fun.__doc__, fun.__name__
import functools

def doc(func):
	@functools.wraps(func)
	def wrapper():
		return func()
	return wrap

@doc
def hello():
	"Print a well-known message."
	print('Hello, world!')










# Context Manager

# An object designed to be used in a with-statement. A context-manager
# ensures that resources are properly and automatically managed
# e.g try, finally statement

# Context-Manager Protocol
# (__enter__(self), __exit__(self, exception_type, exception_value, exception_traceback))

1. with expression
2. context-manager
3. __enter__()          # The return value of expression.__enter__() is bound to 'x',
4. as x:                # not the value of expression
5. body
6. __exit__()           # Exception information is passed to __exit__()


class LoggingContextManager:
	def __enter__(self):
		print('LoggingContextManager.__enter__()')
		return 'You are in a with-block!'

	def __exit__(self, exc_type, exc_val, exc_tb):
		print('LoggingContextManager.__exit__({}, {}, {})'. format(
			exc_type, exc_val, exc_tb))
		return
		# if __exit__() return False, the exception is propagated,
		# if returns True, __exit__() will swallow exceptions


with LoggingContextManager() as x:
	# raise ValueError('Something has gone wrong!')
	print('=====', x, '=====', sep='\n')





# Context manager with contextlib decorator
# Automatically deleted temp directories

import tempfile
import shutil
from contexlib import contextmanager

class TempDir:
	def __enter__(self):
		self.dirname = tempfile.mkdtemp()
		return self.dirname

	def __exit__(self, exc, val, tb):
		shutil.rmtree(self.dirname)

with TempDir() as dirname:
	...


# Its the same code, glued together differently
@contextmanager
def temp_dir():
	dirname = tempfile.mkdtemp()
	try:
		yield dirname
	except Exception:
		raise
		# if raise, exception will be raise,
		# if not exception wont be propagated
	finally:
		shutil.rmtree(dirname)





# Multiple context managers
@contextlib.contextmanager
def nest_test(name):
	print('Entering', name)
	yield name
	print('Exiting', name)


with nest_test('outer') as n1, nest_test('inner, nested in ' + n1):
	print('BODY')

# The same as
with nest_test('outer'):
	with nest_test('inner'):
		print('BODY')

# Opening url and writing to new file
with urlopen(url) as remote, open(file_name, 'wb') as local:
	local.write(remote.read())










# Super

# return a proxy object that delegates method calls to a parent or sibling class of type

# inheritance(dziedziczenie)
# tool for code reused, share implementation, one class use code from another class

# super() mean => NEXT IN LINE, not call your parents
# children before parents, parents stay in order - remember the line order - help(obj)

# use self - starting over again from begining,
# use super - next in line

# super with args - only in python2, python3 do it on its own.
# super(who do we looking, from who do we start)
super(Class_Name, self).__init__(*args, **kwargs)   # python 2
super().__init__(*args, **kwargs)                   # python 3

# super(Base, Derived) => class super proxy
# super(Base, self) => instance super proxy


# The tuple of base classes of a class object
Class_Name.__bases__

# Method Resolution Order, information about linear order of the inheritance(super())
Class_Name.__mro__ == Class_Name.mro()










# __slots__
# special attribute (not a method) that affects the internal storage of an object, with potentially
# huge impact on the use of memory(removing dict) but little effect on its public interface

# Using a dictionary for attribute storage is very convenient, but it can mean a waste of space for objects,
# which have only a small amount of instance variables. The space consumption can become critical when creating
# large numbers of instances. Slots are a nice way to work around this space consumption problem.
# Instead of having a dynamic dict that allows adding attributes to objects dynamically,
# slots provide a static structure which prohibits additions after the creation of an instance

class S:
	# assign iterable of str with identifiers for the instance attributes
	__slots__ = ('val')

	def __init__(self, v):
		self.val = v

s = S(7)
print(s.val)
s.x = 1                         # AttributeError: 'S' object has no attribute 'x'










# Special methods

# __init__ and __new__

# __new__() and __init__() work together in constructing objects,
# __new__() to create an instance, then __init__() to customize it,
# no non-None value may be returned by __init__()

# __new__ is (special)static class method, while __init__ is instance method
# __new__ has to create the instance first, so __init__ can initialize it

# Even if __init__ fails, class call its __del__ method
class Card(object):
	def __init__(self, number, color, soft, hard):
		self.number = number
		self.color = color
		self.soft = soft
		self.hard = hard

class AceCard(Card):
	avaiable_objects = 4

	# args and kwargs are used when initializing class
	def __new__(cls, *args, **kwargs):
		if not cls.avaiable_objects:
			raise ValueError("Cannot crate more objects")
		cls.avaiable_objects -= 1
		return super(AceCard, cls).__new__(cls)

	def __init__(self, number, color, **kwargs):
		super().__init__(number, color, 11, 1)
		# remember additional kwargs
		self.__dict__.update(kwargs)


a = AceCard(3, "spade", name="Ivy")
print(a.number, a.color, a.soft, a.hard, a.__dict__)





# __call__

# called when the instance is 'called' as a function (callable instances)
import socket

class Resolver:

	def __init__(self):
		self._cache = {}

	def __call__(self, host):
		if host not in self._cache:
			self._cache[host] = socket.gethostbyname(host)
		return self._cache[host]


a = Resolver()
a("python.org")
a("nba.com")
print(a._cache)





# __bool__

# called to implement truth value testing and the built-in operation bool()
# should return False or True
# we can use it with 'if' or 'while', or as operands to 'and', 'or' and 'not'
# if a class defines neither __len__() nor __bool__(), all its instances are considered true
class RandomList(object):
	def __init__(self):
		self._list = list(range(10))

	def __bool__(self):
		return bool(self._list)

	def pop_item(self):
		return self._list.pop()


rl = RandomList()
while rl:
	item = rl.pop_item()





# __str__, __repr__ and __format__

# __repr__, called by the repr() built-in function to compute the 'official' string
# representation of an object. if at all possible, this should look like a valid python
# expression that could be used to recreate an object with the same value

# __str__, called by str(object) and the built-in functions format() and print()
# to compute the 'informal' or nicely printable string representation of an object

# if you only implement one of these special methods, choose __repr__

# __format__, called by the format() built-in function, and the str.format() method
class Unit:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	# readable, human-friendly representation of an object
	def __str__(self):
		return "Class dict: {x} and {y}".format(**self.__dict__)

	# debug-friendly, logging representation of an object
	def __repr__(self):
		return '{}(x={}, y={})'.format(self.__class__.__name__, self.x, self.y)

	def __format__(self, f):
		custom_formating = {'a': 'custom format a', 'b': 'custom format b', 'c': 'custom format c'}
		return custom_formating.get(f, 'no custom format avaiable')


a = Unit(3, 7)
print("{0!s},\n{0!r},\n{0:a},\n{0:b},\n{0:d}".format(a))





# __missing__

# called by dict.__getitem__() to implement self[key] for dict subclasses
# when key is not in the dictionary
	def __missing__(self, key):
		return 0





# __reduce__

# __reduce__() method is used by pickle and takes no argument and shall return a tuple, with:
#   a callable object that will be called to create the initial version of the object(e.g. self.__class__)
#   tuple of arguments for the callable object. An empty tuple must be given if the callable does not accept any argument

from collections import OrderedDict, Counter
import pickle

class OrderedCounter(Counter, OrderedDict):

	def __repr__(self):
		return '{} {}'.format(self.__class__.__name__, OrderedDict(self))

	def __reduce__(self):
		return (self.__class__, (OrderedDict(self),))


pickle.dumps(OrderedCounter('abracaadabra'))
pickle.loads(pickled_obj)





# __getattr__, __setattr__ and __delattr__

# dynamic attribute access
# The __getattr__ method is invoked by the interpreter when attribute lookup fails. In simple terms,
# given the expression my_obj.x, python checks if the my_obj instance has an attribute named x; if not,
# the search goes to the class (my_obj.__class__), and then up the inheritance graph. If the x attribute
# is not found, then the __getattr__ method defined in the class of my_obj is called with self and the
# name of the attribute as a string, e.g. 'x'.

# The expressions obj.attribute_name, getattr(obj, 'attribute_name') and hasattr(obj, 'attribute_name')
# may trigger Class.__getattr__(obj, 'attribute_name'), but only if an attribute by that name cannot
# be found in obj or in Class and its superclasses

class CustomAccess:

	def __init__(self):
		# prevents infinite recursion from self.data = {'a': 3, 'b': 7}
		self.__dict__['data'] = {'a': 3, 'b': 7}

	def __getattr__(self, name):
		try:
			return self.data[name]
		except KeyError:
			raise AttributeError("attribute doesn't exist")

	def __setattr__(self, name, value):     
		self.data[name] = value
		# raise AttributeError("can't set attribute")

	def __delattr__(self, name):
		try:
			del self.data[name]
		except KeyError:
			raise AttributeError("attribute doesn't exist")

ca = CustomAccess()
ca._n = 9
del ca.a
print(ca.data, ca.b)



# A read-only façade for navigating a JSON-like object using attribute notation
from collections import abc
from keyword import iskeyword

class FrozenJSON:

	def __new__(cls, arg):
		if isinstance(arg, abc.Mapping):
			return super().__new__(cls)
		elif isinstance(arg, abc.MutableSequence):
			return [cls(item) for item in arg]
		else:
			return arg

	def __init__(self, mapping):
		self._data = {}
		for key, value in mapping.items():
			if iskeyword(key):
				key += '_'
			self._data[key] = value

	def __getattr__(self, name):
		if hasattr(self._data, name):
			# searching for method object e.g dict.keys()
			return getattr(self._data, name)
		else:
			return FrozenJSON(self._data[name])

example = {
	'a':
		{
		'di': {'not': 'a nice string', 'ivy': (33, -11, 77)},
		'li': [-1, -7, 'a', 'r', 6]
		},
	'b': 5,
	'c': [3, 7],
}

fj = FrozenJSON(example)
print(fj.a.di.not_, fj.a.di.keys())



# A key difference between __getattr__ and __getattribute__ is that __getattr__ is only invoked if the attribute
# wasn't found the usual ways. It's good for implementing a fallback for missing attributes, and is probably the
# one of two you want. __getattribute__ is invoked before looking at the actual attributes on the object, and so can
# be tricky to implement correctly. You can end up in infinite recursions very easily

# __getattribute__(self, name)
# Always called when there is an attempt to retrieve the named attribute, except when the attribute sought is a
# special attribute or method. Dot notation and the gettattr and hasattr built-ins trigger this method.
# __getattr__ is only invoked after __gatattribute__, and only when __gatattribute__ raises AttributeError.
# To retrieve attributes of the instance obj without triggering an infinite recursion, implementations of
# __getattribute__ should use super().__getattribute__(obj, name)





# Collection Protocol
from collections.abc import Set
from itertools import chain
try:
	from _bisect import *
except ImportError:
	pass

# Immutable sorted set
class SortedSet(Set):

	def __init__(self, items=None):
		self._items = sorted(set(items)) if items is not None else []

	def __repr__(self):
		return "SortedSet({})".format(self._items if self._items else '')

# Container protocol:
# Membership testing using 'in' and 'not in'

	def __contains__(self, item):
		try:
			self.index(item)
			return True
		except ValueError:
			return False

# Sized protocol:
# Determine number of elements with len(s)

	def __len__(self):
		return len(self._items)             # return non negative integer


# Sequence protocol:
# Retrive elements by index and slices by slicing

	def __getitem__(self, index):
		cls = type(self)
		if isinstance(index, slice):
			return cls(self._items[index])
		elif isinstance(index, numbers.Integral):
			return self._items[index]
		else:
			raise TypeError('{cls.__name__} indices must be integers'.format(cls=cls))

	# def __setitem__(self, index, value):
	# def __delitem__(self, index):

# Equality and inequality protocol(default behavior is to comparing objects id's):
# Testing using '=='

	def __eq__(self, rhs):
		if not isinstance(rhs, SortedSet):
			return NotImplemented           # Not, raise NotImplementedError
			# NotImplemented signals to the runtime that it should ask someone else to satisfy the operation.
			# In the expression a == b, if a.__eq__(b) returns NotImplemented, then Python tries b.__eq__(a).
			# If b knows enough to return True or False, then the expression can succeed. If it doesn't,
			# then the runtime will fall back to the built-in behavior (which is based on identity for == and !=)
		return self._items == rhs._items
		# return len(self) == len(other) and all(a == b for a, b in zip(self, other))           # + __iter__


# Testing using '!='

	def __ne__(self, rhs):
		if not isinstance(rhs, SortedSet):
			return NotImplemented           # Not, raise NotImplementedError
		return self._items != rhs._items


# Hashable object
# An object is hashable if it has a hash value which never changes during its lifetime (it
# needs a __hash__() method), and can be compared to other objects (it needs an
# __eq__() method). Hashable objects which compare equal must have the same hash value

	def __hash__(self):
		return reduce(lambda x, y: xor(hash(x), hash(y)), self._items)
		# tuple is immutable but not always hashable:
		# tt = (1, 2, (30, 40))
		# hash(tt)
		# tl = (1, 2, [30, 40])
		# hash(tl)                      # TypeError: unhashable type: 'list'


# Iterable protocol:

	def __iter__(self):
		return iter(self._items)


# Operator overloading
# stick to the fundamental rule of operators: always return a new object
# in other words, do not modify self, but create and return a new instance of a suitable type

# Concatenation with + operator

	def __add__(self, rhs):
		return SortedSet(chain(self._items, rhs._items))
	# __radd__ = __add__

# Repetition with * operator

	def __mul__(self, rhs):
		return self if rhs > 0 else SortedSet()

# Reversed multiplication
	def __rmul__(self, lhs):
		return self * lhs
	# __rmul__ = __mul__

# KlassA * KlassB
# KlassA.__mul__(self, rhs) => KlassB.__rmul__(self, lhs)

# Arithmetic unary negation
	def __neg__(self):
		return SortedSet(-i for i in self._items)

# prefix 'i' - inplace operators(or augmented), e.g. __iadd__, +=
# very important: augmented assignment special methods must return self


# Set protocol:
# Set algebra operations(rest inheritate from Set)
	
	def issubset(self, iterable):
		return self <= SortedSet(iterable)

	def issuperset(self, iterable):
		return self >= SortedSet(iterable)

	def intersection(self, iterable):
		return self & SortedSet(iterable)

	def union(self, iterable):
		return self | SortedSet(iterable)

	def symetric_difference(self, iterable):
		return self ^ SortedSet(iterable)

	def difference(self, iterable):
		return self - SortedSet(iterable)

# Find index by item

	def index(self, item):
		# Binary search (Logarithmic complexity)
		index = bisect_left(self._items, item)
		if (index != len(self._items)) and (self._items[index] == item):
			return index
		raise ValueError('{} not found'.format(item))

		# Linear complexity
		# for i, v in enumerate(self._items):
		#   if v == value:
		#       return i
		# raise ValueError

# Count items

	def count(self, item):
		# Binary search (Logarithmic complexity)
		return int(item in self)
		# Linear complexity
		# return sum(1 for v in self._items if v == item)

# Produce a reversed sequence, reversed(seq)
# If special method __reversed__() is not implemented then it
# fallback to __getitem__() and __len__() methods


s = SortedSet(range(20, 30))
r = SortedSet(range(10))

print(25 in s, 7 not in r, -s, s.count(23), s.index(29), 3*r, r + s, r.intersection(s), s^r, sep='\n')










# Metaprogramming

# Class decorators are a simpler way of doing something that previously required a metaclass:
# customizing a class the moment it’s created

# At import time, the interpreter parses the source code of a .py module in one pass from top
# to bottom, and generates the bytecode to be executed. That’s when syntax errors may occur. If
# there is an up-to-date .pyc file available in the local __pycache__, those steps are skipped
# because the bytecode is ready to run

# Border between 'import time' and 'run time' is fuzzy: the import statement can trigger all
# sorts of 'run time' behavior

# In the usual case, interpreter defines top level functions at import time, but executes their
# bodies only when — and if — the functions are invoked at run time

# For classes, the story is different: at import time, the interpreter executes the body of every
# class, even the body of classes nested in other classes. Execution of a class body means that
# the attributes and methods of the class are defined, and then the class object itself is built.
# In this sense, the body of classes is 'top level code': it runs at import time

# Everything is executed at the module level when python first imports a module. Function bodies
# (and generator expression bodies) are the exception here, not the rule. Python executes everything
# to create the objects contained in a module; like everything in python, classes are objects, and
# so are functions. The only reason a class body uses a separate code object is because a class body
# is executed in a separate namespace, with that namespace then forming the class attributes. Class
# bodies are not the only such namespaces; set and dict comprehensions, and in Python 3, list
# comprehensions are also executed with a separate namespace, scoping their locals. So functions and
# generator expressions are the exception, expressly because their whole purpose is to be executed
# at a later time. Note that the function definition is executed

# A metaclass is a class factory, except that instead of a function, a metaclass is written as a class

# The class object and type have a unique relationship: object is an instance of type, and type
# is a subclass of object. This relationship is 'magic': it cannot be expressed in python because
# either class would have to exist before the other could be defined. The fact that type is an
# instance of itself is also magical

# Every class is an instance of type, directly or indirectly, but only metaclasses are also
# subclasses of type

# The important takeaway here is that all classes are instances of type, but metaclasses are also
# subclasses of type, so they act as class factories. In particular, a metaclass can customize its
# instances by implementing __init__. A metaclass __init__ method can do everything a class decorator
# can do, but its effects are more profound

import collections

class MetaAleph(type):

	@classmethod
	def __prepare__(cls, name, bases):
		return collections.OrderedDict()

	def __init__(cls, name, bases, dic):
		def inner_2(self):
			return 'inner_2'

		cls.method_z = inner_2


class ClassFive(metaclass=MetaAleph):

	def __init__(self):
		pass

	def method_z(self):
		return 'method_z'


cf = ClassFive()
print(cf.method_z())

# When coding a metaclass, it’s conventional to replace self by cls. For example, in the __init__
# method of the metaclass, using cls as the name of the first argument makes it clear that the
# instance under construction is a class

# The body of __init__ defines an inner_2 function, then binds it to cls.method_z. The name cls
# in the signature of MetaAleph.__init__ refers to the class being created, e.g. ClassFive. On the
# other hand, the name self in the signature of inner_2 will eventually refer to an instance of the
# class we are creating, e.g. an instance of ClassFive

# The __prepare__ method is invoked by the interpreter before the __new__ method in the metaclass
# to create the mapping that will be filled with the attributes from the class body

# Class metaprogramming is about creating or customizing classes dynamically. Classes in python are
# first-class objects, class can be created by a function invoking the type built-in metaclass

# Metaclasses are used in frameworks and libraries that help programmers perform, among other tasks:
# • attribute validation;
# • applying decorators to many methods at once;
# • object serialization or data conversion;
# • object-relational mapping;
# • object-based persistency;
# • dynamic translation of class structures from other languages
