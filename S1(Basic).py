# GENERAL INFORMATION

dir(object)        				# methods object or dir() for list of names defined in the current module
help(object)

object.__doc__     				# docstring for a function or module object
object.__name__					# name of a function or module object, or just __name__ for current module name
object.__file__					# object file path, or just __file__ for current file path(absolute path)
object.__dict__					# a dictionary or other mapping object used to store an object’s (writable) attributes

type(object)       				# type of the object, it is the same as object.__class__
# 								# creating class:	C = type('C', (object,), dict(__init__=__init__, add=add))
id(object)				 		# id of the object

# Immutable basic types such as numbers, strings, bytes, frozensets and tuples

# Mutable objects such as lists, dictionaries, sets and other types -
# meaning you can change their content without changing their identity

# Sequence (such as a string, bytes, tuple, list, or range)
# Collection (such as a dictionary, set, frozenset or bytearray)

# every python object has an identity, a type and a value

# python objects/variables - think of named references to objects rather than variables(variables are just aliases/labels(etykiety))

# del does not delete an object, just a reference to it(name/label)

# shallow copy - copy only the reference to the key, value paires not the objects themselves e.g.
# a = [[0, 1]]*4
# a[2].append(7)

# Dynamic type system
# In dynamic type system objects types are only resolved at runtime (w czasie wykonywania programu)
# (if type-checking is performed at compile time, the language is statically typed)

# Strong type system
# In a strong type system there is no implicit type conversion
# e.g. 'string' + 43 => TypeError
# Java, C++ and Python are strongly typed; PHP, JavaScript and Perl are weakly typed

# Functions in Python are first-class objects
# (created at runtime, assigned to a variable or element in a data structure, passed as an argument to a function, returned as the result of a function)

# Function parameters as references

# Default argument expressions evaluated once, when def is executed
# Always use immutable objects as a default argument value

# Value equality(equivalent 'contents') vs. identity(same object id())
# (równość wartości a równość tożsamości)
# Value comparison can be controlled programatically('__eq__')
# [] == [] => True
# [] is [] => False

# Python does not require you to declare variables, but assumes that a variable assigned in the body of a function is local

# Python name scopes(names are looked up in four nested scopes)
# Local - inside the current function
# Enclosing - any and all enclosing functions
# Global - top-level of module
# Built-in - provide by the builtins module

# Module < Package





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
# import builtins

# return a dictionary representing the current global symbol table
globals()

# return a dictionary mapping local variable names to their value
locals()

# use global to assign to global references from a local scope
global variable_name

# introduce names from the enclosing namespace into the local namespace
nonlocal variable_name

# return the __dict__ of obj, vars(obj) == obj.__dict__
vars(obj)

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

# sorts any iterable series and returns a list, 'key' specifies a function of one argument
sorted(iterable, key=None, reverse=False) 

# reverses any iterable series, returns a reverse iterator
reversed(sequence)

# evaluate a single dynamically generated Python expression and returns it value(cannot evaluate a statement, e.g. x = 5)
eval('a*3')

# execute dynamically generated Python code, always returns None
exec('a = 7')

# slice
sequence[slice(40, None, 2)] == sequence[40::2]

	# indices
	# This method produces 'normalized' tuples of non-negative start, stop and stride integers
	# adjusted to fit within the bounds of a sequence of the given length
	# slice_object.indices(len) -> 						# (start, stop, stride)
	slice(None, 10, 2).indices(5)                       # (0, 5, 2)
	slice(-3, None, None).indices(5)                    # (2, 5, 1)





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

# increment and decrement operators (augmented assignment operators)
# these change their first argument in-place, if it is mutable object if not, the operators works like the normal ones
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



# import math

# return the square root of x
math.sqrt(x)

# with one argument, return the natural logarithm of x (to base e)
math.log(x, base)

# return the base-10 logarithm of x
math.log10(x)

# return x factorial (silnia)
math.factorial(6)

# return the ceiling of x, the smallest integer greater than or equal to x
math.ceil(-0.5)

# return the floor of x, the largest integer less than or equal to x
math.floor(x)



# import cmath - mathematical functions for complex numbers
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

# bitwise Exclusive Or (xor(a, b))
a ^ b





# STRINGS
# raw string (no 'escape sequences' - nothing in the string should be escaped)
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

# find returns index of first occurrence of character
'string'.find('r')                					# 2

# checks if the string has only alphanumeric characters in it (A-Z, a-z and 0-9)
''.isalnum()

# only alpha characters (A-Z, a-z)
'Ng'.isalpha()

# checks if there are only digits (0-9)
'37'.isdigit()

.capitalize()
.lower()
.islower()
.upper()
.swapcase()
# find extension
.lower().endswith('.mp3')
# all chars have been stripped from begining and the end of the string
.strip('chars')
# removing whitespaces from the end of string
.rstrip()
.center(80)

# We decode bytes to str to get human readable text, and we encode str to bytes for storage or transmission

# Encoding to byte sequence
# from string to byte object (python 3)
string_object.encode(encoding='utf-8', errors='strict')
# silently skips characters that cannot be encoded
string_object.encode(encoding='utf-16', errors='ignore')
# substitutes unencodable characters with '?'
string_object.encode(encoding='iso8859_1', errors='replace')
# replaces unencodable characters with a XML entity
string_object.encode(encoding='cp437', errors='xmlcharrefreplace')
# replace each non-decodable byte with a code point in the Unicode range from
# U+DC00 to U+DCFF that lies in the so-called 'Low Surrogate Area' of the standard
string_object.encode(encoding='cp437', errors='surrogateescape')

# Decoding to string
# from byte to string object (python 3)
byte_object.decode(encoding='utf-8', errors='strict')

# utf
# Unicode Transformation Format(system kodowania Unicode), using from 8 to 32 bits(bitów)
# or from 1 to 4 bytes(bajtów) to encode single character fully compatible with ASCII
# (the byte is a unit of digital information that most commonly consists of eight bits)



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
# += is a shortcut for the list.extend()
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
# tri = [(1, 'one', 'jeden'), (2, 'two', 'dwa'), (3, 'three', 'trzy'), (4, 'four', 'cztery')]
# tri.sort(key=lambda trio: trio[1])
li.sort(key=callable, reverse=True)





# ARRAY
import array
# return a new array whose items are restricted by typecode, and initialized from the optional initializer value,
# which must be a list, string or iterable over elements of the appropriate type

# arrays represent basic values(characters('u'), integers('l/q'), floats('f/d')) and behave very much like lists,
# except the type of objects stored in them is constrained
array.array(typecode, iterable)

# write all items(as machine values) to the file object f
floats.tofile(f)

# read n objects from the file object f and append them to the end of the array
floats.fromfile(f, n=10**7)





# SETS (unordered collection of unique, immutable, hashable objects)(Zbiory)
# implemented with hash tables
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



# FROZENSET
# frozensets are like sets except that they cannot be changed, i.e. they are immutable
# the set type is not hashable, but frozenset is, so you can have frozenset elements inside a set
frozenset({'a', 'b', frozenset({1, 3, 7})})




 
# DICTIONARIES (unordered mapping from unique, immutable keys to mutable values -> Key: Value)
# implemented with hash tables
di = {'sape': 4139, 'ivy': 4127, 'jack': 4098}
di = dict([('sape', 4139), ('ivy', 4127), ('jack', 4098)])

# get object - like switch
di.get(key, default=None)
factory_class = {'a': ClassOne, 'b': ClassTwo}.get('b', ClassThree)			# and then factory_class(arg1, arg2)

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

# The method fromkeys() creates a new dictionary with keys from sequence and values set to value
dict.fromkeys(sequence, value)
# di.fromkeys(range(10), 10) => {0: 10, 1: 10, 2: 10, 3: 10, 4: 10, 5: 10, 6: 10, 7: 10, 8: 10, 9: 10}





# MAPPING PROXY TYPE
# MappingProxyType builds a read-only mappingproxy instance from a dict
# mappingproxy is dynamic: any change in original dictionary is reflected
# MappingProxyType == type(type.__dict__)
from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
# changes cannot be made through d_proxy
# d_proxy[2] = 'x'
# only using original dictionary
# d[2] = 'B'





# READING AND WRITING FILES
# always set encoding
# file object support iterator protocol(and yield line by line)

open(file="path to file", mode="read/write/append, binary/text", encoding="text encoding")

# creating the new file or overwriting the existing file
with open("Example.txt", mode="wt", encoding="utf-8") as f:
	# the write method on a TextIOWrapper returns the number of Unicode characters written
	f.write("Hello\n...")

# append to the file instead of overwriting
with open("Example.txt", mode = "at", encoding="utf-8") as f:
	f.write("\nYupii\r...")

# open to read in text mode(default mode is "rt"), no need to f.close() because of "with"
with open("Example.txt", encoding="utf-8") as f:
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

# executable directories with __main__.py
python folder_name (where __main__.py is)

# interative mode with file_name.py
python -i file_name.py



# __name__  is the module's filename
if __name__ == '__main__':
	print('This program is being run by itself')
else:
	print('I am being imported from another module')

# python filename.py                                # This program is being run by itself
# import filename                                   # I am being imported from another module

# Every Python module has its __name__ defined. If this is ’__main__’, that
# implies that the module is being run standalone

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
# {f: os.stat(f).st_size for f in glob.glob('*')}
os.stat(path)

# system dependence separator
os.sep

# os.system function which runs the command as if it was run from the system, in the shell - it returns 0 if
# the command was successfully, else it returns an error number
os.system("dir")

# return the number of CPUs in the system
os.cpu_count()

# returns the directory component of a pathname
os.path.dirname(path)

# returns the absolute version of a path
os.path.abspath(path/file_name)

# split the extension from a pathname, returns (root, ext)
os.path.splitext(string)

# returns the final component of a pathname
os.path.basename(path)

# return tuple (head, tail) where tail is everything after the final slash
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')





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
# assign new variable to current module
setattr(sys.modules[__name__], 'new_variable', 7)

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

# alternate random number generator using sources provided by the operating system
# (such as /dev/urandom on Unix or CryptGenRandom on Windows)
random.SystemRandom().randint(3, 7)





# IMPORTLIB
import importlib

obj = getattr(importlib.import_module('module_name'), 'object_name')





# JSON
import json

# encoding basic python object to json
json.dumps({'a': 'text', '4': 5, '7': [3, 7]}, sort_keys=True, indent=4)			# or json.dump(obj, file_like_object)

# decoding json
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')								# or json.load(file_like_object)





# COLLECTIONS
from collections import OrderedDict, Counter, defaultdict, deque, namedtuple, UserDict, UserList, UserString

# dictionary that remembers insertion order
OrderedDict()



# dict subclass for counting hashable items
Counter('aaabbc')

# n most common elements
counter_obj.most_common(n)

# total of all counts
sum(counter_obj.values())



# dict subclass, that calls a factory function to supply missing values
# defaultdict means that if a key is not found in the dictionary, then instead of a KeyError being thrown,
# a new entry is created. The type of this new entry is given by the argument of defaultdict.
defaultdict(callable)

df = defaultdict(list)
for key, value in pairs:
	dd[key].append(value)



# list-like container with fast appends and pops on either end (double-ended queue)
deque(iterable, maxlen=None)

deque_obj.append(obj)
deque_obj.appendleft(obj)
deque_obj.pop()
deque_obj.popleft()



# namedtuple
# namedtuple function is a factory that produces subclasses of tuple enhanced with field names and a class name — which helps debugging
# can be used to build classes of objects that are just bundles of attributes with no custom methods, like a databaserecord
# you can access the fields by name or position
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))



# Subclassing built-in types is tricky
# This built-in behavior is a violation of a basic rule of object oriented programming: the
# search for methods should always start from the class of the target instance (self), even
# when the call happens inside a method implemented in a superclass

# Instead of subclassing the built-ins, derive your classes from UserDict, UserList and UserString
# from the collections module because the built-in methods mostly ignore user-defined overrides

# class DoppelDict(collections.UserDict):				# +
class DoppelDict(dict): 								# -
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

dd = DoppelDict(one=1) 									# -
print(dd)
dd['two'] = 2 											# +
print(dd)
dd.update(three=3) 										# -
print(dd)



# Interfaces for common python objects are avaible in collections.abc module
from collections.abc import Container, Iterable, Iterator, Set, Mapping
# we can also use them with isinstance or issubclass
isinstance({1, 3, 5}, (Container, Iterable))





# ITERTOOLS
# imap, ifilter, izip, xrange === map, filter, zip, range (python 3)
from itertools import (count, cycle, repeat, chain, islice, accumulate, groupby,
product, permutations, combinations_with_replacement, combinations)

# count, infinite iterators
count(start=0, step=1)

# cycle, repeats indefinitely
# make an iterator returning elements from the iterable and saving a copy of each,
# when the iterable is exhausted, return elements from the saved copy.
cycle(iterable)

# repeat, if time not specified, returns the object endlessly
repeat(object, times=5)

# chains multiple iterators together
# make an iterator that returns elements from the first iterable until it is exhausted,
# then proceeds to the next iterable, until all of the iterables are exhausted
# sorted(chain(collection_1, collections_2), key=lambda instance: instance.name.lower())
chain(*iterables)

# islice(umożliwia podział potencjalnie nieskończonego generatora)
# make an iterator that returns selected elements from the iterable
# islice(iterable, start, stop, step)
islice(iterable, 0, None, 3)

# make an iterator that returns accumulated results of other binary functions
# accumulate(sample, min)
accumulate(range(1, 11), operator.mul)

# make an iterator that returns consecutive keys and groups from the iterable.
# the key is a function computing a key value for each element
# it generates a break or new group every time the value of the key function changes
# (which is why it is usually necessary to have sorted the data using the same key function)
# groupby(iterable, key=None)
animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
for length, group in itertools.groupby(sorted(animals, key=len), len):
    print(length, '->', list(group))



# Combinatoric generators

# cartesian product (ciąg, kolejność istotna)
# product('ABCD', repeat=2) => AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# product('ABC', '!@#', range(2))
product(*iterables, repeat=1)

# r-length tuples, all possible orderings, no repeated elements (ciąg, kolejność istotna)
# permutations('ABCD', 2) => AB AC AD BA BC BD CA CB CD DA DB DC
permutations(iterable, r)

# r-length tuples, in sorted order, with repeated elements (zbiór, kolejność nieistotna)
# combinations_with_replacement('ABCD', 2) => AA AB AC AD BB BC BD CC CD DD
combinations_with_replacement(iterable, r)

# r-length tuples, in sorted order, no repeated elements (zbiór, kolejność nieistotna)
# combinations('ABCD', 2) => AB AC AD BC BD CD
combinations(iterable, r)





# FUNCTOOLS
from functools import wraps, lru_cache, partial, reduce

# without the use of this decorator factory, the name of the wrap function would have been
# 'wrapper', and the docstring of the original function would have been lost
@wraps

# Least Recently Used cache
# decorator to wrap a function with a memoizing callable that saves up to the maxsize most recent calls
# memoization: an optimization technique which works by saving the results of previous invocations of an
# expensive function, avoiding repeat computations on previously used arguments
@lru_cache(maxsize=128, typed=False)

# the partial is used for partial function application which 'freezes' some portion of
# a function’s arguments and/or keywords resulting in a new object with a simplified signature
# new_partial_func.func, new_partial_func.args, new_partial_func.keywords
partial(function, *args, **kwargs)

# repeatedly apply a function to the elements of a sequence, reducing them to a single value
# for +, |, ^ the initializer should be 0, but for *, & it should be 1.
reduce(function, iterable, initial_value)
reduce(lambda x, y: x + y, range(10), 0)
# or
from operator import add
reduce(add, range(100))





# INSPECT
from inspect import getsource, isclass, ismethod, getmembers, signature

# source code of the object
getsource(obj)

# check method
isclass(obj)

# list all members of object, getmembers(obj, filter function)
getmembers(obj, ismethod)

# Extracting the function signature
sig = signature(obj)

for name, param in sig.parameters.items():
	print(param.kind, ':', name, '=', param.default)





# WEAKREF
from weakref import ref, finalize, WeakSet
# References and weak references
# The presence of references is what keeps an object alive in memory. When the reference
# count of an object reaches zero, the garbage collector disposes the object

# Weak references to an object do not increase its reference count. The object that is the
# target of a reference is called the referent. Therefore, we say that a weak reference does
# not prevent the referent from being garbage collected.
# wref = weakref.ref(object)

# ender = weakref.finalize(object, callback_function, *args, **kwargs)
# ender.alive

# class that wants to keep track of all its current instances - this can be done with weak references
class Remember:
	members = []

	def __init__(self):
		r = ref(self)
		cls = type(self)
		cls.members.append(r)

	@classmethod
	def show_alive_members(cls):
		return [item for item in cls.members if item() is not None]

r, s, t = Remember(), Remember(), Remember()

print(Remember.show_alive_members())
del r, t
print(Remember.show_alive_members())





# REGULAR EXPRESSIONS
import re

# compile - compile regexp pattern
re.compile(r'pattern')
# re.compile(r'(\d{3})-(\d{3})-(\d{4})-(\d+)')

# findall - return all matches of pattern
# re.findall() is eager/re.finditer() is lazy
re.findall(pattern, string)
# re.findall("[a-zA-Z]+|[0-9]+", string)            # every word, and every number
# re.findall('http[^"]*', string)                   # every string that start with http and end with "
# re.findall('href="(.+?)"', string)                # everything between href=" and "
# re.findall(' s.*? s', string)                     # regular expression looks for a space,
#                                                   # an s, and then the shortest possible
#                                                   # series of any character(.*?),
#                                                   # then a space, then another s

# sub - replace occurances of pattern
re.sub(pattern, replacement, string, count=0, flags=0)
# re.sub("D:[^\ ]Filmy[^\ ]", "", string)                  # D:\Filmy\ => ""

# split - split string by occurrences of pattern
re.split(pattern, string)
# re.split(r'[;,\s]+', 'asdf fjdk; afed, fjek,asdf, foo')

# search - search for pattern in string
re.search(pattern, string, flags=0)
# re.search(pattern, string, re.VERBOSE)  # verbose regular expressions

# match - checks if string starts with pattern
re.match(pattern, string)
# re.match("c", "abcdef")                 			# no match
# re.search("c", "abcdef")                			# match

# group - returns one or more subgroups of the match
search_object.group()								# group(1)/groups()



# .					matches any character except a newline
# *                 match 0 or more repetitions of the preceding RE
# +                 match 1 or more repetitions of the preceding RE
# ?					match 0 or 1 repetitions of the preceding RE

# greedy - they match as much text as possible
# <.*> is matched against '<a> b <c>', it will match the entire string, and not just <a>

# non-greedy or minimal fashion - they match as few characters as possible
# <.*?> is matched against '<a> b <c>', will match only <a>



# ^					matches the start of a string
# $					matches the end of the string or just before the newline at the end of the string

# {m}				specifies that exactly m copies of the previous RE should be matched
# {m, n}			(greedy)causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as many repetitions as possible
# {m, n}?			(non-greedy)causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as few repetitions as possible

# [] 				indicate a set of characters, e.g. [amk] will match 'a', 'm', or 'k', special characters lose their special meaning inside sets e.g. [(+*)] will match any of the literal characters '(', '+', '*', or ')'
# [^/]+             which will match everything up to the first /

# (...)             matches whatever regular expression is inside the parentheses, and indicates the start and end of a group
# (A|B|C)           match exactly one of A, B, or C
# (?P<name>...)     similar to regular parentheses, but the substring matched by the group is accessible via the symbolic group name name

# \d                digit (0–9)
# \D                non digits

# \b                empty string boundary
# \B 				empty string non boundary

# \w 				matches any alphanumeric character including the underscore, equivalent to [A-Za-z0-9_]
# \W 				matches any non-word character(non-alphanumeric), equivalent to [^A-Za-z0-9_]

# \s 				whitespace
# \S 				non whitespace

# \A 				start of the string
# \Z 				end of the string
