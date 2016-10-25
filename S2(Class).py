# Classes, Function Factories, Decorators
# Callable objects: regular functions, lambdas expressions, classes(constructor),
# 					methods, instance objects with __call__

# Functions can be treated like any other objects

# @staticmethod - without 'self' in method args. Code organization(like free function)
# @classmethod - first arg 'cls'. Refere to class object within the method class, e.g. class attribute
import random
class ShippingContainer:
    next_serial = 1337						# Class attribute

    @staticmethod							# Static method
    def get_code(owner, serial):
        return '{0}/{1}/{2}'.format(owner.upper(), random.randint(0, 100), serial)

    @classmethod							# Class method
    def get_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty_container(cls, owner):
        return cls(owner, content=None)		# Create new Class Instance

    def __init__(self, owner, content):
        self.owner = owner					# Instance attribute
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




# __init__, and super().__init__
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




# __call__ - callable instances(like the functions)
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
print("{0!s}, and {0!r}".format(a))         # format default calls __str__




# __bool__
class RandomList:
    def __init__(self):
        self._list = range(10)

    def __bool__(self):
        return bool(self._list)

    def pop_item(self):
        return self._list.pop()

# e.g. we can use it with 'if', 'while'
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
# Testing using '=='(is)

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

# Iterable protocol:
# Can produce an iterator with iter

    def __iter__(self):
        return iter(self._items)
        # for i in self._items:
        #   yield i

# __iter__ method is called on initialization of an iterator.
# This should return an object that has a next method
# (In python 3 this is changed to __next__)
# class Fib:                                       
#     def __iter__(self):                          
#         self.a = 0
#         self.b = 1
#         return self

#     def next(self):                          
#         ...
#         if self.index >= len(self.data):
#             raise StopIteration
#         ...


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
# If sepcial method __reversed__() is not implemented then it
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










# Iterators and Generators

# Iterable object - Objects which can be used with a for loop.
#                   There are many functions which consume these iterables, e.g. join, list.

# iter(callable, sentinel) - The built-in function iter takes an iterable object and returns an iterator.(no args callable)
with open('some_file.txt', 'rt') as f:
  for line in iter(lambda: f.readline().split(), 'END'):
      print(line)


# reading big file
f = open('really_big_file.dat')
def read1k():
    return f.read(1024)

for piece in iter(read1k, ''):
    process_data(piece)


# Iterators are implemented as classes.
# Iterable protocol(__iter__, __next__ and raise StopIteration())
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


# Generators simplifies creation of iterators.
# A generator is a function that produces a sequence of results instead of a single value.
import random

def generator():
    while True:                     # infinite loop
        yield random.random()

gen = generator()
print(next(gen))










# Super()

# inheritance(dziedziczenie) - tool for code reused, share implementation,
#                              one class use code from another class
#                              children before parents, parents stay in order - remember the line order - help(obj)
#                              super() mean => NEXT IN LINE, not call your parents
#                              use self - starting over again from begining,
#                              use super - next in line
# super with args - only in python2, python3 do it on its own. super(who do we looking, from who do we start)
super(Class_Name, self).__init__(*args, **kwargs)   # python 2
super().__init__(*args, **kwargs)                   # python 3

# super(Base, Derived) => class super proxy
# super(Base, self) => instance super proxy

# Class_Name.__bases__,

# Method Resolution Order
# Class_Name.__mro__ == Class_Name.mro()    # info about linear order of the inheritance(super())

from collections import OrderedDict, Counter

class OrderedCounter(Counter, OrderedDict):

  def __repr__(self):
      return '{} {}'.format(self.__class__.__name__, OrderedDict(self))

  def __reduce__(self):
      return self.__class__, (OrderedDict(self),)

oc = OrderedCounter('abracaadabra')
print('{}'.format(oc))











# Interface

# Abstract classes are available via the standard abc library package.
# They are useful for the definition of interfaces and common functionality

from abc import ABCMeta, abstractmethod
class Worker(metaclass=ABCMeta):

    @abstractmethod
    def do(self, func, args, kwargs):
        "work on function"

    @abstractmethod
    def is_busy(self,):
        "tell if busy"























# Properties
class Example:

    def __init__(self, foo):
        self.foo = foo

    @property
    def foo(self):
        print('prop')
        return self._foo

    @foo.setter
    def foo(self, value):
        print('set')
        self._foo = value
















# Design Patterns
# Each pattern describes a problem, which occurs over and over again in our environment,
# and then describes the core of the solution to that problem in such a way that you can
# use this solution a million times over, without ever doing it the same way twice

# In the world of software, the term design pattern refers to a general repeatable
# solution to a commonly occurring problem in software design





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
    #   return getattr(self.fish,attr)

# Facade pattern - Hiding system complexity for a simpler interface

# Flyweight pattern - Consuming less memory with shared objects

# Command pattern - Easy-execution management for commands (83 Python Unlock)

# Abstract factory
# class Animal(six.with_metaclass(abc.ABCMeta, object)):
#   """ clients only need to know this interface for animals"""
#   @abc.abstractmethod
#   def sound(self, ):
#       pass

# Registry pattern - Adding functionality from anywhere in code to class

# State pattern - Changing execution based on state










# TO DO
atrybut, właściwość, metoda



