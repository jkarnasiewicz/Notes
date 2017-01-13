# Conditional execution, the first true value from if or elif ends the if-else block
a = 11
if a > 12:
	print('a is greater than 12')
elif a > 10:
	print('a is greater than 10')
else:
	print('a is less or equal than 10')



# Conditional expresion/Conditional value
result = true_value if condition else false_value



# Else blocks

# for/else
# the else block will run only if and when the for loop runs to completion;
# i.e. not if the for is aborted with a break
for item in ['orange', 'apple']:
	if item == 'banana':
		break
else:
	raise ValueError('No banana flavor found!')

# while/else
# the else block will run only if and when the while loop exits because the condition
# became falsy; i.e. not when the while is aborted with a break

# try/else
# the else block will only run if no exception is raised in the try block. The official
# docs also state: 'Exceptions in the else clause are not handled by the preceding
# except clauses.'
try:
	dangerous_call()
except OSError:
	log('OSError...')
else:
	after_call()

# In all cases, the else clause is also skipped if an exception or a return, break or con
# tinue statement causes control to jump out of the main block of the compound statement



# Checking if n is prime number(Sprawdzanie czy n jest liczba pierwsza)
def check_prime(n):
	if n % 2 == 0:
		return False
	from_i = 3
	to_i = math.sqrt(n) + 1
	for i in range(from_i, int(to_i), 2):
		if n % i == 0:
			return False
	return True



# Prime Numbers(Liczby pierwsze)
def prime_numbers(lim):
	for i in range(2, lim+1):
		for j in range(2, i+1):
			if i == j:
				yield '{} is prime number'.format(i)
				break
			if i % j == 0:
				yield '{} is not prime number, {} * {}'.format(i, j, i/j)
				break

print([i for i in prime_numbers(100) if 'is prime number' in i])



# Prime factor(Rozklad liczby na czynniki pierwsze)
def decay(n):
	for i in range(2, n+1):
		while n % i == 0:
			yield i
			n = n/i

print([i for i in decay(273)])



# Signum function
def sign(x):
	return (x > 0) - (x < 0)



# Fibonacci series, the sum of two elements defines the next, return Fibonacci series up to n
def fib(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result

print(fib(100))



def silnia(n):
	result = 1
	while n > 1:
		result = result * n
		n -= 1
	return result

def factorial_recursion(n):
	return n*factorial_recursion(n-1) if n > 1 else 1

from functools import reduce
from operator import mul

def factorial_reduce(n):
	return reduce(mul, range(1, n+1), 1)

print(silnia(5))
print(factorial_recursion(6))
print(factorial_reduce(7))



# Reverse function
def reverse(iterable):
	for i in range(len(iterable)-1):
		iterable.insert(i, iterable.pop())
	return iterable

print(reverse([0, 1, 2, 3, 4, 5]))



# Default Mutable Argument Values(domyslne 'modyfikowalne' argumenty)
def f(a, L = []):
	L.append(a)
	return L

print(f(1))
print(f(2))
print(f(3, L = []))
print(f(4))



# Arbitrary Arguments List(samowolny, arbitralny)
def concat(*args, sep="/"):
   return print(sep.join(args))

concat("earth", "mars", "venus", "sun")
concat("earth", "mars", "venus", sep=".")



# Keyword-only arguments do not need to have a default value, but they can be still mandatory
def pow(a, *, x):
	return print(a**x)

pow(3, x=4)



# Unpacking List
args = [3, 6]
print(list(range(*args)))



# Unpacking Dictionary
def vol(voltage, who='you', action='vanish'):
	print("If you put", voltage, "volts through", who+",", who, "will", action+".")

d = {"voltage": 4000, "action": "fly"}
vol(**d)
vol(10)



# Unpacking Tuple
metro_areas = [
	('Tokyo', 'JP', 36.933, (35.689722, 139.691667)), #
	('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
	('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
]

for name, cc, pop, (latitude, longitude) in metro_areas:
	print('{:20} {}, {}'.format(name, latitude, longitude))



# Keyword-only args
def fun(*args, post, **kwargs):
	pass

# TypeError: fun() missing 1 required keyword-only argument: 'post'
fun(1, 2, 'st', p=33, k=44, j='o')



# Lambda Expressions
def f(a,b,c):
	return lambda x: a*x**2 + b*x + c

g = f(1,2,3)
print(g(1))
print(g(2))



# Comprehensions - short-hand syntax for creating collections and iterable objects
# List Comprehensions
print( [(x, y) for x in [-2,-1,0,1] for y in [1,2,3] if x!=y] )

print( [[y * 3 for y in range(x)] for x in range(10)] )


vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])



# Generator elementow
print(sum((1 for n in list_of_numbers if n % 3 == 0)))                  # divisible_by_three



# Rounding
from math import pi
print( [str(round(pi, i)) for i in range(1, 6)] )



# Transpose
matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
]

print([tuple(row[i] for row in matrix) for i in range(4)])
print(list(zip(*matrix)))



# Set Comprehensions + Dictionaries
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

b = {x: x**2 for x in (2, 4, 6)}
print(b)

c = {(i, v) for i, v in enumerate(['jack','jill','ivy'], start=1)}
print(sorted(c, key = lambda s: s[1]))



# Map (returns lazy iterable object)
# map(f, sequence1, sequence2) is equivalent to [f(x1, x2) for x1, x2 in zip(sequence1, sequence2)]
import itertools
f = list(map(ord, 'The quick brown fox'))
s = list(map(lambda x, y: x*y , itertools.count(), range(10)))
print(f, s, sep='\n')



# Filter (returns lazy iterable object)
# filter(function, sequence)
trues = filter(None, [0, 1, False, True, [], [1, 2, 3]])                        # Remove elements which evaluate to False
positives = filter(lambda x: x%2 == 0, [-3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])      # Even numbers
print(list(trues), list(positives), sep='\n')



# Sort Dictionary By Values
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}

print(sorted(prices.values()))                                                  # Only Values
print(sorted(prices, key = prices.get))                                         # Only Keys
print(sorted(prices.items(), key=lambda x: x[1], reverse=True))                 # Tuples(Key,Value)



# Multidictionary
d = {}
pairs =[(x,y) for x in range(10) for y in ('a','b','c','d','e','f')]
for key, value in pairs:
	if key not in d:
		d[key] = []
	d[key].append(value)

print(d)



# with (Context-Manager Protocol)
# sys.stdout.write/redirect_stdout
import contextlib
@contextlib.contextmanager
def looking_glass():
    # __enter__
    import sys
    original_write = sys.stdout.write
    def reverse_write(text):
        original_write(text[::-1])
    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    # __exit__
    sys.stdout.write = original_write

with looking_glass():
    print('hello')

print('hello')



# Generator with Yield
def aritprog_gen(begin, step, end=None):
	result = type(begin + step)(begin)
	forever = end is None
	index = 0
	while forever or result < end:
		yield result
		index += 1
		result = begin + step * index
		# index variable because:
		# 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 = 0.9999999999999999
		# 0.1 + 0.1*9 = 1.0

# def aritprog_gen(begin, step, end=None):
#     first = type(begin + step)(begin)
#     ap_gen = itertools.count(first, step)
#     if end is not None:
#         ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
#     return ap_gen

for i in aritprog_gen(3, 7, 100):
	print(i)



# Send to yield
def reciver():
	while True:
		item = yield
		print('Got: ', item)

fun = reciver()
next(fun)

fun.send('hello')
next(fun)
fun.send('hello again')

fun.close()



# yield from
def chain(x, y):
	yield from x
	yield from y

a = [1, 2, 3]
b = ['a', 'b', 'c']

for item in chain(chain(a, a), chain(b, b)):
	print(item)



# iter and __next__
def take(n, seq):
	"""Returns first n values from the given sequence."""
	seq = iter(seq)
	result = []
	try:
	  for i in range(n):
		  result.append(seq.__next__())
	except StopIteration:
		pass
	return result

print(take(7, [i for i in range(10)]))



# Normal version of grep
# def grep(pattern, filenames):
#     for f in filenames:
#         for line in open(f):
#             if pattern in line:
#                 print(line)

# Generator version
def readfiles(filenames):
	for f in filenames:
		for line in open(f):
			yield line

def grep(pattern, lines):
	return (line for line in lines if pattern in line)

def printlines(lines):
	for line in lines:
		print(line)

def main(pattern, filenames):
	lines = readfiles(filenames) # => generator
	lines = grep(pattern, lines) # => generator expresion
	printlines(lines)

main('grep', [__file__])



# Change a Sequence You Are Iterating Over While Inside The Loop
words = ['cat', 'window', 'defenestrate']
for w in words[:]:                                                              # Loop over a slice copy of the entire list
	if len(w) > 6:
		words.insert(0, w)

print(words)


# Bisection algorithms
# return the index where to insert item x in list a, assuming a is sorted
# bisect(a, x, lo=0, hi=len(a))
import bisect

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
	i = bisect.bisect(breakpoints, score)
	return grades[i]

print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])               # ['F', 'A', 'C', 'C', 'B', 'A', 'A']



# Memoryview
# memoryview objects allow python code to access the internal data of an object that supports the buffer protocol(bytes and bytearray) without copying
# they can be sliced without copying the underlying data, unlike bytes/str
import time
for n in (100000, 200000, 300000, 400000):
	data = b'x'*n
	start = time.time()
	# b = data
	b = memoryview(data)
	while b:
		b = b[1:]
	print('memoryview', n, time.time()-start)



# the disassembler function(wywołania instrukcji)
from dis import dis
dis('{1}')
# vs
dis('set([1])')



# Finding the largest or smallest N items
import random
import heapq
a = random.sample(range(1000001), 1000)
print(sorted(a, reverse=True)[:10])
print(heapq.nlargest(10,a))


portfolio = [
	{'name': 'IBM', 'shares': 100, 'price': 91.1},
	{'name': 'AAPL', 'shares': 50, 'price': 543.22},
	{'name': 'FB', 'shares': 200, 'price': 21.09},
	{'name': 'HPQ', 'shares': 35, 'price': 31.75},
	{'name': 'YHOO', 'shares': 45, 'price': 16.35},
	{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(sorted(portfolio, key = lambda s: s['price'], reverse = False)[:3])
print(heapq.nsmallest(3, portfolio, key=lambda s: s['price']))



# Pickle (object serialization, python objects converted into a byte stream)
# saving an array of floats with pickle.dump is almost as fast as with array.tofile,
# but pickle handles almost all built-in types
import pickle
li = [2, "Hello", 3.14, "..."]

# with file
with open("Example.data", mode="wb") as plik:
	pickle.dump(li, plik)

with open("Example.data", mode="rb") as plik:
	example = pickle.load(plik)

# without file
pickle.dumps(python_obj)
pickle.loads(pickled_obj)



# ZipFile Module
from zipfile import ZipFile
# We Don't Need To Use myzip.close()
with ZipFile('Zip.zip', 'w') as myzip:
	myzip.write(r'Example.data', 'Example')



# os.walk
import os
for root, dirs, files in os.walk(os.path.dirname(__file__)):
	for fname in filter(lambda fname: fname.endswith('.py'), files):
			document = open(os.path.join(root, fname), mode='rt', encoding='utf-8')



# tempfile, zipfile, os.walk
def zip_file(self, sample):
	path = ''
	try:
		with tempfile.SpooledTemporaryFile() as tmp:
			with zipfile.ZipFile(tmp, 'w') as zipf:
				for root, dirs, files in os.walk(path):
					for f in files:
						zipf.write(os.path.join(root, f),
								   os.path.join(sample.name, f),
								   zipfile.ZIP_DEFLATED)
			tmp.seek(0)
			response = HttpResponse(
				tmp.read(), mimetype='application/x-zip-compressed')
			content = 'attachment; filename={}.zip'.format(sample.name)
			response['Content-Disposition'] = content
			return response
	except:
		raise Http404()



# tarfile
import tarfile, os, glob
os.mkdir('Apps')
for i in glob.glob('D:/Science/And Whatnot Final/*'):
	t = tarfile.open(i)
	try:
		t.extractall('Apps')
	except:
		continue



# Xml
import urllib.request
from xml.etree.ElementTree import parse

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()

doc = parse('rt22.xml')
for bus in doc.findall('bus'):
	print(bus.findtext('d'))
	print(float(bus.findtext('lat')))



# Bytes and Bytearrays (an 8-bit word of data holds up to 256 values)
fin = open('C:/Python34/Scripts/utf8.txt', 'r', encoding='utf-8')
fout = open('C:/Python34/Scripts/utf8.html', 'w')
outbytes = bytearray()
for line in fin:
	for c in line:
		if(ord(c))>127:
			outbytes += bytes('&#{:04d};'.format(ord(c)), encoding='utf8')
		else:
			outbytes.append(ord(c))
outstr = str(outbytes, encoding='utf-8')
print(outstr, file = fout)
print(outstr)
print('Done.')



# Buforowanie wartości metody
class SomeModel(models.Model):
	def some_expensive_function(self):
		if not hasattr(self, "_expensive_value_cached"):
			# jakieś bardzo skomplikowane obliczenia...
			# ...i zapisanie wyniku w zmiennej result
			self._expensive_value_cached = result
		return self._expensive_value_cached

# In templates
# {% if object.some_expensive_function %}
#     <span class="special">{{ object.some_expensive_function }}</span>
# {% endif %}



# Sqlite3
import sqlite3
db = sqlite3.connect('test.db')
db.row_factory = sqlite3.Row                    # specify how rows will be returned from the cursor
db.execute('drop table if exists test')
db.execute('create table test (t1 text, i1 int)')
db.execute('insert into test (t1, i1) values (?, ?)', ('one', 1))
db.execute('insert into test (t1, i1) values (?, ?)', ('two', 2))
db.commit()

cursor = db.execute('select * from test order by t1')

for row in cursor:
	print(dict(row))                            # dict because of the row_factory
	print(row['t1'], row['i1'])



# Host and IP 
import socket
myname = socket.getfqdn(socket.gethostname( ))
myaddr = socket.gethostbyname(myname)
print("Host:", myname, "IP:", myaddr)



# Logging (rejestracja danych)
import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

logger = logging.getLogger('app.location')              # logging.getLogger(__name__)
logger.info('any message')



# Distributing modules
# the distutils package is used to help you distribute your python code
# the main function in distutils is setup()
# python setup.py --help

# setup.py
from distutils.core import setup

setup(
	name='',
	version='',
	py_modules=['module_name'],

	# metadata
	author='',
	author_email='',
	description='',
	license='',
	keywords='',
)

# install module
python setup.py install

# creating version(file) for distribution
# python setup.py sdist --help-formats
python setup.py sdist --format zip



# Handling Exception (try, except, else, finally, raise)
# raise without an argument re-raises the current exception
# NotImplementedError, LookupError(IndexError, KeyError), NameError, ImportError, ValueError, TypeError, IOError, SyntaxError
def readfile(filename):
	if filename.endswith('.txt'):
		fh = open(filename)
		return fh.readlines()
	else:
		raise ValueError('Filename must end with .txt')         # More informations about error


try:
	for line in readfile('xline.doc'):
		print(line.strip())
except IOError as e:
	print('Could not open the file', e)
except ValueError as e:
	print('Bad filename.', e)


while True:
	try:
		x = int(input("Please enter a number: "))
		break
	except ValueError:
		print("Oops!  That was no valid number.  Try again...")


try:  
	from lxml import etree
except ImportError:
	import xml.etree.ElementTree as etree
else:
	# The use of the else clause is better than adding additional code to the try
	# clause because it avoids accidentally catching an exception that wasn’t raised
	# by the code being protected by the try ... except statement.
finally:
	# A finally clause is always executed before leaving the try statement,
	# whether an exception has occurred or not.



# Assert
assert False, 'This should never happen'
assert isinstance(instance_of_the_class, ClassName), 'Comments'



# Documentation Strings
def square(x):
	'''Do nothing, but document it.
	No, really, it doesn't do anything.

	Args:
		x: The number for which the square root is to be computed

	Returns:
		The square root of x.

	Raises:
		ValueError: If x is negative.
	'''
	pass

print(function.__doc__)
