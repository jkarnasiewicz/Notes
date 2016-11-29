# Classes, Function Factories, Decorators and Special Methods

# Callable objects: regular functions, lambdas expressions, classes(constructor),
# methods, instance objects with __call__

# Functions can be treated like any other objects

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










# Properties

# @property is read only
# gracefully convert public attributes to private
# property function, property(fget=None, fset=None, fdel=None, doc=None)
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










# Descriptors

# Descriptors - customized processing of attribute access (dostosowany/zindywidualizowany proces dostępu do atrybutu)
# Descriptor is an object attribute with 'binding behavior'(wiążącym zachowaniem),
# one whose attribute access has been overridden by methods in the descriptor protocol.
# Those methods are __get__(), __set__(), and __delete__().
# If any of those methods are defined for an object, it is said to be a descriptor.

# Descriptor works only in a class. Storing attribute data directly in a descriptor means sharing between instances

# Descriptors are a great solutions for attributes with common behavior across multiple classes
# - reusable propertise (e.g. database fields, attached to many different classes with many different names)

# Descriptors are the mechanism behind properties, methods, static methods, class methods, and super()



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
# (It is an easier way to create iterators using a keyword yield from a function)

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
# ===================================

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
def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
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










# Special methods

# __init__ and __new__

# __new__() and __init__() work together in constructing objects,
# __new__() to create it, and __init__() to customize it,
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

    # args and kwargs are from initialiazing class
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
        return self._items[index]

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


# Testing using '!='

    def __ne__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented           # Not, raise NotImplementedError
        return self._items != rhs._items

# Concatenation with + operator

    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs._items))

# Repetition with * operator

    def __mul__(self, rhs):
        return self if rhs > 0 else SortedSet()

    # Reversed multiplication
    def __rmul__(self, lhs):
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

# Iterable protocol:

    def __iter__(self):
        return iter(self._items)

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

print(25 in s, 7 not in r, s.count(23), s.index(29), 3*r, r + s, r.intersection(s), s^r, sep='\n')
