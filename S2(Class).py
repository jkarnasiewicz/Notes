# Classes, Function Factories, Decorators, Special Methods

# Callable objects: regular functions, lambdas expressions, classes(constructor),
# methods, instance objects with __call__

# Functions can be treated like any other objects

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

    def __init__(self, owner, content):     # ? instance method
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





# Properties

# @property is read only
# gracefully convert public attributes to private
class Example:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
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





# Interface

# abstract classes are available via the standard abc library package
# they are useful for the definition of interfaces and common functionality

from abc import ABCMeta, abstractmethod
class Worker(metaclass=ABCMeta):

    @abstractmethod
    def do(self, func, args, kwargs):
        "work on function"

    @abstractmethod
    def is_busy(self,):
        "tell if busy"





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





# Iterables, Iterators and Generators

# Iterables
# ===================================

# Iterable protocol
# __iter__ and __getitem__
# __iter__ method is called on initialization of an iterator, this should return an object that has a __next__ method

    def __getitem__(self, index):
        return self.sequence[index]

# Iterables are objects over which we can iterate item by item (lists, dict, strings or files)
# there are many functions which consume these iterables, e.g. join, list

# Iterable objects can be passed to the built-in iter() function to get an iterator
# iterator = iter(iterable)

    def __iter__(self):
        return iter(self._items)

# or
# iterator = iter(callable, sentinel) - callable without arguments

with open('some_file.txt', 'rt') as f:
  for line in iter(lambda: f.readline().split(), 'END'):
      print(line)





# Iterators
# ===================================

# Iterator protocol
# __iter__ and __next__ with raise StopIteration()

# we retrive an iterator from an iterable object using the built-in iter() function
# iterators produce items one-by-one from the underlying iterable series each time
# they are passed to the built-in next() function

# Iterator objects can be passed to build-in next() function to fetch the next item
# item = next(iterator)

class Sensor:

    def __iter__(self):
        return self

    def __next__(self):
        return random.random()

sensor = Sensor()
timstamps = iter(datetime.datetime.now, None)

for stamp, value in itertools.islice(zip(timstamps, sensor), 10):
    print(stamp, value)
    time.sleep(3)





# Generators
# ===================================

# Generators simplifies creation of iterators

# Generators are defined by any python function witch using the 'yield' keyword at least once in it's definition
# (produces a sequence of results instead of a single value)

# All generators are iterators, when advanced with next() the generator starts or resumes
# execution up to and including the next yield

# Generators are lazily evaluated - the next value in the sequence is computed on demand
# (can model infinite sequence - such as data streams with no definite end)

# When a generator function is called, it returns a generator object without
# even beginning execution of the function. When next method is called for the first time,
# the function starts executing until it reaches yield statement.
# The yielded value is returned by the next call.

import random

def generator():
    while True:
        yield random.random()

gen = generator()
print(next(gen))

# Generators provide a convenient way to implement the iterator protocol,
# if a container object’s __iter__() method is implemented as a generator,
# it will automatically return an iterator object

    def __iter__(self):
        for i in self._items:
            yield i

# Generators comprehensions/generator expressions
(expr(item) for item in iterable)

# Stateful generators:
#   generators resume execution
#   can maintain state in local variables
#   complex control flow
#   lazy evaluation



# Comparison
# Both iterables and generators produce an iterator

# The difference between iterables and generators:
#   once you’ve burned through a generator, you’re done, no more data: 

generator = (word + '!' for word in 'baby let me iterate ya'.split())

# real processing happens during iteration
for val in generator:
    print(val)

# nothing printed, no more data, generator stream already exhausted above
for val in generator:
    print(val)


# On the other hand, an iterable creates a new iterator every time it’s looped over
# (technically, every time iterable.__iter__() is called, such as when Python hits a 'for' loop): 

class BeyonceIterable(object):
    def __iter__(self):
        """
        The iterable interface: return an iterator from __iter__()
 
        Every generator is an iterator implicitly (but not vice versa!),
        so implementing '__iter__' as a generator is the easiest way
        to create streamed iterables
 
        """
        for word in 'baby let me iterate ya'.split():
            yield word + '!'


iterable = BeyonceIterable()

# iterator created here
for val in iterable:
    print(val)

# another iterator created here
for val in iterable:
    print(val)


# So iterables are more universally useful than generators, because we can go over the sequence more than once
# Of course, when your data stream comes from a source that cannot be readily repeated (such as hardware sensors),
# a single pass via a generator may be your only option































































































# __missing__
# called by dict.__getitem__() to implement self[key] for dict subclasses
# when key is not in the dictionary
    def __missing__(self, key):
        return 0





# __reduce__
# __reduce__ is used by pickle
# __reduce__() method takes no argument and shall return a tuple, with:
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





# __init__ and __new__
# because __new__() and __init__() work together in constructing objects (__new__() to create it, and __init__() to customize it),
# no non-None value may be returned by __init__()

# Even if __init__ fails, class call its __del__ method
class Card:
    def __init__(self, number, color, soft, hard):
        self.number = number
        self.color = color
        self.soft = soft
        self.hard = hard

class AceCard(Card):
    def __init__(self, number, color, **kwargs):
        super().__init__(number, color, 11, 1)
        self.__dict__.update(kwargs)


a = AceCard(3, "spade", name="Ivy")
print(a.number, a.color, a.soft, a.hard, a.name, a.__dict__)





# __call__
# callable instances(like the functions)
import socket

class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]


a = Resolver()
a("wp.pl")
a("nba.com")
print(a._cache)





# __str__, and __repr__
class Unit:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):                      # readable, human-friendly representation of an object
        return "Class dict: {x} and {y}".format(**self.__dict__)

    def __repr__(self):                     # debug-friendly, logging representation of an object
        return '{}(x={}, y={})'.format(self.__class__.__name__, self.x, self.y)

    def __format__(self, f):
        # '{0:r}'.format(obj) => f == 'r'
        return '{}'.format()


a = Unit(3, 7)
print("{0!s}, and {0!r}".format(a))         # format calls __str__ by default





# __bool__
class RandomList:
    def __init__(self):
        self._list = range(10)

    def __bool__(self):
        return bool(self._list)

    def pop_item(self):
        return self._list.pop()

# we can use it with 'if', 'while'
rl = RandomList()
while rl:
    card = rl.pop_item()





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

# Equality and inequality protocol(default behavior is to comparing objects id's):
# Testing using '=='

    def __eq__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented           # Not, raise NotImplementedError
        return self._items == rhs._items

# Testing using '!='

    def __ne__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented           # Not, raise NotImplementedError
        return self._items != rhs._items

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
        return len(self._items)             # Non negative integer


# Sequence protocol:
# Retrive elements by index and slices by slicing

    def __getitem__(self, index):
        return self._items[index]

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

# Concatenation with + operator

    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs._items))

# Repetition with * operator

    def __mul__(self, rhs):
        return self if rhs > 0 else SortedSet()

    def __rmul__(self, lhs):        # Reversed multiplication
        return self * lhs
    # __rmul__ = __mul__

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



s = SortedSet(range(20, 30))
r = SortedSet(range(10))

print(25 in s, 7 not in r, s.count(23), s.index(29), 3*r, r + s, r.intersection(s), s^r, sep='\n')





# Context Manager

# An object designed to be used in a with-statement. A context-manager
# ensures that resources are properly and automatically managed
# e.g try, finally statement

# Context-Manager Protocol
# (__enter__(self), __exit__(self, exception_type, exception_value, exception_traceback))

1. with expression
2. context-manager
3. __enter__()          # The retur value of expression.__enter__() is bound to 'x',
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
import contextlib
import sys

@contextlib.contextmanager
def logging_context_manager():
    print('logging_context_manager: __enter__()')
    try:
        yield 'You are in a with-block!'
        print('logging_context_manager: normal exit')
    except Exception:
        print('logging_context_manager: exceptional exit',
            sys.exc_info())
        raise
        # if raise, exception will be raise,
        # if not exception wont be propagated


with logging_context_manager() as x:
    # raise ValueError('Something has gone wrong!')
    print('=====', x, '=====', sep='\n')



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
print(square.__closure__)						# show 2 values remembered by fun, exp and y
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





# Function Decorators - modify or enhance functions without changing their definition
def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap

# equivalent using class as decorator
# class escape_unicode:
# 	def __init__(self, f):
# 		self.f = f

# 	def __call__(self, *args, **kwargs):
# 		x = self.f(*args, **kwargs)
# 		return ascii(x)

@escape_unicode
def string(s):
    return s

print(string("ałó€"))



# Decorating Callables
def closure_deco(prefix):
    def deco(func):
        return lambda x:x+prefix
return deco

@closure_deco(2)
def func(x):
    ...



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



# Instance as decorators
# @AnotherDec()								# In __call__ we have decorator

# Multiple decorators(decorator3 will return callable to decorator2,
# 					  and decorator 2 will return callable to decorator 1)
# @decorator1
# @decorator2
# @decorator3
# def some_function()



# Important metadata with Decorators
# functools.wrap() - naive decorators can lose important metadata
#					 e.g. fun.__doc__, fun.__name__
import functools

def noop(f):
    @functools.wraps(f)
    def wrap():
        return f()
    return wrap

@noop
def hello():
    "Print a well-known message."
    print('Hello, world!')



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











































# def take(n, seq):
#     """Returns first n values from the given sequence."""
#     # seq = iter(seq)
#     result = []
#     try:
#       for i in range(n):
#           result.append(seq.__next__())
#     except StopIteration:
#         pass
#     return result

# print(take(15, (i for i in range(10))))


# Normal version
# def grep(pattern, filenames):
#     for f in filenames:
#         for line in open(f):
#             if pattern in line:
#                 print line,


# Generator version
# def readfiles(filenames):
#     for f in filenames:
#         for line in open(f):
#             yield line

# def grep(pattern, lines):
#     return (line for line in lines if pattern in line)

# def printlines(lines):
#     for line in lines:
#         print(line)

# def main(pattern, filenames):
#   import pdb
#   pdb.set_trace()
#   lines = readfiles(filenames) # => generator
#   lines = grep(pattern, lines) # => generator expresion
#   printlines(lines)


# main('open', [__file__])
