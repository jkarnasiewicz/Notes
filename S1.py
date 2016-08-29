# HELP
# dir(object)        every method for object or dir() for list of names defined in the current module
# help(object)
# object.__doc__     documentation Strings
# .....__class__
# type(object)       type of the object
# id()				 id of the object

# Class_Name.__mro__ == Class_Name.mro()    # info about linear order of the inheritance(super())

# Immutable basic types (numbers, strings, tuples)
# Mutable objects such as lists, dictionaries, and other types - meaning you can change their content without
# 																 changing their identity

# Sequence (such as a string, bytes, tuple, list, or range)
# Collection (such as a dictionary, set, or frozen set).

# Module < Package

# Runing python with -O option, allow to run python without active assertions



# IMPORT MODULES
# import ...
# from ... import ... as ...
# from ... import *                                	# This will import all public names but would not
#                                                     import __something__ because it starts with
#                                                     double underscores.
# from .b import B                        			# Relative imports
# from ..a import A (parent directory)
# __all__ = ['names', 'available', 'in_module']		# In __init__.py, if we "import *" we get only names from that list
# __main__.py 										# Executable directories. Run: python folder_name(where __main__.py is)


# RUNNING FILES AND SCRIPTS
# exec(open("./filename").read())
# exec(open("C:/Python33/Scripts/1.py").read())    	# run files from python shell

# C:\Python33>python ./Scripts/1.py                	# run files from cmd
# C:\Python33>python C:/.../1.py



# SYS.PATH (THE import SEARCH PATH)(built-in modules - in C)
# import sys
# sys.path 											# the list of search path imports
# sys.path.insert(0,'C:\\...')
# sys.path.extend(['path1', 'path2'])    			# add to the end of the list

# sys.argv                 							# contains the list of command line arguments


# import os, glob
# __file__											# absolute file path
# os.listdir('D:/')
# os.path.splitext('')
# os.path.dirname(__file__)							# current working directory
# os.getcwd()              							# current working directory
# os.path.abspath(__file__)							# current working file
# os.sep                   							# system dependence separator

# os.chdir()               							# change the current working directory to path
# os.stat(file)            							# file information e.g. st.size
# os.mkdir                 							# create folders
# os.system("dir")         							# os.system function which runs the command as if
#													  it was run from the system, in the shell - it returns 0 if
#                            						  the command was successfully, else it returns
#                            						  an error number.
# sys.getsizeof(object)								# size of the object in bytes
# glob.glob('D:\Filmy\*' ) 							# every file in the directory


# RUNING SCRIPTS and Module Built-in attribute
# if __name__ == '__main__':                        # __name__  is the module's filename
# 	print('This program is being run by itself')
# else:
# 	print('I am being imported from another module')

# python filename.py                                # This program is being run by itself
# import filename                                   # I am being imported from another module

# Every Python module has its __name__ defined. If this is ’__main__’, that
# implies that the module is being run standalone



# BUILT-IN FUNCTIONS
locals()											# return a dictionary mapping local variable names to their value

global variable_name								# create global name
nonlocal variable_name								# introduce names from the enclosing namespace into the local namespace

callable(obj)										# return True or False(callable or not)

# isinstance
isinstance(3, (int, str))
# issublclass
issubclass(list, object)

all(iterable)										# return True if every element of the iterable is truthy
#													# all([]) returns True

any(iterable)										# return True if any element of the iterable is truthy
# 													# any([]) returns False

# has, get and setattr
a = [1, 4, 'reduce']
hasattr(a, "index")									# Results are True or False
getattr(object, "atribute_name", default)			# default argument if "atribute_name" doesn't exist
setattr(object, "atribute_name", value)

map(function, sequence, sequence)					# apply a function to every element in a sequence, producing a new sequence
# 													  finish when get the last element in the sequence

filter(function, sequence)							# apply a function to each element in a sequence, constructing a new sequence
# 													  with the elements for witch the function returns True




# CONVERT VALUES
# int(x)									 # unlimited precision signed integer
# int(x, base)								 # bases from 2 to 36
# bin(x) - base 2, oct(x) - base 8, hex(x) - base 16
# float(x)	  								 # 1bit(sign) - 11bits(exponent) - 52bits(fraction)
#											 # 15 to 17 bits of decimal precision
# str(x)      								 # convert x to string
# repr(x)

# ascii()	  								 # replace non-ASCII characters with escape sequences
# chr(97)      => returns the string 'a'     # return the string representing a character
#                                              whose Unicode codepoint is the integer
# ord('a')     => returns the integer 97     # return an integer representing the Unicode
#                                              code point of that character




# NUMBERS
# 17 / 3        => 5.666666666666667 	# classic division returns a float(divide)
# 17 // 3       => 5                 	# floor division discards the fractional part
# 17 % 3        => 2                 	# the % operator returns the remainder of the division(modulo)
# (-7) % 3					 => 2		# float remainder
# Decimal(-7) % Decimal(3)	 => -1		# decimal remainder
# divmod(5, 3)	=> (1, 2)		     	# (floor division, remainder)
# 5 * 3 + 2     => 17                	# result * divisor + remainder
# 2 * 3         => 6                 	# multiply
# 2 ** 4        => 16                	# power == pow(2,4)
# abs(-4)								# absolute value of a number
# round(17/9)          				 	# rounding function
# 										# Be carefull with float numbers which can't be represented exacly in binary
# round(Decimal('3.456'), 2)       		# how many digits we want to round to
# round(Fraction(57, 100), 1)			# Fraction(3, 5)

# +=, -=, *=, /=, //=                	# increment and decrement operators
# <, >, <=, >=, ==, !=				 	# comparing values
# is, is not						 	# testing ids of the objects/compare ids
# and                  				 	# i
# or                   				 	# lub
# bool(a) != bool(b)                    # Exclusive or(alternatywa wykluczająca)

# Bitwise operators
# 2 << 2        => 8   # 2 is represented by 10 in bits(left shift)
#                        Left shifting by 2 bits gives 1000 which represents the decimal 8.
# 11 >> 1       => 5   # (right shift) Shifts the bits of the number to the right by the number
#                        of bits specified. 11 is represented in bits by 1011 which when right
#                        shifted by 1 bit gives 101 which is the decimal 5.

# Decimal
# import decimal
# decimal.getcontext().prec = 6
# decimal.Decimal('0.8')				# always use quotes
# from decimal import Decimal as d
# d('1.234567') + d(1)	=> d('2.23457')
# d('Infinity'), d('-Infinity'), d('NaN')

# Fractions (ulamki)
# from fractions import Fraction as f
# f(1,2)+f(3,4)							=> 5/4
# f('0.1') == f(Decimal('0.1'))			=> 1/10
# f(0.1)								=> 3602879701896397/36028797018963968

# Complex Numbers
# complex(2, 3)							=> (2 + 3j)
# complex('2+3j')						=> (2 + 3j)
# c = 2 + 3j							=> (2 + 3j)
# c.real 								=> 2.0
# c.imag 								=> 3.0
# c.conjugate()							=> (1 - 3j)		# sprzężenie zespolone

# import cmath - Mathematical functions for complex numbers
# cmath.sqrt(-1)						=> 1j
# cmath.polar(1+1j)						=> (1.4142135623730951, 0.7853981633974483) = modulus, phase
# cmath.rect(modulus, phase)

# Statistics
# import statistics as s
# a = [2, 4, 5, 1, 3, 6, 3, 7]
# print(s.median(a), s.mean(a), s.variance(a))



# STRINGS
# r"This is a\tstring!"					   # raw string
# len('Python')                            # length of the string

# "string"[0:6:3]              => 'si'     # slice [start:stop:step]
# "string"[-1]                 => 'g'      # last character
# "string"[2:5]                => 'rin'    # characters from position 2 (included) to 5 (excluded)
# "string"[-2:]                => 'ng'     # characters from the second-last (included) to the end
# "python"[:2] + "python"[2:]  => 'python'

# "key/value".split("/",1)          	=> ['key', 'value']    # .split() by "space"
# .splitlines()                     	=> []
# "-".join(str(i) for i in [1, 3, 6])   => "1-3-6"
# " ".join("string")                	=> "s t r i n g"
# "string".replace("r", "-", 5)     	=> "st-ing"
# "string".find('r')                	=> 2

# .isalnum()                       # checks if the strnig has only alphanumeric
#                                  # characters in it
# .isalpha()                       # only alpha characters
# .isdigit()                       # checks if there are only digits

# .center(80)
# .capitalize()
# .lower()
# .upper()
# .swapcase()
# .lower().endswith('.mp3')        # find extension
# .rstrip()                        # removing whitespaces from the end of string
# .strip([chars])				   # all chars have been stripped from begining and
#								   # the end of the string

# .encode('utf-8')                 # from bytes to unicode characters e.g. gb18030, big5
# .decode('utf-16')				   # from unicode characters to bytes


# Formating And "Print"
# li = [123, 456, 789]
# print(*li, sep = " \t", end = "\n")						# optional kwargs: file = ''

# s = 'This is a string. \
# This continues the string.'

# \n - line feed
# \r - carriage return
# \t - tabulator

# print( "{0}'s password is {1}".format(username, password) )
# print( "real part:{0.r}, imaginary part:{0.i} i liczba {1:.1f}".format(Complex(3, 6), 123.345) )
# print( "{0:>40.1f}".format(123.345) )					   # to righr, 40 characters, one character after dot, float
# print('{0}, lub {0:.3}'.format(1/3))
# print('{0:_^11}'.format('hello'))

# print('{0!r}'.format(object))							   # we're requesting __repr__()
# print('{0!s}'.format(object))							   # we're requesting __str__()

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {Jack}; Sjoerd: {Sjoerd:.2f}; Dcab: {Dcab}'.format(**table))



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



# TUPLE
# t = 1,                                  # creating tuple with one element
# t = 1, 2, 3, 4, 3

# t.count(3)
# t.index(4)

# min(t)
# max(t)



# LISTS
# cubes = [1, 8, 27, 65, 125]
# cubes[3] = 64  # replace the wrong value

# [['a', 'b', 'c'], [1, 2, 3]]
# x[0]      => ['a', 'b', 'c']
# x[0][1]   => 'b'

# a = [66.25, 333, 333, 1, 1234.5]
# a.count(333) => 2
# a.count('x') => 0
# a.index(333) => 1
# 333 in a     => True
# 333 not in a => False

# a.insert(2, -1) => [66.25, 333, -1, 333, 1, 1234.5]
# a.append(333)   => [66.25, 333, -1, 333, 1, 1234.5, 333]
# a.extend() - The extend() method takes a single argument,
#              which is always a list, and adds each of the
#              items of that list to a list

# a.remove(333)  # remove the first occurrence of number 333
# del a[3]       # delete the object at index 3
# a.pop()        =>  333
# a.pop(1)       =>  -1

# a.reverse()    =>  [333, 1234.5, 1, 333, -1, 66.25]
# a.sorted()     =>  [-1, 1, 66.25, 333, 333, 1234.5]


# Using Lists as Stacks (Stos)
# stack = [3, 4, 5]
# stack.append(6)   =>  [3, 4, 5, 6]
# stack.pop()       =>  6
# stack             =>  [3, 4, 5]
# stack.pop(0)      =>  3


# Using Lists as Queues (Kolejka)
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")
# queue.popleft()
# 'Eric'
# queue
# deque(['Joh', Michael', 'Terry'])



# SETS (Unordered Collection With No Duplicate Elements)(Zbiory)
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# {'orange', 'banana', 'pear', 'apple'}  # duplicates have been removed

# basket.add()     The add() method takes a single argument, which can be any datatype, and adds the given value to the set
# basket.update()  You can actually call the update() method with any number of arguments

# basket.remove()  if the value doesn’t exist in the set, the remove() method raises a KeyError exception.
# basket.discard()

# a = set('abracadabra') => {'a', 'r', 'b', 'c', 'd'}   # unique letters in a
# b = {'m', 'l', 'z', 'a', 'c'}
# 'r' in a  => True                                     # fast membership testing
# a.difference(b),           a - b     => {'r', 'd', 'b'}                          # letters in a but not in b (Roznica)
# a.union(b),                a | b     => {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'} # letters in either a or b (Suma)
# a.intersection(),          a & b     => {'a', 'c'}                               # letters in both a and b (Iloczyn)
# a.symetric_difference(b),  a ^ b     => {'r', 'd', 'b', 'm', 'z', 'l'}           # letters in a or b but not both (Roznica symetryczna)

# if(len(set(exp_type)) != 1)                                                      # If True, list have more than one diffrent object

# Subset and Superset(podzbiory, nadzbiory i zawieranie sie zbiorow)
# a.issubset(b)   => False
# a.issuperset(b) => False



# DICTIONARIES (Unordered Set Of Key: Value Pairs)
# a = {'sape': 4139, 'guido': 4127, 'jack': 4098}
# a = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# a.get(key, default=None))          			# like switch
# factory_class = {'a': ClassOne, 'b': ClassTwo}.get('b', ClassThree)		# factory_class(arg1, arg2)

# a.setdefault(key, default=None)				# the method will set dict[key]=default if key is not already in dict

# a['jack'] = 9744								# update existing entry
# a['thx'] = 4567								# add new entry
# a.update(dictionary)							# adds dictionary key-values pairs to 'a'

# del a['sape']									# remove entry with key 'sape'
# a.pop('sape')                                 # remove and return value of 'sape'
# a.clear()										# remove all entries in dict
# del a  										# delete entire dictionary

# b = dict( one = 'first', two = 'second', three = 'third', four = 'fourth',
#			five = 'fifth', **a)
# b.items()
# b.keys()
# b.values()
# dict.fromkeys(range(10), 10)
# print('jack' not in b)



# Comparing Sequences And Other Types
# [1, 2, 3]              < [1, 2, 4]
# 'ABC' < 'C' < 'Pascal' < 'Python'
# (1, 2, 3, 4)           < (1, 2, 4)
# (1, 2)                 < (1, 2, 1)
# (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)



# READING AND WRITING FILES
# with open("Example.txt", mode = "w", encoding = "utf-8") as plik:   # creating the new file or overwriting the existing file
#     plik.write("Hello\n...")
# with open("Example.txt") as plik:                                   # default mode is "r"
# 	print(plik.read())                                                # no need to plik.close() because of "with"
# with open("Example.txt", mode = "a", encoding = "utf-8") as plik:   # append to the file instead of overwriting
# 	plik.write("\nYupii\r...")
# with open("Example.txt", mode = "r", encoding = "utf-8") as plik:
# 	print(plik.read())

# print("Example.txt".readlines())                                    # List of Strings

# with open("0.52930300392065.jpg", mode = "rb") as image:            # open to read in binary mode
# 	print(len(image.read())/1024,"KB")
# image.tell(), image.read(?), image.seek(?)                          # methods track the number of bytes read


# Reading and Writting with Buffer
# buffersize = 50000                    # number of bytes
# infile = open('C:/Python34/Scripts/bigfile.txt', 'r')
# outfile = open('C:/Python34/Scripts/newfile.txt', 'w')
# buffer = infile.read(buffersize)
# while len(buffer):
# 	outfile.write(buffer)
# 	print('.', end='')
# 	buffer = infile.read(buffersize)
# print('Done.')



# RANDOM
# import random
# print(10*random.random())					# Random number from (0, 1)
# print(random.uniform(-10.5, 10.5))

# a = random.randrange(0, 101, 3)
# print(a)

# weighted_choices = [('Red', 3), ('Blue', 2), ('Yellow', 1), ('Green', 4)]
# population = [val for val, cnt in weighted_choices for i in range(cnt)]
# print(population)
# print(random.choice(population))

# a = random.choice('asdfgh')
# print(a)

# a = random.sample(range(10000000),60)
# print(a)

# items = [1, 2, 3, 4, 5, 6, 7]
# random.shuffle(items)
# print(items)



# PICKLE (Python objects converted into a byte stream)
# import pickle
# li = [2, "Hello", 3.14, "..."]
# with open("Example.data", mode = "wb") as plik:
# 	pickle.dump(li, plik)

# with open("Example.data", mode = "rb") as plik:
# 	example = pickle.load(plik)



# TIME
# import time
# time.localtime()
# time.time()
# print(".".join(str(i) for i in time.localtime()[:6]))
# time.sleep(2)

# import datetime

# dt = datetime.datetime(2014, 2, 27, 12, 22, 45, 38543)
# print(dt.now(), dt.date(), dt.time(), dt.utcnow())
# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))                 # strftime - from datetime object to string
# 										('%A %-d %B %Y')
# print(datetime.datetime.strptime('2000-01-01 00:00', '%Y-%m-%d %H:%M')       # strptime - from string to datetime object
# 								  ('Monday 6 January 2014, 12:13:31',
# 								   '%A %d %B %Y, %H:%M:%S')
# datetime.datetime.combine(dt.date, dt.time)

# print(datetime.date(year=2014, month=1, day=6))
# d = datetime.date.today()
# d.year, d.month, d.day, d.weekday(), d.isoweekday()
# print(datetime.date.fromtimestamp(1000000000))

# t = datetime.time(hour=23, minute=57, second=59, microsecond=999)
# t.isoformat(), t.strftime('%Hh%Mm%Ss')
# print(datetime.time.min, datetime.time.max, datetime.time.resolution)

# timedelta instance store only days, seconds, microseconds
# datetime.timedelta(days=4, hours=3, minutes=45, weeks=3)					   # constructor accepts and sums
# datetime.date.today() + datetime.timedelta(weeks=3)



# TARFILE
# import tarfile
# import os
# import glob
# os.mkdir('Apps')
# for i in glob.glob('D:/Science/And Whatnot Final/*'):
#   t = tarfile.open(i)
#   try:
#       t.extractall('Apps')
#   except:
#       continue



# SQLITE3
# import sqlite3
# db = sqlite3.connect('test.db')
# db.row_factory = sqlite3.Row                    # specify how rows will be returned from the cursor
# db.execute('drop table if exists test')
# db.execute('create table test (t1 text, i1 int)')
# db.execute('insert into test (t1, i1) values (?, ?)', ('one', 1))
# db.execute('insert into test (t1, i1) values (?, ?)', ('two', 2))
# db.commit()
# cursor = db.execute('select * from test order by t1')
# for row in cursor:
# 	print(dict(row))                            # dict because of the row_factory
# 	print(row['t1'], row['i1'])




# To Do
sys.modules 				# modules imports
More regular expressions, e.g string stars with st and ends with st
math.copysign(1, y)
math.log10(abs(y))
# ===========================
Parallel programming
Data split(big data, each proces have own set of data)
Functional split(multiple small tasks)
process
threads/subtask in parent process
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

os.path.splitext
os.path.basename

import pdb
pdb.set_trace()

# Monkey patching lub guerrilla patching to technika polegająca na dostarczeniu kodu rozszerzającego
# lub modyfikującego inny kod w czasie jego działania (podmiana funkcji)
from django.utils import text
from slugify import slugify_de as awesome_slugify
awesome_slugify.to_lower = True
text.slugify = awesome_slugify

# logging
import logging
logger = logging.getLogger('app.location')
logger.info('any message')

# stx
# testing
coverage
c9.io
https://github.com/stxnext/php-sources
https://github.com/stxnext/grot-client
grot-server.games.stxnext.pl/games
grot-server.games.stxnext.pl

# imports
import importlib
MyClass = getattr(importlib.import_module(module_name), class_name)
middleware = MyClass()

sys.exit



from coupons.models import Coupon
my = Coupon.objects.filter(template=661)  # 703 generate numeric only
beta = Coupon.objects.filter(template=657)  # 704

if my.count() == beta.count():
	for i in range(50):
		instance = beta[i]
		instance.code = 'TECHL' + str(my[i].code)
		instance.save()

import inspect
=============
x < 10 < x*10 < 100			# x < 10 and 10 < x * 10 and x*10 < 100

import itertools
qiter = itertools.chain(query_set_1, query_set_2)
