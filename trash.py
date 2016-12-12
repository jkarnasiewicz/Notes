# -*- coding: utf-8 -*-
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

# classic Iterator pattern
import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)

class SentenceIterator:

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


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


import re
import reprlib
RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # generator function
        # for match in RE_WORD.finditer(self.text):
        #     yield match.group()
        # or
        # generator expression
        return (match.group() for match in RE_WORD.finditer(self.text))
        # The end result is the same: the caller of __iter__ gets a generator object



def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index

# from decimal import Decimal as d
# print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1)
# print(0.1 + 0.1*9)

def aritprog_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen

451
