# -*- coding: utf-8 -*-
# iter(), next()
# class attribute vs instnace attribute
# __prepare__
# __getattribute__(self, name)
# __new__(cls, clsname, bases, clsdict)
# memoryview

# import inspect
# inspect.getsource(object_name)



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
# # the disassembler function
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




from pprint import pprint as print
a = {'1': 1, '2': 2, '3': '3'}
a = {1, 3, 5}

# print('asdąś€'.encode('utf-8'))
# print('asdąś€'.encode('utf-16'))
# print('asdąś€'.encode('cp1252', errors='replace'))
# print('asdąś€'.encode('latin1', errors='replace'))
# print('asdąś€'.encode('ascii', 'surrogateescape'))
