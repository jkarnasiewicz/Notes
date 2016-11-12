# GENERAL INFORMATION/HELP

dir(object)        				# every method for object or dir() for list of names defined in the current module
help(object)

object.__doc__     				# docstring for a function or module object
object.__name__					# name of a function or module object, or just __name__ for current module name
object.__file__					# object file path, or just __file__ for current file path(absolute path)

type(object)       				# type of the object
id(object)				 		# id of the object

# mro - informations about linear order of the inheritance(super())
ClassName.__mro__ == Class_Name.mro()

# Immutable basic types such as numbers, strings, tuples

# Mutable objects such as lists, dictionaries, sets and other types -
# meaning you can change their content without changing their identity

# Sequence (such as a string, bytes, tuple, list, or range)
# Collection (such as a dictionary, set, or frozen set)

# python objects/variables - think of named references to objects rather than variables

# shallow copy - copy only the reference to the key, value paires not the objects themselves e.g.
# a = [[0, 1]]*4
# a[2].append(7)

# Dynamic type system
# In dynamic type system objects types are only resolved at runtime (w czasie wykonywania programu)

# Strong type system
# In a strong type system there is no implicit type conversion
# e.g. 'string' + 43 => TypeError

# Default argument expressions evaluated once, when def is executed
# Always use immutable objects as a default argument value

# Value equality(equivalent 'contents') vs. identity(same object id())
# Value comparison can be controlled programatically('__eq__')
# [] == [] => True
# [] is [] => False


# Python name scopes(names are looked up in four nested scopes)
# Local - inside the current function
# Enclosing - any and all enclosing functions
# Global - top-level of module
# Built-in - provide by the builtins module

# Module < Package

# Runing python with -O option, allow to run python without active assertions





# IMPORT MODULES
import module
from module import object_name as alias_name

# This will import all public names but would not import __name__ because it starts with double underscores
from module import *

# Selective import - if use "from module import *" and that module has define __all__ we get only names from that list(e.g. in __init__.py)
__all__ = ['names', 'available', 'in_module']

# Relative imports
from .b import B
# Parent directory
from ..a import A





# BUILT-IN FUNCTIONS
# return a dictionary representing the current global symbol table
globals()

# return a dictionary mapping local variable names to their value
locals()

# use global to assign to global references from a local scope
global variable_name

# introduce names from the enclosing namespace into the local namespace
nonlocal variable_name

# return True or False (callable or not)
callable(obj)

# isinstance
isinstance(3, (int, str))
# issublclass
issubclass(list, object)

# return True if every element of the iterable is truthy, all([]) returns True
all(iterable)

# return True if any element of the iterable is truthy any([]) returns False
any(iterable)

# has, get and setattr
hasattr(object, 'atribute_name')					# return True or False
getattr(object, 'atribute_name', default)			# default argument if 'atribute_name' doesn't exist
setattr(object, 'atribute_name', value)

# apply a function to every element in a sequence, producing a new sequence finish when get the last element in the sequence
map(function, sequence, sequence)

# apply a function to each element in a sequence, constructing a new sequence with the elements for witch the function returns True
filter(function, sequence)

# function that aggregates elements from each of the iterables
zip(sequence, sequence, sequence)

# sorts any iterable series and returns a list
sorted(iterable, key=None, reverse=False) 

# reverses any iterable series, returns a reverse iterator
reversed(sequence)





# CONVERT VALUES
# return a boolean value (True or False)
bool(object)

# unlimited precision signed integer
int(x)
# bases from 2 to 36 (oct(x) - base 8, hex(x) - base 16)
int(string, base)

# convert an integer number to a binary string (base 2)
bin(x)

# floating point number constructed from a number or string x
# 1bit(sign) - 11bits(exponent) - 52bits(fraction) 15 to 17 bits of decimal precision
float(x)

# convert x to string, calling __str__ method
str(x)
# string representation of an object, calling __repr__ method
repr(x)

# replace non-ASCII characters with escape sequences
ascii()

# return the string representing a character whose Unicode codepoint is the integer
chr(97)												# returns the string 'a'     

# return an integer representing the Unicode code point of that character
ord('a')											# returns the integer 97     





# NUMBERS
# power
2 ** 4 == pow(2,4)									# 16

# classic division returns a float(divide)
17 / 3        										# 5.666666666666667 	

# floor division discards the fractional part
17 // 3       										# 5

# the % operator returns the remainder of the division(modulo)
17 % 3        										# 2

# float remainder
(-7) % 3					 						# 2

# decimal remainder
Decimal(-7) % Decimal(3)	 						# -1

# divmod = (floor division, remainder)
divmod(5, 3)										# (1, 2)

# absolute value of a number
abs(-4)												# 4

# return the smallest item in an iterable or the smallest of two or more arguments
min(iterable, key, default)

# return the largest item in an iterable or the largest of two or more arguments
max(iterable, key, default)

# rounding function, be carefull with float numbers which can't be represented exacly in binary
round(17/9)
# how many digits we want to round to
round(Decimal('3.456'), 2)
# Fraction(3, 5)
round(Fraction(57, 100), 1)

# increment and decrement operators
+=, -=, *=, /=, //=

# comparing values
<, >, <=, >=, ==, !=

# x < 10 and 10 < x * 10 and x*10 < 100
x < 10 < x*10 < 100

# comparing sequences and other types
[1, 2, 3] < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4) < (1, 2, 4)
(1, 2) < (1, 2, 1)
(1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)

# testing ids of the objects/compare ids
is, is not

# membership testing using
in, not in

# i, lub
and, or

# Exclusive or(alternatywa wykluczająca)
bool(a) != bool(b)



# Decimal
# import decimal
decimal.getcontext().prec = 6
# always use quotes
decimal.Decimal('0.8')

# from decimal import Decimal as d
# d('Infinity'), d('-Infinity'), d('NaN')
d('1.234567') + d(1)								# d('2.23457')



# Fractions (ulamki)
# from fractions import Fraction as f
f(1, 2) + f(3, 4)									# Fraction(5, 4)
f('0.1') == f(Decimal('0.1'))						# Fraction(1. 10)
f(0.1)												# 3602879701896397/36028797018963968



# Complex Numbers
complex(2, 3)										# (2 + 3j)
complex('2+3j')										# (2 + 3j)
c = 2 + 3j											# (2 + 3j)
c.real 												# 2.0
c.imag 												# 3.0
# sprzężenie zespolone
c.conjugate()										# (1 - 3j)

# import cmath - Mathematical functions for complex numbers
cmath.sqrt(-1)										# 1j
cmath.polar(1+1j)									# (1.4142135623730951, 0.7853981633974483) = modulus, phase
cmath.rect(modulus, phase)



# Statistics
# import statistics as s
a = [2, 4, 5, 1, 3, 6, 3, 7]
print(s.median(a), s.mean(a), s.variance(a))



# Bitwise operators
# 2 is represented by 10 in bits(left shift) Left shifting by 2 bits gives 1000 which represents the decimal 8
2 << 2        										# 8

# (right shift) Shifts the bits of the number to the right by the number
# of bits specified. 11 is represented in bits by 1011 which when right
# shifted by 1 bit gives 101 which is the decimal 5.
11 >> 1												# 5





# STRINGS
# raw string (no 'escape sequences')
r'This is a\tstring!'

# breaking string with \
s = 'This is a string. \
	This continues the string.'

# length of the string
len('Python')

# slice [start:stop:step]
'string'[0:6:3]										# 'si'
# last character
'string'[-1]				                 		# 'g'
# characters from position 2 (included) to 5 (excluded)
'string'[2:5]                						# 'rin'
# characters from the second-last (included) to the end
'string'[-2:]                						# 'ng'
'python'[:2] + 'python'[2:]  						# 'python'

# split()
'key value pair'.split()							# ['key', 'value', 'pair']
'key/value/pair'.split('/', 2)          			# ['key', 'value', 'pair']

# splitlines()
'st\nri\nng'.splitlines()							# ['st', 'ri', 'ng']

# join()
# always prefer 'join' over regular concatenation, strings are immutable,
# so the += operator re-binds the reference to a new object(adding memory usage)
'-'.join(str(i) for i in [1, 3, 6])   				# '1-3-6'
' '.join("string")                					# 's t r i n g'

# partition()
'unforgetable'.partition('forget')					# ('un', 'forget', 'able')


# replace(old, new, count)
'string'.replace('r', '-', 5)     					# 'st-ing'
'string'.find('r')                					# 2

# checks if the string has only alphanumeric characters in it (A-Z, a-z and 0-9)
''.isalnum()

# only alpha characters (A-Z, a-z)
'Ng'.isalpha()

# checks if there are only digits (0-9)
'37'.isdigit()

.capitalize()
.lower()
.upper()
.swapcase()
# find extension
.lower().endswith('.mp3')
# all chars have been stripped from begining and the end of the string
.strip('chars')
# removing whitespaces from the end of string
.rstrip()
.center(80)

# from string to byte object (python 3)
string_object.encode(encoding='utf-8', errors='strict')

# from byte to string object (python 3)
byte_object.decode('utf-8')



# Formating And "Print"
# output of print can be redirected using the optional file argument
print(*objects, sep = " \t", end = "\n", file=sys.stdout)

print( "{0}'s password is {1}".format(username, password) )
print( "real part:{0.r}, imaginary part:{0.i} i liczba {1:.1f}".format(Complex(3, 6), 123.345) )

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack}; Sjoerd: {Sjoerd:.2f}; Dcab: {Dcab}'.format(**table))

# to righr, 40 characters, one character after dot, float
print( "{0:>40.1f}".format(123.345) )
print('{0}, lub {0:.3}'.format(1/3))
print('{0:_^11}'.format('hello'))

# requesting __repr__()
print('{0!r}'.format(object))

# requesting __str__()
print('{0!s}'.format(object))

# line feed
'\n'
# carriage return
'\r'
# tabulator
'\t'





# TUPLE
t = 1, 2, 3, 4, 3
# creating tuple with one element
t = 1,

# return number of occurrences of value
t.count(value)

# return first index of value
t.index(value)





# LISTS
li = [1, 8, 27, [0, 1], 125]
# replace value
li[3][1] = 3

# count value
li.count(value)

# return first index of value
li.index(value)

# insert object
li.insert(index, object)

# append object to end
li.append(object)

# The extend() method takes a single argument, which is always a list, and adds each of the items of that list to a list
li.extend(iterable)

# remove the first occurrence of object
li.remove(object)

# delete the object at index 3
del li[3]

# remove and return item at index (default last)
li.pop(index)

# reverse in place
li.reverse()

# sorts in place
li.sort(key=callable, reverse=True)





# SETS (unordered collection of unique, immutable objects)(Zbiory)
# duplicates are removed, only unique items stay
basket = set(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])			# {'orange', 'banana', 'pear', 'apple'}

# The add() method takes a single argument, which can be any immutable datatype, and adds the given object to the set
basket.add(object)

# You can actually call the update() method with any number of arguments, update a set with the union of itself and others
basket.update(iterable)

# remove object, if the value doesn’t exist in the set, the remove() method raises a KeyError exception,
basket.remove(object)

# remove object, discard don't raises any exception
basket.discard(object)

# shallow copy of the set
basket.copy()

# a | b, letters in either a or b (Suma)
a.union(b)

# a - b, letters in a but not in b (Roznica)
a.difference(b)

# a & b, letters in both a and b (Iloczyn)
a.intersection()

# a ^ b, letters in a or b but not both (Roznica symetryczna)
a.symetric_difference(b)

# Subset and Superset(podzbiór, nadzbiór i rozłączność)
a.issubset(b)
a.issuperset(b)
a.isdisjoint(b)

# If True, list have more than one diffrent object
if(len(set(iterable)) != 1)




 
# DICTIONARIES (unordered mapping from unique, immutable keys to mutable values -> Key: Value)
di = {'sape': 4139, 'ivy': 4127, 'jack': 4098}
di = dict([('sape', 4139), ('ivy', 4127), ('jack', 4098)])

# get object - like switch
di.get(key, default=None)
# factory_class(arg1, arg2)
factory_class = {'a': ClassOne, 'b': ClassTwo}.get('b', ClassThree)

# the method will set dict[key]=default if key is not already in dict
di.setdefault(key, default=None)

# update existing entry
di['jack'] = 9744

# add new entry
a['lee'] = 4567

# update, adds dictionary key-values pairs to 'di'
di.update(dictionary)

# remove entry with key 'sape'
del di['sape']

# remove and return value of 'sape'
di.pop('sape')

# remove all entries in dict
di.clear()

# shallow copy of the dictionary
di.copy()

# delete entire dictionary
del a

di.items()
di.keys()
di.values()
di.fromkeys(range(10), 10)





# READING AND WRITING FILES
# file object support iterator protocol(and yield line by line)

open(file="path to file", mode="read/write/append, binary/text", encoding="text encoding")

# creating the new file or overwriting the existing file
with open("Example.txt", mode="wt", encoding="utf-8") as f:
	f.write("Hello\n...")

# append to the file instead of overwriting
with open("Example.txt", mode = "at", encoding = "utf-8") as f:
	f.write("\nYupii\r...")

# open to read in text mode(default mode is "rt"), no need to f.close() because of "with"
with open("Example.txt") as f:
	f.read()

# writelines
f = open('Example.txt', mode='at', encoding='utf-8')
f.writelines( ['example text, \n', you cannot say, or guess, 'where the sun beats\n'] )
f.close()

# readline and readlines
f.readline() 													  		# read single line
f.readlines()                                    						# list of all the lines

# method track the number of bytes read
f.tell()

# reposition of the read/write pointer within the file
f.seek(position)

# open to read in binary mode
with open("Example.jpg", mode="rb") as image:
	print(len(image.read())/1024, "KB")



# Reading and Writting with Buffer
# number of bytes
buffersize = 50000
infile = open('bigfile.txt', 'rt')
outfile = open('newfile.txt', 'wt')
buffer = infile.read(buffersize)
while len(buffer):
	outfile.write(buffer)
	print('.', end='')
	buffer = infile.read(buffersize)
print('Done.')





# RUNNING FILES AND SCRIPTS
# __name__  is the module's filename
if __name__ == '__main__':
	print('This program is being run by itself')
else:
	print('I am being imported from another module')

# python filename.py                                # This program is being run by itself
# import filename                                   # I am being imported from another module

# Every Python module has its __name__ defined. If this is ’__main__’, that
# implies that the module is being run standalone

# __main__.py
# Executable directories. Run: python folder_name (where __main__.py is)

# run files from python shell
exec(open("Example.py").read())





# OS
import os

# list containing names of the files and directories
os.listdir('D:/')
# list containing names of the files and directories(regexp)
# import glob
glob.glob('D:/*' )

# current working directory
os.getcwd()

# directory tree generator(dirpath, dirnames, filenames)
os.walk()

# create folders
os.mkdir('folder_name')

# change the current working directory to path
os.chdir(path)

# perform a stat system call on the given path
os.stat(path)

# system dependence separator
os.sep

# os.system function which runs the command as if it was run from the system, in the shell - it returns 0 if
# the command was successfully, else it returns an error number
os.system("dir")

# returns the directory component of a pathname
os.path.dirname(path)

# returns the absolute version of a path
os.path.abspath(path/file_name)

# split the extension from a pathname, returns (root, ext)
os.path.splitext(string)

# returns the final component of a pathname
os.path.basename(path)





# SYS
import sys

# SYS.PATH (THE 'import' SEARCH PATH)(built-in modules - in C)
# the list of search path imports
sys.path
sys.path.insert(0,'C:\\...')
# add to the end of the list
sys.path.extend(['path1', 'path2'])

# contains the list of command line arguments
sys.argv

# imported modules
sys.modules

# print(file=sys.stdout)
sys.stdout.write(string)

# exit the interpreter by raising SystemExit(status)
sys.exit(status)

# size of the object in bytes
sys.getsizeof(object)

# who called the function(is it coroutine)
sys.getframe(func).f_code.co_flags





# TIME/DATETIME
import time

# localtime returns (tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)
time.localtime()									# ".".join(str(i) for i in time.localtime()[:6])

# convert a time in seconds since the Epoch to a string in local time
time.ctime()

# return the current time in seconds since the Epoch
time.time()



import datetime

# datetime.datetime
# date
datetime.datetime(2014, 2, 27, 12, 22, 45, 38543).date()

# time
datetime.datetime(2014, 2, 27, 12, 22, 45, 38543).time()

# local datetime
datetime.datetime.now()

# utc datetime (Universal Time Coordinated)
datetime.datetime.utcnow()

# strftime - from datetime object to string
datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#								('%A %-d %B %Y')

# strptime - from string to datetime object
# string, format -> new datetime parsed from a string
datetime.datetime.strptime('2000-01-01 00:00', '%Y-%m-%d %H:%M')
#						  ('Monday 6 January 2014, 12:13:31', '%A %d %B %Y, %H:%M:%S')

# combine
datetime.datetime.combine(dt_object.date(), dt_object.time())



# datetime.date
datetime.date(year=2014, month=1, day=6)
datetime.date.today()

date_object.year
date_object.month
date_object.day
date_object.weekday()
date_object.isoweekday()

# local date from a POSIX timestamp
datetime.date.fromtimestamp(1000000000)



# datetime.time
# datetime.time.min, datetime.time.max, datetime.time.resolution
datetime.time(hour=23, minute=57, second=59, microsecond=999)
time_object.isoformat()
time_object.strftime('%Hh%Mm%Ss')



# datetime.timedelta
# timedelta instance store only days, seconds, microseconds
datetime.timedelta(days=4, hours=3, minutes=45, weeks=3)
datetime.date.today() + datetime.timedelta(weeks=3)





# RANDOM
import random

# random floating point number from (0, 1)
random.random()

# get a random floating point number in the range (start, stop)
random.uniform(-10.5, 10.5)

# choose a random integer number from range (start, stop, step)
random.randrange(-10, 101, 3)

# choose a random element from a non-empty sequence
random.choice('asdfgh')

weighted_choices = [('Red', 3), ('Blue', 2), ('Yellow', 1), ('Green', 4)]
population = [val for val, cnt in weighted_choices for i in range(cnt)]
random.choice(population)

# chooses k unique random elements from a population sequence or set
random.sample(range(10000000), 60)

# shuffle list x in place, and return None
random.shuffle(items)





# IMPORTLIB
import importlib

obj = getattr(importlib.import_module('module_name'), 'object_name')





# COLLECTIONS
from collections import OrderedDict, Counter, defaultdict, deque

# dictionary that remembers insertion order
OrderedDict()



# dict subclass for counting hashable items
Counter('aaabbc')

# n most common elements
counter_obj.most_common(n)

# total of all counts
sum(counter_obj.values())


# dict subclass that calls a factory function to supply missing values
# defaultdict means that if a key is not found in the dictionary, then instead of a KeyError being thrown,
# a new entry is created. The type of this new entry is given by the argument of defaultdict.
defaultdict(callable)



# list-like container with fast appends and pops on either end
deque(iterable, maxlen=None)

deque_obj.append(obj)
deque_obj.appendleft(obj)
deque_obj.pop()
deque_obj.popleft()





# Regular Expressions
# import re

# re.compile(pattern)                                      # compile pattern
# re.sub(pattern, replacement, string, count=0, flags=0)
# re.sub("D:[^\ ]Filmy[^\ ]", "", string)                  # D:\Filmy\ => ""
# re.findall("[a-zA-Z]+|[0-9]+", string)                   # every word, and every number
# re.findall('http[^"]*', string)                          # every string that start with http and end with "
# re.findall('href="(.+?)"', string)                       # everything between href=" and "
# re.findall(' s.*? s', string)                            # regular expression looks for a space,
#                                                          # an s, and then the shortest possible
#                                                          # series of any character(.*?),
#                                                          # then a space, then another s
# re.split(r'[;,\s]\s*', 'asdf fjdk; afed, fjek,asdf, foo')
# re.search(pattern, string, flags=0)
# re.search(pattern, string, re.VERBOSE)  # verbose regular expressions

# re.match("c", "abcdef")                 # No match
# re.search("c", "abcdef")                # Match
# re.groups()

# [^/]+                                   # which will match everything up to the first /
# ^ matches the start of a string         # ^cos
# $ matches the end of a string.          # cos$
# ?                                       # ? makes a pattern optional
# \b                                      # matches a word boundary
# M?M?M?                                  # you’re matching anywhere from zero to three M characters in a row
# ^M{0,3}$                                # {0,3} matches between 0 and 3 occurrences of a pattern, exacly 3, {3}
# \d                                      # matches any numeric digit (0–9)
# \D                                      # matches anything but digits
# +                                       # means 1 or more
# *                                       # means zero or more
# (A|B|C)                                 # means, match exactly one of A, B, or C
# (x)                                     # you can get the value of what matched by using the groups()
#                                           method of the object returned by re.search.







# To Do



# IMPORT ITERTOOLS
# Itertools
# imap, ireduce, ifilter i izip === map, reduce, filter, zip (python 3)
# islice - umożliwia podział potencjalnie nieskończonego generatora
# takewhile - dodaje warunek, który powoduje zakończenie działania generatora
# cycle - rzez ciągłe powtarzanie skończonego generatora powoduje, że staje się on nieskończony
# count - ???
import itertools
# chains multiple iterators together
qiter = itertools.chain(query_set_1, query_set_2)



# IMPORT JSON
import json



# IMPORT FUNCTOOLS
import functools
functools.partial(foo, 10, 20, v1=23)
functools.reduce(function, iterable, initializer)
functools.wraps



More regular expressions, e.g string stars with st and ends with st
math.copysign(1, y)
math.log10(abs(y))
# ===========================
Parallel programming
Data split(big data, each proces have own set of data)
Functional split(multiple small tasks)
process
threads/subtask in parent process
Binary trees
# ===========================
# FORMAT method
re.compile(
    r"(?P<fill_align>.?[\<\>=\^])?"
    "(?P<sign>[-+ ])?"
    "(?P<alt>#)?"
    "(?P<padding>0)?"
    "(?P<width>\d*)"
    "(?P<comma>,)?"
    "(?P<precision>\.\d*)?"
    "(?P<type>[bcdeEfFgGnosxX%])?" )

execfile(filename, globals, locals) ===
exec(compile(open(filename, "rb").read(), filename, 'exec'), globals, locals) ===
exec(open(filename).read())

regular expressions:
.
\s
\w


import inspect
=============





# REST - representational state transfer
# Podejście REST sugeruje przygotowanie struktury adresu URL dopasowanej do struktury danych
# RESTful URLs are very useful for designing CRUD interfaces(Create, Read, Update, and Delete)

# API - Application Programming Interface
