# -*- coding: utf-8 -*-

# eval vs exec
# django bulk_create

# Peter Norvig Design Patterns book
# The message from Peter Norvig’s design patterns slides is that the Command and Strategy
# patterns — along with Template Method and Visitor — can be made simpler or even
# “invisible” with first class functions, at least for some applications of these patterns

# Python has first-class functions and first-class types, features that Norvig claims affect
# 10 of the 23 patterns

# The authors are explicit right at the beginning of their book that
# “some of our patterns are supported directly by the less common object-oriented languages”



# Scopes
# Python does not require you to declare variables, but assumes that a variable assigned in the body of a function is local.
# This is much better than the behavior of JavaScript, which does not require variable declarations
# either, but if you do forget to declare that a variable is local (with var), you may clobber
# a global variable without knowing.

# iter(), next()
# class attribute vs instnace attribute
# __prepare__
# __getattribute__(self, name)
# __new__(cls, clsname, bases, clsdict)
# memoryview



# import inspect
# inspect.getsource(object_name)
# ? inspect.getmembers(promotions, inspect.isfunction) / (obj, filter func)
# ? inspect.isclass

# Extracting the function signature
# from inspect import signature
# sig = signature(f)
# print(sig)

# for name, param in sig.parameters.items():
#     print(param.kind, ':', name, '=', param.default)



# prefix 'i' - inplace, e.g. __iadd__


# First-Class Functions
# Functions in Python are first-class objects
# “first-class object” as a program entity that can be:
# • created at runtime;
# • assigned to a variable or element in a data structure;
# • passed as an argument to a function;
# • returned as the result of a function.



# bound vs unbound
# Unbound (class) method objects: no self
# Accessing a function attribute of a class by qualifying the class returns an unbound method object.
# To call the method, you must provide an instance object explicitly as the first argument.
# In Python 3.X, an unbound method is the same as a simple function and can be called through the class’s name;
# in 2.X it’s a distinct type and cannot be called without providing an instance.

# Bound (instance) method objects: self + function pairs
# Accessing a function attribute of a class by qualifying an instance returns a bound method object.
# Python automatically packages the instance with the function in the bound method object,
# so you don’t need to pass an instance to call the method.



# namedtuple
# namedtuple can be used to build classes of objects that are just bundles of attributes with no custom methods, like a databaserecord
# The collections.namedtuple function is a factory that produces subclasses of tuple enhanced with field names and a class name — which helps debugging
# You can access the fields by name or position

# from collections import namedtuple
# City = namedtuple('City', 'name country population coordinates')
# tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# print(tokyo)



# special methods - the Python interpreter is the only frequent caller of most special methods


# __repr__() - The string returned by __repr__ should be unambiguous and, if possible, match the source code necessary to recreate the object being represented
# representation should looks like calling the constructor of the class

# __str__- which is called by the str() constructor and implicitly used by the print function. __str__ should return a string suitable for display to end-users

# If you only implement one of these special methods, choose __repr__



# Container sequences
# list, tuple and collections.deque can hold items of different types.
# Flat sequences
# str, bytes, bytearray, memoryview and array.array hold items of one type.
# Container sequences hold references to the objects they contain, which may be of any
# type, while flat sequences physically store the value of each item within its own memory
# space, and not as distinct objects. Thus, flat sequences are more compact, but they are
# limited to holding primitive values like characters, bytes and numbers



# __next__ example
# class Sensor:

#     def __init__(self):
#         self._list = [1, 3, 5]
#         self.index = -1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         try:
#             result = self._list[self.index]
#             self.index -= 1
#         except IndexError:
#             self.index = -1
#             raise StopIteration
#         return result

#     def __next__(self):
#         'Returns the next value till current is lower than high'
#         if self.current > self.high:
#             raise StopIteration
#         else:
#             self.current += 1
#             return self.current - 1



# os.path
# _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')



# tuple unpacking
# metro_areas = [
#     ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)), #
#     ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
#     ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
# ]

# for name, cc, pop, (latitude, longitude) in metro_areas:
#     print('{:20} {}, {}'.format(name, latitude, longitude))



# bisection algorithms
# import bisect

# def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#     i = bisect.bisect(breakpoints, score)
#     return grades[i]

# print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])               # ['F', 'A', 'C', 'C', 'B', 'A', 'A']



# import array
# Return a new array whose items are restricted by typecode, and
# initialized from the optional initializer value, which must be a list,
# string or iterable over elements of the appropriate type.

# Arrays represent basic values(characters, integers, floats) and behave very much like lists, except
# the type of objects stored in them is constrained.
# array.array(typecode, iterable)
# floats.tofile(fp)
# floats2.fromfile(fp, 10**7)



# collections.abc



# hashable object
# An object is hashable if it has a hash value which never changes during its lifetime (it
# needs a __hash__() method), and can be compared to other objects (it needs an
# __eq__() method). Hashable objects which compare equal must have the same hash value.

# def __hash__(self):
#     return hash(self.x) ^ hash(self.y)

# tuple is immutable but not always hashable:
# tt = (1, 2, (30, 40))
# hash(tt)
# tl = (1, 2, [30, 40])
# hash(tl)



# ChainMap
# UserDict(inherit from userdict rather then dict)



# MappingProxyType builds a read-only mappingproxy instance from a dict
# mappingproxy is dynamic: any change in original dictionary is reflected
# from types import MappingProxyType
# d = {1: 'A'}
# d_proxy = MappingProxyType(d)
# d_proxy
# d_proxy[1]
# # changes cannot be made through d_proxy
# d_proxy[2] = 'x'
# d[2] = 'B'
# d_proxy
# d_proxy[2]



# Set and frozenset
# Set elements must be hashable. The set type is not hashable, but frozenset is, so you
# can have frozenset elements inside a set
# frozenset(range(10))

# from dis import dis
# # the disassembler function(wywołania instrukcji)
# dis('{1}')
# # vs
# dis('set([1])')



# dict
# 1: Keys must be hashable objects
# An object is hashable if all of these requirements are met:
#     1. It supports the hash() function via a __hash__() method that always returns the
#     same value over the lifetime of the object.
#     2. It supports equality via an __eq__() method.
#     3. If a == b is True then hash(a) == hash(b) must also be True.

# 2: dicts have significant memory overhead
# 3: Key search is very fast(example of trading space for time)
# 4: Key ordering depends on insertion order
# 5: Adding items to a dict may change the order of existing keys



# we decode bytes to str to get human readable text, and we encode str to bytes for storage or transmission

# print('asdąś€'.encode('utf-8'))
# print('asdąś€'.encode('utf-16'))
# print('asdąś€'.encode('cp1252', errors='replace'))
# print('asdąś€'.encode('latin1', errors='replace'))
# print('asdąś€'.encode('ascii', 'surrogateescape'))

# Normalizing Unicode text
# from unicodedata import normalize, name
# def nfc_equal(str1, str2):
#     return normalize('NFC', str1) == normalize('NFC', str2)

# def fold_equal(str1, str2):
#     return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold())

# Sorting Unicode text
# Python sorts sequences of any type by comparing the items in each sequence one by
# one. For strings, this means comparing the code points. Unfortunately, this produces
# unacceptable results for anyone who uses non-ASCII characters

# Sorting with the Unicode Collation Algorithm
# import pyuca
# coll = pyuca.Collator()
# fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
# sorted_fruits = sorted(fruits, key=coll.sort_key)



# keyword-only arguments do not need to have a default value, but they can be still mandatory
# def f(a, *, b):
#     print(a, b)

# f(3, b=4)


# identity, value and aliasing(label/etykieta)
# The theme is the distinction between objects and their names. A name is not the object;
# a name is a separate thing

# variables are labels, not boxes

# Python variables are like reference variables in Java, so it’s better to think of them as labels attached to objects
# variables hold references to object

# With reference variables it makes much more sense to say that the variable is assigned to an object, and not the
# other way around. After all, the object is created before the assignment. right-hand side of an assignment happens first

# Every object has an identity, a type and a value. An object’s identity never changes once
# it has been created; you may think of it as the object’s address in memory. The is operator
# compares the identity of two objects; the id() function returns an integer representing
# its identity.

# The == operator compares the values of objects (the data they hold), while is compares
# their identities

# The is operator is faster than ==, because it cannot be overloaded, so Python does not
# have to find and invoke special methods to evaluate it, and computing is as simple as
# comparing two integer ids

# copy.copy(obj)
# copy.deepcopy(obj)

# Function parameters as references

# The problem is that each default value is evaluated
# when the function is defined — i.e. usually when the module is loaded — and the
# default values become attributes of the function object

# Unless a method is explicitly intended to mutate an object received
# as argument, you should think twice before aliasing the argument
# object by simply assigning it to an instance variable in your class. If
# in doubt, make a copy

# del does not delete an object, just a reference to it(name/etykiete)

# The presence of references is what keeps an object alive in memory. When the reference
# count of an object reaches zero, the garbage collector disposes of it

# Weak references to an object do not increase its reference count. The object that is the
# target of a reference is called the referent. Therefore, we say that a weak reference does
# not prevent the referent from being garbage collected.
# (import weakref WeakValueDictionary, WeakSet, ref)
# wref = weakref.ref(object)

# ender = weakref.finalize(object, callback_function)
# ender.alive

# class that wants to keep track of all its current instances - This can be done with weak references

# Every Python object has an identity, a type and a value

# The fact that variables hold references has many practical consequences in Python programming.
# 1. Simple assignment does not create copies.
# 2. Augmented assignment with +=, *= creates new objects if the left-hand variable is
# bound to an immutable object, but may modify a mutable object in-place.
# 3. Assigning a new value to an existing variable does not change the object previously
# bound to it. This is called a rebinding: the variable is now bound to a different object.
# If that variable was the last reference to the previous object, that object will be
# garbage collected.
# 4. Function parameters are passed as aliases, which means the function may change
# any mutable object received as an argument. There is no way to prevent this, except
# making local copies or using immutable objects (eg. passing a tuple instead of a
# list).
# 5. Using mutable objects as default values for function parameters is dangerous because
# if the parameters are changed in-place then the default is changed, affecting
# every future call that relies on the default.

# duck typing
# And this can be accomplished without inheritance, in the spirit of
# duck typing: you just implement the methods needed for your objects to behave as
# expected



# repr() - Return a string representing the object as the developer wants to see it.
# str() -Return a string representing the object as the user wants to see it.

# __iter__ makes a object iterable; this is what makes unpacking work, e.g,
# x, y = my_object

# Private attribute
# if you name an instance attribute in the form __mood (two leading
# underscores and zero or at most one trailing underscore), Python stores the name in
# the instance __dict__ prefixed with a leading underscore and the class name, so in the
# Dog class, __mood becomes _Dog__mood

# safety and not security


# __slots__
# special attribute (not a method) that affects the internal storage of an object, with potentially
# huge impact on the use of memory(removing dict) but little effect on its public interface

# To define __slots__ you create a class attribute with that name and assign it an iterable
# of str with identifiers for the instance attributes
# __slots__ = ('__x', '__y')

# Protocols and duck typing
# In the context of Object Oriented Programming, a protocol is an informal interface,
# defined only in documentation and not in code. For example, the sequence protocol in
# Python entails just the __len__ and __getitem__ methods. Any class Spam that implements
# those methods with the standard signature and semantics can be used anywhere
# a sequence is expected. Whether Spam is a subclass of this or that is irrelevant, all that
# matters is that it provides the necessary methods.

# We say it is a sequence because it behaves like one, and that is what matters

# protocols are defined as the informal interfaces that make polymorphism work
# in languages with dynamic typing like Python

# interface
# interface is: the subset of an object’s public methods
# that enable it to play a specific role in the system. That’s what is implied when the
# Python documentation mentions “a file-like object” or “an iterable”, without specifying
# a class

# protocol
# Protocols are interfaces, but because they are informal — defined only by documentation
# and conventions — protocols cannot be enforced like formal interfaces can. A protocol may be
# partially implemented in a particular class, and that’s OK.

# “duck typing”: operating with objects regardless
# of their types, as long as they implement certain protocols.

# Sequence protocol:
# __getitem__, __len__, __contains__, __iter__??

# slice
# s[1:4:2, 7:9]       # (slice(1, 4, 2), slice(7, 9, None))
# print([1, 3, 5, 7, 9][slice(None, None, 2)])

# indices
# S.indices(len) -> (start, stop, stride)
# This method produces “normalized” tuples of non-negative start, stop and stride integers
# adjusted to fit within the bounds of a sequence of the given length
# slice(None, 10, 2).indices(5)                       # (0, 5, 2)
# slice(-3, None, None).indices(5)                    # (2, 5, 1)

# def __getitem__(self, index):
#     cls = type(self)
#     if isinstance(index, slice):
#         return cls(self._components[index])
#     elif isinstance(index, numbers.Integral):
#         return self._components[index]
#     else:
#         msg = '{cls.__name__} indices must be integers'
#         raise TypeError(msg.format(cls=cls))


# dynamic attribute access
# The __getattr__ method is invoked by the interpreter when attribute lookup fails. In
# simple terms, given the expression my_obj.x, Python checks if the my_obj instance has
# an attribute named x; if not, the search goes to the class (my_obj.__class__), and then
# up the inheritance graph2. If the x attribute is not found, then the __getattr__ method
# defined in the class of my_obj is called with self and the name of the attribute as a string,
# e.g. 'x'.

# def __getattr__(self, name):
#     cls = type(self)
#     ...
#     raise AttributeError(msg)

# def __setattr__(self, name, value):
#     ...
#     raise AttributeError('readonly attribute'/"can't set attributes")
#     super().__setattr__(name, value)



# reduce
# As examples, for +, |, ^ the initializer should be 0, but for *, & it should be 1.



# KISS principle - KISS is an acronym for "Keep it simple, stupid"



# random.SystemRandom()?


# Strong versus weak typing
# If the language rarely performs implicit conversion of types, it’s considered strongly
# typed; if it often does it, it’s weakly typed. Java, C++ and Python are strongly typed.
# PHP, JavaScript and Perl are weakly typed.



# Static versus dynamic typing
# If type-checking is performed at compile time, the language is statically typed; it it
# happens at run-time, it’s dynamically typed. Static typing requires type declarations
# (some modern languages use type inference to avoid some of that). Fortran and
# Lisp are the two oldest programming languages still alive and they use, respectively,
# static and dynamic typing.

# To summarize, Python uses dynamic and strong typing



# Subclassing built-in types is tricky
# This built-in behavior is a violation of a basic rule of object oriented programming: the
# search for methods should always start from the class of the target instance (self), even
# when the call happens inside a method implemented in a superclass.

# from collections import OrderedDict
# +class DoppelDict(collections.UserDict):
# -class DoppelDict(dict):
#     def __setitem__(self, key, value):
#         super().__setitem__(key, [value] * 2)

# dd = DoppelDict(one=1) #
# print(dd)
# dd['two'] = 2
# print(dd)
# dd.update(three=3) #
# print(dd)

# Instead of subclassing the built-ins, derive your classes
# from UserDict, UserList and UserString from the collections
# module, which are designed to be easily extended.



# NotImplemented vs NotImplementedError
# Do not confuse NotImplemented with NotImplementedError. The
# first, NotImplemented is a special singleton value that an infix operator
# special method should return to tell the interpreter it cannot
# handle a given operand. In contrast, NotImplementedError is an
# exception that stub methods in abstract classes raise to warn that
# they must be overwritten by subclasses.



# If an infix operator method raises an exception, it aborts the operator
# dispatch algorithm. In the particular case of TypeError, it is often
# better to catch it and return NotImplemented. This allows the interpreter
# to try calling the reversed operator method which may
# correctly handle the computation with the swapped operands, if they
# are of different types.



# Operator overloading
# stick to the fundamental rule of operators: always return a new object !!!
# In other words, do not modify self, but create and return a new instance of a suitable type

# def __abs__(self):
#     return math.sqrt(sum(x * x for x in self))
# # - __neg__
# # Arithmetic unary negation. If x is -2 then -x == 2
# def __neg__(self):
#     return Vector(-x for x in self)
# # + __pos__
# # Arithmetic unary plus. Usually x == +x
# def __pos__(self):
#     return Vector(self)
# def __add__(self, other):
#     pairs = itertools.zip_longest(self, other, fillvalue=0.0) #
#     return Vector(a + b for a, b in pairs) #
# def __radd__(self, other):
#     return self + other

# __radd__ = __add__

# def __mul__(self, scalar):
#     if isinstance(scalar, numbers.Real): #
#         return Vector(n * scalar for n in self)
#     else: #
#         return NotImplemented
# def __rmul__(self, scalar):
#     return self * scalar

# __rmul__ = __mul__

# KlassA * KlassB
# KlassA.__mul__(self, rhs) => KlassB.__rmul__(self, lhs)


# += as a shortcut for the list.extend()
# Very important: augmented assignment special methods must return self


# import itertools
# import numbers

# class Vector:
#     def __init__(self, sequence):
#         self.data = list(sequence)

#     def __iter__(self):
#         return (i for i in self.data)

#     def __add__(self, rhs):
#         pairs = itertools.zip_longest(self, rhs, fillvalue=0.0)
#         return Vector(a + b for a, b in pairs)

#     def __radd__(self, lhs):
#         return self + lhs
#     # __radd__ = __add__

#     def __mul__(self, scalar):
#         print('MUL')
#         if isinstance(scalar, numbers.Real):
#             return Vector(n * scalar for n in self)
#         else:
#             return NotImplemented

#     def __rmul__(self, scalar):
#         print('RMUL')
#         return self * scalar
#     # __rmul__ = __mul__

#     def __eq__(self, other):
#         if isinstance(other, Vector):
#             return (len(self) == len(other) and
#                     all(a == b for a, b in zip(self, other)))
#         else:
#             return NotImplemented

#     def __str__(self):
#         return 'Vector([{}])'.format(self.data)





# Iterables, iterators and generators
# But an iterator — as defined in the GoF book — retrieves
# items from a collection, while a generator can produce items
# “out of thin air”

# reprlib.repr ('string ... string')

# Every Python programmer knows that sequences are iterable

# Whenever the interpreter needs to iterate over an object x, it automatically calls iter(x).
# The iter built-in function:
# 1. Checks whether the object implements, __iter__, and calls that to obtain an iterator;
# 2. If __iter__ is not implemented, but __getitem__ is implemented, Python creates
# an iterator that attempts to fetch items in order, starting from index 0 (zero);
# 3. If that fails, Python raises TypeError, usually saying "'C' object is not itera
# ble", where C is the class of the target object.

# The standard interface for an iterator has two methods
# __next__
# Returns the next available item, raising StopIteration when there are no more
# items.
# __iter__
# Returns self; this allows iterators to be used where an iterable is expected, for
# example, in a for loop.

# for loop equivalent
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         del it
#         break

# checking if object is iterator
# isinstance(object, abc.Iterator)


# iter - Once exhausted, an iterator becomes useless


# iterable
# Any object from which the iter built-in function can obtain an iterator. Objects
# implementing an __iter__ method returning an iterator are iterable. Sequences
# are always iterable; so as are objects implementing a __getitem__ method which
# takes 0-based indexes


# iterator
# Any object that implements the __next__ no-argument method which returns the
# next item in a series or raises StopIteration when there are no more items. Python
# iterators also implement the __iter__ method so they are iterable as well.


# issubclass(SentenceInterator, abc.Iterator)

# Generator objects implement both(next, iter), so from this perspective
# every generator is an iterator

# But you can write an iterator that is not a generator —
# by implementing the classic Iterator pattern, as we saw in Example 14-4,
# or by coding an extension in C.

# classic Iterator pattern
# import re
# import reprlib

# RE_WORD = re.compile('\w+')

# class Sentence:

#     def __init__(self, text):
#         self.text = text
#         self.words = RE_WORD.findall(text)

#     def __repr__(self):
#         return 'Sentence(%s)' % reprlib.repr(self.text)

#     def __iter__(self):
#         return SentenceIterator(self.words)

# class SentenceIterator:

#     def __init__(self, words):
#         self.words = words
#         self.index = 0

#     def __next__(self):
#         try:
#             word = self.words[self.index]
#         except IndexError:
#             raise StopIteration()
#         self.index += 1
#         return word

#     def __iter__(self):
#         return self


# To 'support multiple traversals' it must be possible to obtain multiple independent
# iterators from the same iterable instance, and each iterator must keep its own internal
# state, so a proper implementation of the pattern requires each call to iter(my_itera
# ble) to create a new, independent, iterator. That is why we need the SentenceItera
# tor class in this example.

# s = Sentence('2323d 23f23fd 23d23d')
# # print([i for i in s])
# it = iter(s)
# # print([i for i in s])
# print(it)

# import re
# import reprlib
# RE_WORD = re.compile('\w+')

# class Sentence:

#     def __init__(self, text):
#         self.text = text
#         self.words = RE_WORD.findall(text)

#     def __repr__(self):
#         return 'Sentence(%s)' % reprlib.repr(self.text)

#     def __iter__(self):
#         for word in self.words:
#             yield word
# __iter__ is generator function which, when called, builds a generator object which
# implements the iterator interface, so the SentenceIterator class is no longer needed


# s = Sentence('2323d 23f23fd 23d23d')
# # print([i for i in s])
# it = iter(s)
# # print([i for i in s])
# print(it)



# Any Python function that contains the yield keyword is a generator function

# A generator doesn’t “return” values in the usual way: the return statement in the body
# of a generator function causes StopIteration to be raised by the generator object

# lazy is re.finditer() / eager is re.findall()


# import re
# import reprlib
# RE_WORD = re.compile('\w+')

# class Sentence:

#     def __init__(self, text):
#         self.text = text

#     def __repr__(self):
#         return 'Sentence(%s)' % reprlib.repr(self.text)

#     def __iter__(self):
#         # generator function
#         # for match in RE_WORD.finditer(self.text):
#         #     yield match.group()
#         # or
#         # generator expression
#         return (match.group() for match in RE_WORD.finditer(self.text))
#         # The end result is the same: the caller of __iter__ gets a generator object



# def aritprog_gen(begin, step, end=None):
#     result = type(begin + step)(begin)
#     forever = end is None
#     index = 0
#     while forever or result < end:
#         yield result
#         index += 1
#         result = begin + step * index

# from decimal import Decimal as d
# print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1)
# print(0.1 + 0.1*9)

# def aritprog_gen(begin, step, end=None):
#     first = type(begin + step)(begin)
#     ap_gen = itertools.count(first, step)
#     if end is not None:
#         ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
#     return ap_gen

# import itertools
# list(itertools.accumulate(sample, min)
# list(itertools.accumulate(range(1, 11), operator.mul)
# list(itertools.starmap(operator.mul, enumerate('albatroz', 1)))
# list(itertools.chain(enumerate('ABC')))
# list(itertools.chain.from_iterable(enumerate('ABC')))
# list(itertools.zip_longest('ABC', range(5)))
# list(itertools.zip_longest('ABC', range(5), fillvalue='?'))
# list(itertools.product('AB', range(2), repeat=2))
# list(itertools.product('ABC', '!@#', range(2)))
# list(itertools.islice(itertools.count(1, .3), 3))
# list(map(operator.mul, range(11), itertools.repeat(5)))

# groupby
# for char, group in itertools.groupby('LLLLAAAGG'):
#     print(char, '->', list(group))

# animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
# for length, group in itertools.groupby(reversed(animals), len):
#     print(length, '->', list(group))

# tee - tuple of n independent iterators
# print(list(itertools.tee('ABC', 5)))

# all and any
# g = (n for n in [0, 0.0, 7, 8])
# print(all(g))
# print(next(g))
# print(next(g))
# print(next(g))

# iter(callable, sentinel)
# a marker value which, when returned by the callable, causes the
# iterator to raise StopIteration instead of yielding the sentinel

# with open('some_file.txt', 'rt') as f:
#     for line in iter(lambda: f.readline().split(), 'END'):
#     # for line in iter(f.readline, ''):
#         print(line)


# Coroutines
# Like .__next__(), .send() causes the generator to advance to the next yield, but it
# also allows the client using the generator to send data into it: whatever argument is
# passed to .send() becomes the value of the corresponding yield expression inside the
# generator function body. In other words, .send() allows two-way data exchange between
# the client code and the generator — in contrast with .__next__() which only lets
# the client receive data from the generator.
# This is such a major “enhancement” that it actually changes the nature of generators:
# when used in this way, they become coroutines.

# That’s the big advantage of having coroutines: functions that can be suspended and resumed

# Fibonacci series
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b



# else blocks
# for/else
# The else block will run only if and when the for loop runs to completion; i.e. not
# if the for is aborted with a break
# for item in my_list:
#     if item.flavor == 'banana':
#         break
# else:
#     raise ValueError('No banana flavor found!')

# while/else
# The else block will run only if and when the while loop exits because the condition
# became falsy; i.e. not when the while is aborted with a break

# try/else
# The else block will only run if no exception is raised in the try block. The official
# docs also state: “Exceptions in the else clause are not handled by the preceding
# except clauses.”
# try:
#     dangerous_call()
# except OSError:
#     log('OSError...')
# else:
#     after_call()

# In all cases, the else clause is also skipped if an exception or a return, break or con
# tinue statement causes control to jump out of the main block of the compound statement



# EAFP
# Easier to ask for forgiveness than permission. This common Python coding style
# assumes the existence of valid keys or attributes and catches exceptions if the assumption
# proves false. This clean and fast style is characterized by the presence of
# many try and except statements. The technique contrasts with the LBYL style common
# to many other languages such as C.

# LBYL
# Look before you leap. This coding style explicitly tests for pre-conditions before
# making calls or lookups. This style contrasts with the EAFP approach and is characterized
# by the presence of many if statements. In a multi-threaded environment,
# the LBYL approach can risk introducing a race condition between “the looking” and
# “the leaping”. For example, the code, if key in mapping: return mapping[key] can
# fail if another thread removes key from mapping after the test, but before the lookup.
# This issue can be solved with locks or by using the EAFP approach.



# with blocks
# The with statement was designed to simplify the try/finally pattern which guarantees
# that some operation is performed after a block of code, even if the block is aborted
# because of an exception, a return or sys.exit() call. The code in the finally clause
# usually releases a critical resource or restores some previous state that was temporarily
# changed.

# with blocks don’t define a new scope, as functions and modules do.

# with is not just for
# resource management, but it’s a tool for factoring out common setup and tear down
# code, or any pair of operations that need to be done before and after another procedure



# sys.stdout.write/redirect_stdout
# import contextlib
# @contextlib.contextmanager
# def looking_glass():
#     # __enter__
#     import sys
#     original_write = sys.stdout.write
#     def reverse_write(text):
#         original_write(text[::-1])
#     sys.stdout.write = reverse_write
#     yield 'JABBERWOCKY'
#     # __exit__
#     sys.stdout.write = original_write

# with looking_glass():
#     print('hello')

# print('hello')



# Coroutines
# thinking of yield primarily in terms of control flow

# A coroutine is syntactically like a generator: just a function with the yield keyword in
# its body. However, in a coroutine, yield usually appears on the right side of an expression,
# e.g. datum = yield, and it may or may not produce a value — if there is no expression
# after the yield keyword, the generator yields None. The coroutine may receive
# data from the caller, which uses .send(datum) instead of next(…) to feed the coroutine.
# Usually, the caller pushes values into the coroutine

# This allows a generator to be used as a coroutine: a procedure that collaborates
# with the caller, yielding and receiving values from the caller

# def simple_coro2(a):
#     print('-> Started: a =', a)
#     b = yield a
#     print('-> Received: b =', b)
#     c = yield a + b
#     print('-> Received: c =', c)
#     print(a, b, c)
#     return 'msg'

# my_coro2 = simple_coro2(14)
# print(next(my_coro2))
# print(my_coro2.send(28))
# my_coro2.send(99)



# coroutine decorator
# from functools import wraps
# def coroutine(func):
#     """Decorator: primes `func` by advancing to first `yield`"""
#     @wraps(func)
#     def primer(*args,**kwargs):
#         gen = func(*args,**kwargs)
#         next(gen)
#         return gen
#     return primer



# generator.throw(exc_type[, exc_value[, traceback]])
# Causes the yield expression where the generator was paused to raise the exception
# given. If the exception is handled by the generator, flow advances to the next
# yield, and the value yielded becomes the value of the generator.throw call. If the
# exception is not handled by the generator, it propagates to the context of the caller.

# generator.close()
# Causes the yield expression where the generator was paused to raise a Generator
# Exit exception. No error is reported to the caller if the generator does not handle
# that exception or raises StopIteration — usually by running to completion. When
# receiving a GeneratorExit the generator must not yield a value, otherwise a Run
# timeError is raised. If any other exception is raised by the generator, it propagates
# to the caller.



# One of the main reasons why the yield from construct was added to Python 3.3 has to
# do with throwing exceptions into nested coroutines. The other reason was to enable
# coroutines to return values more conveniently. Read on to see how

# class DemoException(Exception):
#     """An exception type for the demonstration."""

# def demo_finally():
#     print('-> coroutine started')
#     try:
#         while True:
#             try:
#                 x = yield
#             except DemoException:
#                 print('*** DemoException handled. Continuing...')
#             else:
#                 print('-> coroutine received: {!r}'.format(x))
#     finally:
#         print('-> coroutine ending')

# co = demo_finally()
# next(co)
# co.send(22)
# co.send(47)
# co.send(5)
# co.throw(DemoException)
# co.send(7)



# Return value from coroutine
# from collections import namedtuple
# Result = namedtuple('Result', 'count average')

# def averager():
#     total = 0.0
#     count = 0
#     average = None
#     while True:
#         term = yield
#         if term is None:
#             break
#         total += term
#         count += 1
#         average = total/count
#     return Result(count, average)

# coro_avg = averager()
# next(coro_avg)
# coro_avg.send(10)
# coro_avg.send(30)
# coro_avg.send(6.5)
# try:
#     coro_avg.send(None)
# except StopIteration as exc:

#     result = exc.value

# print(result)


# yield from and the StopIteration value from function return 
# In the case of yield from, the interpreter not only consumes
# the StopIteration, but its value attribute becomes the value of the yield
# from expression itself.

# !!!
# The first thing to know about yield from is that it is a completely new language construct.
# It does so much more than yield that the reuse of that keyword is arguably
# misleading
# Similar constructs in other languages are called await and that is a much
# better name because it conveys a crucial point: when a generator gen calls yield from
# subgen(), the subgen takes over and will yield values to the caller of gen; the caller will
# in effect drive subgen directly. Meanwhile gen will be blocked, waiting until subgen
# terminantes

# The first thing the yield from x expression does with the x object is to call iter(x) to
# obtain an iterator from it. This means that x can be any iterable

# !!!
# The main feature of yield from is to open a bidirectional channel from the outermost
# caller to the innermost subgenerator, so that values can be sent and yielded back and
# forth directly from them, and exceptions can be thrown all the way in without adding
# a lot of exception handling boilerplate code in the intermediate coroutines. This is what
# enables coroutine delegation in a way that was not possible before

# Since the delegating generator works as a
# pipe, you can connect any number of them in a pipeline: one delegating generator uses
# yield from to call a subgenerator, which itself is a delegating generator calling another
# subgenerator with yield from and so on. Eventually this chain must end in a simple
# generator that uses just yield, but it may also end in any iterable object

# We saw how the statement return the_result in a generator
# now raises StopIteration(the_result), allowing the caller to retrieve the_result
# from the value attribute of the exception. This is a rather cumbersome way to retrieve
# coroutine results, but it’s handled automatically by the yield from syntax introduced
# in PEP 380

# The coverage of yield from started with trivial examples using simple iterables, then
# moved to an example highlighting the three main components of any significant use of
# yield from: the delegating generator (defined by the use of yield from in its body),
# the subgenerator activated by yield from and the client code that actually drives the
# whole setup by sending values to the subgenerator through the pass-through channel
# established by yield from in the delegating generator

# We closed the chapter with the discrete event simulation example, showing how generators
# can be used as an alternative to threads and callbacks to support concurrency.
# Although simple, the taxi simulation gives a first glimpse at how event-driven frameworks
# like Tornado and asyncio use a main loop to drive coroutines executing concurrent
# activities with a single thread of execution.

# Coroutine
# One final note: this chapter adopted a broad, informal definition of a coroutine: a generator
# function driven by a client sending it data through .send(…) calls or yield from


# Example of flattening a nested sequence using subgenerators
# from collections import Iterable

# def flatten(items, ignore_types=(str, bytes)):
#     for x in items:
#         if isinstance(x, Iterable) and not isinstance(x, ignore_types):
#             yield from flatten(x)
#         else:
#             yield x

# items = [1, 2, [3, 4, [5, 6], 7], 8]

# # Produces 1 2 3 4 5 6 7 8
# for x in flatten(items):
#     print(x)

# items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
# for x in flatten(items):
#     print(x)



# DES - discrete event simulation
# Intuitively, turn-based games are examples of discrete event simulations: the state of the
# game only changes when a player moves, and while a player is deciding the next move,
# the simulation clock is frozen. Real time games, on the other hand, are continuous
# simulations where the simulation clock is running all the time, the state of the game is
# updated many times per second and slow players are at a real disadvantage.


# raise from lambda !


# Blocking I/O and the GIL
# The CPython interpreter is not thread-safe internally, so it has a Global Interpreter Lock
# (GIL) which allows only one thread at a time to execute Python bytecodes. That’s why
# a single Python process usually cannot use multiple CPU cores at the same time3.
# When we write Python code we have no control over the GIL, but a built-in function
# or an extension written in C can release the GIL while running time consuming tasks.
# In fact, a Python library coded in C can manage the GIL, launch its own OS threads and
# take advantage of all available CPU cores. This complicates the code of the library considerably,
# and most library authors don’t do it.

# Every blocking I/O function in the Python standard library releases
# the GIL, allowing other threads to run. The time.sleep()
# function also releases the GIL. Therefore, Python threads are
# perfectly usable in I/O bound applications, despite the GIL.


# Launching processes with concurrent.futures
# The documentation page for the concurrent.futures package is subtitled “Launching
# parallel tasks”. The package does enable truly parallel computations because it supports
# distributing work among multiple Python processes using the ProcessPoolExecutor
# class — thus bypassing the GIL and leveraging all available CPU cores, if you need to
# do CPU-bound processing.

# os.cpu_count()

# concurent
# map vs submit/as_completed
# The Executor.map function is easy to use but it has a feature that may or may not be
# helpful, depending on your needs: it returns the results exactly in the same order as the
# calls are started: if the first call takes 10s to produce a result, and the others take 1s each,
# your code will block for 10s as it tries to retrieve the first result of the generator returned
# by map. After that, you’ll get the remaining results without blocking because they will
# be done. That’s OK when you must have all the results before proceeding, but often it’s
# preferable to get the results as they are ready, regardless of the order they were submitted.
# To do that, you need a combination of the Executor.submit method and the fu
# tures.as_completed function,

# Python threads are well suited for I/O intensive applications, and the concurrent.fu
# tures package makes them trivially simple to use for certain use cases
# Python threads are well suited for I/O bound applications, despite the
# GIL: every standard library I/O function written in C releases the GIL, so while a given
# thread is waiting for I/O, the Python scheduler can switch to another thread.

# import tqdm(pasek postepu)

# highest level                                                                 concurrent.futures.ThreadPoolExecutor/ProcessPoolExecutor
#                                                                                                 /                \
# lower level - build your own solution out of basic components(more flexible)            threading               multiprocessing


# Concurrency with asyncio

# asyncio uses a stricter definition of “coroutine”. A coroutine suitable for
# use with the asyncio API must use yield from and not yield in its
# body. Also, an asyncio coroutine should be driven by a caller invoking
# it through yield from or by passing the coroutine to one of the
# asyncio functions such as asyncio.async(…)

# One final point related to threads versus coroutines: if you’ve done any non-trivial programming
# with threads, you know how challenging it is to reason about the program
# because the scheduler can interrupt a thread at any time. You must remember to hold
# locks to protect the critical sections of your program, to avoid getting interrupted in the
# middle of a multi-step operation — which could leave data in an invalid state.
# With coroutines, everything is protected against interruption by default. You must explicitly
# yield to let the rest of the program run. Instead of holding locks to synchronize
# the operations of multiple threads, you have coroutines that are “synchronized” by definition:
# only one of them is running at any time. And when you want to give up control,
# you use yield or yield from to give control back to the scheduler. That’s why it is
# possible to safely cancel a coroutine: by definition, a coroutine can only be cancelled
# when it’s suspended at a yield point, so you can perform cleanup by handling the
# CancelledError exception.

# Using yield from with a future automatically takes care of waiting for it to finish,
# without blocking the event loop — because in asyncio, yield from is used to give
# control back to the event loop

# You don’t need my_future.add_done_callback(…) because you can simply put
# whatever processing you would do after the future is done in the lines that follow
# yield from my_future in your coroutine. That’s the big advantage of having coroutines:
# functions that can be suspended and resumed

# To make sense of Table 18-1, bear in mind that modern CPUs with GHz clocks run
# billions of cycles per second. Let’s say that a CPU runs exactly 1 billion cycles per second.
# That CPU can make 333,333,333 L1 cache reads in one second, or 4 (four!) network
# reads in the same time.

# To keep a program alive despite the inevitable blocking functions there are two
# solutions: using threads or asynchronous calls — the latter being implemented as callbacks
# or coroutines.

# We then saw how to delegate blocking jobs — such as saving a file — to a thread pool
# using the loop.run_in_executor method.

# This was followed by a discussion of how coroutines solve the main problems of callbacks:
# loss of context when carrying out multi-step asynchronous tasks, and lack of a
# proper context for error handling

# Threading
# import threading
# import itertools
# import time
# import sys

# class Signal:
#     go = True


# def spin(msg, signal):
#     write, flush = sys.stdout.write, sys.stdout.flush
#     for char in itertools.cycle('|/-\\'):
#         status = char + ' ' + msg
#         write(status)
#         flush()
#         # The trick to do text-mode animation: move the cursor back with backspace characters (\x08)
#         write('\x08' * len(status))
#         time.sleep(.1)
#         if not signal.go:
#             break
#     write(' ' * len(status) + '\x08' * len(status))


# def slow_function():
#     # pretend waiting a long time for I/O
#     time.sleep(3)
#     return 42


# def supervisor():
#     signal = Signal()
#     spinner = threading.Thread(target=spin, args=('thinking!', signal))
#     print('spinner object:', spinner)
#     spinner.start()
#     result = slow_function()
#     signal.go = False
#     spinner.join()
#     return result


# def main():
#     result = supervisor()
#     print('Answer:', result)

# if __name__ == '__main__':
#     main()


# import asyncio
# import itertools
# import sys


# @asyncio.coroutine
# def spin(msg):
#     write, flush = sys.stdout.write, sys.stdout.flush
#     for char in itertools.cycle('|/-\\'):
#         status = char + ' ' + msg
#         write(status)
#         flush()
#         write('\x08' * len(status))
#         try:
#             yield from asyncio.sleep(.1)
#         except asyncio.CancelledError:
#             break
#     write(' ' * len(status) + '\x08' * len(status))


# @asyncio.coroutine
# def slow_function():
#     # pretend waiting a long time for I/O
#     yield from asyncio.sleep(3)
#     return 42


# @asyncio.coroutine
# def supervisor():
#     spinner = asyncio.async(spin('thinking!'))
#     print('spinner object:', spinner)
#     result = yield from slow_function()
#     spinner.cancel()
#     return result


# def main():
#     loop = asyncio.get_event_loop()
#     result = loop.run_until_complete(supervisor())
#     loop.close()
#     print('Answer:', result)


# if __name__ == '__main__':
#     main()



# must explicitly schedule execution
# loop.create_task(three_stages(request1))


# Metaprogramming

# + json.load/dump

# from urllib.request import urlopen
# import warnings
# import os
# import json
# URL = 'http://www.oreilly.com/pub/sc/osconfeed'
# JSON = 'data/osconfeed.json'

# def load():
#     if not os.path.exists(JSON):
#         msg = 'downloading {} to {}'.format(URL, JSON)
#         warnings.warn(msg)
#         # multiple with statement  
#         with urlopen(URL) as remote, open(JSON, 'wb') as local:
#             local.write(remote.read())

#     with open(JSON) as fp:
#         return json.load(fp)

# Exploring JSON-like data with dynamic attributes
# from collections import abc, namedtuple

# City = namedtuple('City', 'name population')
# van = City('Vancouver', 800000)
# a = {'a': {'example': {'qwe': '3 332  23d32d3d23', 'van': (33, van, 33)}, 'list': [-1, -7, 'a', 'r', 6]}, 'b': 5, 'c': [3, 7], 'van': van}


# class FrozenJSON:
#     """A read-only façade for navigating a JSON-like object
#     using attribute notation
#     """
#     def __init__(self, mapping):
#         self.__data = dict(mapping)

#     def __getattr__(self, name):
#         if hasattr(self.__data, name):
#             # searching for method object e.g dict.keys()
#             return getattr(self.__data, name)
#         else:
#             return FrozenJSON.build(self.__data[name])

#     @classmethod
#     def build(cls, obj):
#         if isinstance(obj, abc.Mapping):
#             return cls(obj)
#         elif isinstance(obj, abc.MutableSequence):
#             print('list', obj)
#             return [cls.build(item) for item in obj]
#         else:
#             print('obj', obj)
#             return obj

# fj = FrozenJSON(a)
# print(fj.a.list[3])


# alternatively implementing with __new__
# from collections import abc
# class FrozenJSON:
#     """A read-only façade for navigating a JSON-like object
#     using attribute notation
#     """
#     def __new__(cls, arg):
#         if isinstance(arg, abc.Mapping):
#             return super().__new__(cls)
#         elif isinstance(arg, abc.MutableSequence):
#             return [cls(item) for item in arg]
#         else:
#             return arg

#     def __init__(self, mapping):
#         self.__data = {}
#         for key, value in mapping.items():
#             if iskeyword(key):
#                 key += '_'
#             self.__data[key] = value

#     def __getattr__(self, name):
#         if hasattr(self.__data, name):
#             return getattr(self.__data, name)
#         else:
#             return FrozenJSON(self.__data[name])



# import keyword
# print(len(keyword.kwlist))


# This is a common shortcut to build an instance with attributes created from keyword arguments
# updating an instance __dict__ with a mapping is a quick way to create a bunch of attributes in that instance9
# class Record:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#     def __eq__(self, other):
#         if isinstance(other, Record):
#             return self.__dict__ == other.__dict__
#         else:
#             return NotImplemented


# Custom exceptions are usually marker classes, with no body. A docstring
# explaining the usage of the exception is better than a mere pass statement.
# class MissingDatabaseError(RuntimeError):
#     """Raised when a database is required but was not set."""

# vars returns the __dict__ of obj, vars(obj) == obj.__dict__

# property
# properties are class attributes designed to manage instance attributes !!!!!!!!!!!!!!!!!!

# Properties override instance attributes(Instance attribute does not shadow class property)
# Properties are always class attributes, but they actually manage attribute access in the
# instances of the class.


# New class property shadows existing instance attribute
# Class.data = property(lambda self: 'the "data" prop value')

# The main point of this section is that an expression like obj.attr does not search for
# attr starting with obj. The search actually starts at obj.__class__, and only if there is
# no property named attr in the class, Python looks in the obj instance itself


# documentation of the properties

# class Foo:
#     @property
#     def bar(self):
#         "The bar attribute"
#         return self.__dict__['bar']

#     @bar.setter
#     def bar(self, value):
#         return 5

# help(Foo)
# help(Foo.bar)

# Remember: the right side of an assignment is evaluated first, so when quantity() is invoked, the price class attribute doesn’t even exist

# Property factory
# def quantity(storage_name):

#     def qty_getter(instance):
#         # qty_getter references storage_name, so it will be preserved in the closure of
#         # this function; the value is retrieved directly from the instance.__dict__ to
#         # bypass the property and avoid an infinite recursion
#         return instance.__dict__[storage_name]

#     def qty_setter(instance, value):
#         if value > 0:
#             instance.__dict__[storage_name] = value
#         else:
#             raise ValueError('value must be > 0')
#     return property(qty_getter, qty_setter, doc='quantity property factory')


# class LineItem:
#     weight = quantity('weight')
#     price = quantity('price')

#     def __init__(self, description, weight, price):
#         self.description = description
#         self.weight = weight
#         self.price = price

#     def subtotal(self):
#         return self.weight * self.price


# a = quantity('help')
# print(a.fset.__closure__[0].cell_contents)
# nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)



# Essential attributes and functions for attribute handling

# obj.__class__ is the same as type(obj)
# Python looks for special methods such as __getattr__ only in an object’s class, and not in the instances themselves

# __dict__
# A mapping that stores the writable attributes of an object or class. An object that
# has a __dict__ can have arbitrary new attributes set at any time

# __slots__
# An attribute that may be defined in a class to limit the attributes its instances can
# have. __slots__ is a tuple of strings naming the allowed attributes

# + obok getattr, setattr, hasattr
# vars([object])
# Returns the __dict__ of object; vars can’t deal with instances of classes that define
# __slots__ and don’t have a __dict__ (contrast with dir, which handles such instances).
# Without an argument, vars() does the same as locals(): returns a dict
# representing the local scope.

# __getattr__(self, name)
# Called only when an attempt to retrieve the named attribute fails, after the obj,
# Class and its superclasses are searched. The expressions obj.no_such_attr, get
# attr(obj, 'no_such_attr') and hasattr(obj, 'no_such_attr') may trigger
# Class.__getattr__(obj, 'no_such_attr'), but only if an attribute by that name
# cannot be found in obj or in Class and its superclasses.

# __getattribute__(self, name)
# Always called when there is an attempt to retrieve the named attribute, except when
# the attribute sought is a special attribute or method. Dot notation and the get
# tattr and hasattr built-ins trigger this method. __getattr__ is only invoked after
# __gatattribute__, and only when __gatattribute__ raises AttributeError. To
# retrieve attributes of the instance obj without triggering an infinite recursion, implementations
# of __getattribute__ should use super().__getattri
# bute__(obj, name).


# Uniform Access Principle (or a variation of it) is the fact that
# function calls and object instantiation use the same syntax in Python: my_obj =
# foo(), where foo may be a class or any other callable



# Attribute Descriptors are a way of reusing the same access logic in multiple attributes. For example,
# field types in ORMs such as the Django ORM and SQL Alchemy are descriptors,
# managing the flow of data from the fields in a database record to Python object attributes
# and vice-versa



# class Quantity:
#     def __init__(self, storage_name):
#         self.storage_name = storage_name

#     def __set__(self, instance, value):
#         if value > 0:
#             instance.__dict__[self.storage_name] = value
#         else:
#             raise ValueError('value must be > 0')


# class LineItem:
#     weight = Quantity('weight')
#     price = Quantity('price')

#     def __init__(self, description, weight, price):
#         self.description = description
#         self.weight = weight
#         self.price = price

#     def subtotal(self):
#         return self.weight * self.price

# instance.__dict__[self.storage_name] = value
# the tempting but bad alternative would be:
# self.__dict__[self.storage_name] = value

# To understand why this would be wrong, think about the meaning of the first two
# arguments to __set__: self and instance. Here, self is the descriptor instance, which
# is actually a class attribute of the managed class. You may have thousands of LineI
# tem instances in memory at one time, but you’ll only have two instances of the descriptors:
# LineItem.weight and LineItem.price. So anything you store in the descriptor
# instances themselves is actually part of a LineItem class attribute, therefore it is shared
# among all LineItem instances


# Property factory versus descriptor class
# def quantity():
#     try:
#         quantity.counter += 1
#     except AttributeError:
#         quantity.counter = 0

#     storage_name = '_{}:{}'.format('quantity', quantity.counter)

#     def qty_getter(instance):
#         return getattr(instance, storage_name)

#     def qty_setter(instance, value):
#         if value > 0:
#             setattr(instance, storage_name, value)
#         else:
#             raise ValueError('value must be > 0')

#     return property(qty_getter, qty_setter)



# Template Method design pattern:
# A template method defines an algorithm in terms of abstract operations that subclasses
# override to provide concrete behavior

# Class.descriptor_name triggers the descriptor __get__ method, passing None as the second argument (instance)

# Overriding Descriptor/data descriptors
# A descriptor that implements the __set__ method it called an overriding descriptor,
# because although it is a class attribute, a descriptor implementing __set__ will override
# attempts to assign to instance attributes. This is how Example 20-2 was implemented.
# Properties are also overriding descriptors: if you don’t provide a setter function, the
# default __set__ from the property class will raise AttributeError to signal that the
# attribute is read-only

# Overriding descriptor without __get__/data descriptors without __get__
# Usually, overriding descriptors implement both __set__ and __get__, but it’s also possible
# to implement only __set__, as we saw in Example 20-1. In this case, only writing
# is handled by the descriptor. Reading the descriptor through an instance will return the
# descriptor object itself because there is no __get__ to handle that access. If a namesake
# instance attribute is created with a new value via direct access to the instance
# __dict__, the __set__ method will still override further attempts to set that attribute,
# but reading that attribute will simply return the new value from the instance, instead of
# returning the descriptor object. In other words, the instance attribute will shadow the
# descriptor, but only when reading

# Non-overriding descriptor/non-data descriptors
# If a descriptor does not implement __set__, then it’s a non-overriding descriptor. Setting
# an instance attribute with the same name will shadow the descriptor, rendering it
# ineffective for handling that attribute in that specific instance. Methods are implemented
# as non-overriding descriptors

# The bound method object also has a __call__ method, which handles the actual invocation.
# This method calls the original function referenced in __func__, passing the
# __self__ attribute of the method as the first argument. That’s how the implicit binding
# of the conventional self argument works



# Descriptor usage tips
# 1. Use property to keep it simple
# The property built-in actually creates overriding descriptors implementing both
# __set__ and __get__, even if you do not define a setter method. The default __set__
# of a property raises AttributeError: can't set attribute, so a property is the easiest
# way to create a read-only attribute, avoiding the issue described next.
# 2. Read-only descriptors require __set__
# If you use a descriptor class to implement a read-only attribute you must remember to
# code both __get__ and __set__, otherwise setting a namesake attribute on an instance
# will shadow the descriptor. The __set__ method of a read-only attribute should just
# raise AttributeError with a suitable message 5.
# 3. Validation descriptors can work with __set__ only
# In a descriptor designed only for validation, the __set__ method should check the value
# argument it gets, and if valid, set it directly in the instance __dict__ using the descriptor
# instance name as key. That way, reading the attribute with the same name from the
# instance will be as fast as possible, as it will not require a __get__. See the code for
# Example 20-1.
# 4. Caching can be done efficiently with __get__ only
# If you code just the __get__ method you have a non-overriding descriptor. These are
# useful to make some expensive computation and then cache the result by setting an
# attribute by the same name on the instance. The namesake instance attribute will shadow
# the descriptor, so subsequent access to that attribute will fetch it directly from the instance
# __dict__ and not trigger the descriptor __get__ anymore.
# 5. Non-special methods can be shadowed by instance attributes
# Because functions and methods only implement __get__, they do not handle attempts
# at setting instance attributes with the same name, so a simple assignment like
# my_obj.the_method = 7 means that further access to the_method through that instance
# will retrieve the number 7 — without affecting the class or other instances. However,
# this issue does not interfere with special methods. The interpreter only looks for special
# methods in the class itself, in other words, repr(x) is executed as
# x.__class__.__repr__(x), so a __repr__ attribute defined in x has no effect of
# repr(x). For the same reason, the existence of an attribute named __getattr__ in an
# instance will not subvert the usual attribute access algorithm.



# Metaprogramming
# Invoking type with three arguments is a common way of creating a class dynamically
# type(my_object) to get the class of the object — same as my_object.__class__

# Class decorators are a simpler way of doing something that
# previously required a metaclass: customizing a class the moment it’s created

# At import time, the interpreter parses the source code of a .py module in one pass from
# top to bottom, and generates the bytecode to be executed. That’s when syntax errors
# may occur. If there is an up-to-date .pyc file available in the local __pycache__, those
# steps are skipped because the bytecode is ready to run

# That’s why the border between “import time” and “run time” is
# fuzzy: the import statement can trigger all sorts of “run time” behavior

# In the usual case, this means that the interpreter defines top level
# functions at import time, but executes their bodies only when — and if — the functions
# are invoked at run time

# For classes, the story is different: at import time, the interpreter executes the body of
# every class, even the body of classes nested in other classes. Execution of a class body
# means that the attributes and methods of the class are defined, and then the class object
# itself is built. In this sense, the body of classes is “top level code”: it runs at import time

# A metaclass is a class factory, except that instead of a function, like record_factory from Example 21-2, a metaclass is written as a class

# The classes object and type have a unique relationship: object is an
# instance of type, and type is a subclass of object. This relationship
# is “magic”: it cannot be expressed in Python because either class would
# have to exist before the other could be defined. The fact that type is
# an instance of itself is also magical

# Every class is an instance of type, directly or indirectly, but only metaclasses are also subclasses of type

# The important takeaway here is that all classes are instances of type, but metaclasses
# are also subclasses of type, so they act as class factories. In particular, a metaclass can
# customize its instances by implementing __init__. A metaclass __init__ method can
# do everything a class decorator can do, but its effects are more profound, as the next exercise demonstrates.

# class MetaAleph(type):

#     @classmethod
#     def __prepare__(cls, name, bases):
#         return collections.OrderedDict()

#     def __init__(cls, name, bases, dic):
#         def inner_2(self):
#             pass

#     cls.method_z = inner_2


# class ClassFive(metaclass=MetaAleph):

#     def __init__(self):
#         pass

#     def method_z(self):
#         pass

# When coding a metaclass, it’s conventional to replace self by cls.
# For example, in the __init__ method of the metaclass, using cls as
# the name of the first argument makes it clear that the instance under
# construction is a class

# The body of __init__ defines an inner_2 function, then binds it to cls.method_z. The
# name cls in the signature of MetaAleph.__init__ refers to the class being created, e.g.
# ClassFive. On the other hand, the name self in the signature of inner_2 will eventually
# refer to an instance of the class we are creating, e.g. an instance of ClassFive.

# The __prepare__ method is invoked by
# the interpreter before the __new__ method in the metaclass to create the mapping that
# will be filled with the attributes from the class body
# @classmethod
#   def __prepare__(cls, name, bases):
#       pass

# metaclasses are used in frameworks and libraries that help programmers perform, among other tasks:
# • attribute validation;
# • applying decorators to many methods at once;
# • object serialization or data conversion;
# • object-relational mapping;
# • object-based persistency;
# • dynamic translation of class structures from other languages


# Class metaprogramming is about creating or customizing classes dynamically. Classes
# in Python are first-class objects, so we started the chapter by showing how a class can
# be created by a function invoking the type built-in metaclass

# !!! check import order in metaprograming chapter
# but clearly a lot of code runs triggered by the import statement

# I haven’t yet found a language that manages to be easy for beginners, practical for professionals
# and exciting for hackers in the way that Python is

# “Only those who work make mistakes" - great advice to avoid being paralyzed by the fear of making errors

# 717 python jargon





# Additional topics
# Everything is executed at the module level when Python first imports a module. Function bodies
# (and generator expression bodies) are the exception here, not the rule. Python executes everything
# to create the objects contained in a module; like everything in Python, classes are objects, and so are functions.
# The only reason a class body uses a separate code object is because a class body is executed in a separate namespace,
# with that namespace then forming the class attributes. Class bodies are not the only such namespaces;
# set and dict comprehensions, and in Python 3, list comprehensions are also executed with a separate namespace,
# scoping their locals. So functions and generator expressions are the exception, expressly because their whole
# purpose is to be executed at a later time. Note that the function definition is executed:

# import shelve

# A key difference between __getattr__ and __getattribute__ is that __getattr__ is only invoked if the attribute
# wasn't found the usual ways. It's good for implementing a fallback for missing attributes,
# and is probably the one of two you want. __getattribute__ is invoked before looking at the actual attributes on the object,
# and so can be tricky to implement correctly. You can end up in infinite recursions very easily










# JavaScript The Good Parts
# JavaScript is an important language because it is the language of the web browser. Its
# association with the browser makes it one of the most popular programming languages in the world

# The API of the browser, the Document Object Model (DOM) is quite awful, and JavaScript is unfairly blamed

# literal - notations for atomic values
# In computer science, a literal is a notation for representing a fixed value in source code.
# Almost all programming languages have notations for atomic values such as integers,
# floating-point numbers, and strings, and usually for booleans and characters;
# some also have notations for elements of enumerated types and compound values such as
# arrays, records, and objects. An anonymous function is a literal for the function type


# When used inside of a function, the var statement defines the function’s private variables

# The switch, while, for, and do statements are allowed to have an optional label prefix
# that interacts with the break statement

# A function always returns a value. If the return value is not specified, then undefined is returned

# If the function was invoked with the new prefix and the return value is not an object, then this (the new object) is returned instead

# throw/try/catch

# Scope in a programming language controls the visibility and lifetimes of variables and parameters

# This is possible because the function has access to the context in which it was created. This is called closure.

# global object - window.foo

# undefine, NaN, null

# Declarations
# There are three kinds of declarations in JavaScript.
# var - Declares a variable, optionally initializing it to a value.
# let - Declares a block scope local variable, optionally initializing it to a value.
# const - Declares a read-only named constant. 

# hoisting
# Another unusual thing about variables in JavaScript is that you can refer to a variable
# declared later, without getting an exception. This concept is known as hoisting;
# variables in JavaScript are in a sense "hoisted" or lifted to the top of the
# function or statement. However, variables that are hoisted will return a value of undefine

# Global variables
# Global variables are in fact properties of the global object.
# In web pages the global object is window, so you can set and access global variables
# using the window.variable syntax



# !
# let allows you to declare variables that are limited in scope to the block, statement,
# or expression on which it is used. This is unlike the var keyword,
# which defines a variable globally, or locally to an entire function regardless of block scope.

# When used inside a block, let limits the variable's scope to that block.
# Note the difference between var whose scope is inside the function where it is declared.
# var a = 1;
# var b = 2;

# if (a === 1) {
#   var a = 11; // the scope is global
#   let b = 22; // the scope is inside the if-block

#   console.log(a);  // 11
#   console.log(b);  // 22
# } 

# console.log(a); // 11
# console.log(b); // 2



# A var has function scope (it declares a variable that's visible throughout the function) even though it looks like it has block scope.

# At the top level of programs and functions, let, unlike var, does not create a property on the global object. For example:
# var x = 'global';
# let y = 'global';
# console.log(this.x); // "global"
# console.log(this.y); // undefined



# Adopt let and const(and ===). Stop using var !
# let x = 'x';

# Constants
# You can create a read-only, named constant with the const keyword
# const PI = 3.14;
# A constant cannot change value through assignment or be re-declared
# while the script is running. It has to be initialized to a value.

# JavaScript is a dynamically typed language.
# That means you dont have to specify the data type of a variable when you declare it,
# and data types are converted automatically as needed during script execution

# .toString()
# parseInt()   function parses a string argument and returns an integer of the specified radix
# parseFloat() function parses a string argument and returns a floating point number.
# typeof
# addEventListener

# Literals
# You use literals to represent values in JavaScript.
# These are fixed values, not variables, that you literally provide in your script.
# Array literals 				var coffees = ["French Roast", "Colombian", "Kona"];
# Boolean literals 				true and false
# Floating-point literals 		-3.1E+12
# Integers 						-345
# Object literals 				var car = { myCar: "Saturn", getCar: carTypes("Honda"), special: sales };
# RegExp literals 				var re = /ab+c/;
# String literals 				"John's \n cat"
# !!!!IMP
# Template literals
# 	var name = "Bob", time = "today";
# 	`Hello ${name}, how are you ${time}?`

# var str = "this string \
# is broken \
# across multiple\
# lines."

# FUBAR (fucked up beyond all recognition)

# Exception
# var log = console.log;
# try {
#   throw "myException"; // generates an exception
# }
# catch (e) {
#   // statements to handle any exceptions
#   log(e); // pass exception object to error handler
# }
# finally {
#   log("finally over");
# }



# Promise
# function imgLoad(url) {
#   return new Promise(function(resolve, reject) {
#     var request = new XMLHttpRequest();
#     request.open('GET', url);
#     request.responseType = 'blob';
#     request.onload = function() {
#       if (request.status === 200) {
#         resolve(request.response);
#       } else {
#         reject(Error('Image didn\'t load successfully; error code:' 
#                      + request.statusText));
#       }
#     };
#     request.onerror = function() {
#       reject(Error('There was a network error.'));
#     };
#     request.send();
#   });
# }



# For example, getting all the nodes of a tree structure (e.g. the DOM)
# is more easily done using recursion:

# function walkTree(node) {
# 	if (node == null) {
#     return;
#   }
#   log('AAAA');
#   if(node.nodeName === 'P') {
#     log('BBB');
#     node.style.color = "purple";
#   }
  
#   for (var i = 0; i < node.childNodes.length; i++) {
#     walkTree(node.childNodes[i]);
#   }

# }

# walkTree(document.body);



# closures(function factories, and secure variable of the outer function)
# ! Be careful - the magical this variable is very tricky in closures.
# They have to be used carefully, as what this refers to depends completely
# on where the function was called, rather than where it was defined.

# function outside(x) {
# 	function inside(y) {
# 		return Math.pow(x, y);
# 	}
# 	return inside;
# }

# fn_inside = outside(3)
# fn_inside(3);



# function createPet(name) {
#   var sex;
  
#   return {
#     setName: function(newName) {
#       name = newName;
#     },
    
#     getName: function() {
#       return name;
#     },
    
#     getSex: function() {
#       return sex;
#     },
    
#     setSex: function(newSex) {
#       if(typeof newSex === "string" && (newSex.toLowerCase() === "male" || newSex.toLowerCase() === "female")) {
#         sex = newSex;
#       }
#     }
#   }
# }

# var pet = createPet("Vivie");
# log(pet.getName());                  // Vivie

# log(pet.setName("Oliver"));
# log(pet.setSex("male"));
# log(pet.getSex());                   // male
# log(pet.getName());                  // Oliver



# Using the arguments
# function myConcat(separator) {
#    let result = "";
#    for (let i = 1; i < arguments.length; i++) {
#       result += arguments[i] + separator;
#    }
#    return result;
# }

# myConcat(", ", "red", "orange", "blue");



# Default parameters
# function multiply(a, b=1) {
#   return a*b;
# }

# multiply(5);



# Rest parameters
# function multiply(multiplier, ...theArgs) {
#   return theArgs.map(x => multiplier * x);
# }

# var arr = multiply(2, 1, 2, 3);
# console.log(arr); // [2, 4, 6]



# Arrow functions
# var a = ["Hydrogen", "Helium", "Lithium", "Beryllium"];
# var a2 = a.map(function(s){ return s.length }); // old
# var a3 = a.map(s => s.length); // new


# Lexical this
# function Person(){
#   this.age = 0;

#   setInterval(() => {
#     // |this| properly refers to the person object, dont need to use 'var self = this;'
#     this.age++;
#   }, 1000);
# }

# var p = new Person();



# Comparison
# Strict equal (===) 	Returns true if the operands are equal and of the same type
# Strict not equal (!==) 	Returns true if the operands are of the same type but not equal, or are of different type.

# Bitwise operators
# AND 15 & 9 	9 	1111 & 1001 = 1001
# OR  15 | 9 	15 	1111 | 1001 = 1111

# Unary operators
# delete objectName.property;

# typeof myFun;         // returns "function"
# typeof "round";       // returns "string"
# typeof 4;        	    // returns "number"
# typeof new Date();    // returns "object"
# typeof doesntExist;   // returns "undefined"
# typeof true; 		    // returns "boolean"
# typeof null; 		    // returns "object"



# Relational operators
# in - propNameOrNumber in objectName
# var trees = ["redwood", "bay", "cedar", "oak", "maple"];
# 0 in trees;        // returns true
# 6 in trees;        // returns false
# "bay" in trees;    // returns false (you must specify the index number,
#                    // not the value at that index)
# "length" in trees; // returns true (length is an Array property)
# "PI" in Math;          // returns true

# var mycar = { make: "Honda", model: "Accord", year: 1998 };
# "make" in mycar;  // returns true

# The instanceof operator returns true if the specified object is of the specified object type
# instanceof - objectName instanceof objectType
# var theDay = new Date(1995, 12, 17);
# if (theDay instanceof Date) {
#   // statements to execute
# }



# Expresions
# this
# <p>Enter a number between 18 and 99:</p>
# <input type="text" name="age" size=3 onChange="document.writeln(this.value);">


# Comprehensions

# Array comprehensions.
# [for (x of y) x]
# var abc = [ "A", "B", "C" ];
# [for (letters of abc) letters.toLowerCase()]; // [ "a", "b", "c" ]

# Generator comprehensions.
# (for (x of y) y)



# new
# You can use the new operator to create an instance of a user-defined
# object type or of one of the built-in object types. Use new as follows:

# var objectName = new objectType([param1, param2, ..., paramN]);



# Spread operator
# The spread operator allows an expression to be expanded in places where multiple arguments
# (for function calls) or multiple elements (for array literals) are expected

# var parts = ['shoulder', 'knees'];
# var lyrics = ['head', ...parts, 'and', 'toes'];

# function f(x, y, z) {return x + y + z }
# var args = [0, 1, 2];
# f(...args);



# Numbers(+Infinity, -Infinity, and NaN)
# Hexadecimal numbers(0123456789abcdef)
# Internationalization - Intl object is the namespace for the ECMAScript Internationalization API



# RegExp
# x(?=y) 	Matches 'x' only if 'x' is followed by 'y'. This is called a lookahead.
# For example, /Jack(?=Sprat)/ matches 'Jack' only if it is followed by 'Sprat'. /Jack(?=Sprat|Frost)/ matches 'Jack' only if it is followed by 'Sprat' or 'Frost'. However, neither 'Sprat' nor 'Frost' is part of the match results.


# x(?!y) Matches 'x' only if 'x' is not followed by 'y'. This is called a negated lookahead.
# For example, /\d+(?!\.)/ matches a number only if it is not followed by a decimal point. The regular expression /\d+(?!\.)/.exec("3.141") matches '141' but not '3.141'.

# (?:x) Matches 'x' but does not remember the match. The parentheses are called non-capturing parentheses,