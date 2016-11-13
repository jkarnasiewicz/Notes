import random
the_world_is_flat = random.randrange(2)
if the_world_is_flat:
    print("Be careful not to fall off!\n")
else:
    print("You fell")



# Conditional execution, the first true value from if or elif ends the if statement
a = 11
if a > 12:
    print('a is greater than 12')
elif a > 10:
    print('a is greater than 10')
else:
    print('a is less or equal than 10')

# Conditional expresion/Conditional value
result = true_value if condition else false_value



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
for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
    print(n, 'is a prime number')



# Even Numbers(Liczby parzyste)
for num in range(1, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a odd number", num)



# Signum function
def sign(x):
  return (x > 0) - (x < 0)



# Reverse function
def reverse(iterable):
    for i in range(len(iterable)-1):
        iterable.insert(i, iterable.pop())
    return iterable

print(reverse([0, 1, 2, 3, 4, 5]))



# Fibonacci series, the sum of two elements defines the next, return Fibonacci series up to n
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print(fib2(100))



# Default Argument Values(domyslne argumenty)
def f(a, L = []):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3,L = []))



# Keyword Arguments
def zd(kto = 'Ona', co = 'lubi', kogo = 'jego'):
    print(kto, co, kogo)

zd()
zd('Jego', 'lubia', 'Oni')
zd('Paulina', kogo = 'Jacka')
zd(co = 'nie lubi', kogo = 'Jacka')



# Arbitrary Argument Lists(samowolny, arbitralny)
def shop(kind, *arguments, **keywords):
    print("Do you have any", kind, "?")
    print("I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

shop("Ice cream", "Nooo",":(", "!",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Shop Sketch")


def concat(*args, sep="/"):
   return print(sep.join(args))

concat("earth", "mars", "venus", "sun")
concat("earth", "mars", "venus", sep=".")



# Unpacking Argument Lists
args = [3, 6]
print(list(range(*args)))


def vol(voltage, who='you', action='vanish'):
    print("If you put", voltage, "volts through", who+",", who, "will", action+".")

d = {"voltage": 4000, "action": "fly"}
vol(**d)
vol(10)



# Lambda Expressions
def f(a,b,c):
    return lambda x: a*x**2 + b*x + c

g = f(1,2,3)
print(g(1))
print(g(2))


tri = [(1, 'one', 'jeden'), (2, 'two', 'dwa'), (3, 'three', 'trzy'), (4, 'four', 'cztery')]
tri.sort(key=lambda pair: pair[1])
print(tri)


# Comprehensions - short-hand syntaxfor creating collections and iterable objects
# List Comprehensions
print( [(x, y) for x in [-2,-1,0,1] for y in [1,2,3]    if x!=y] )
print( [[y * 3 for y in range(x)] for x in range(10)] )             # List of lists


vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])


print(len([n for n in list_of_numbers if n % 3 == 0]))                  # divisible_by_three
# Generator elementow
print(sum((1 for n in list_of_numbers if n % 3 == 0)))                  # divisible_by_three


from math import pi
print( [str(round(pi, i)) for i in range(1, 6)] )



# Transpose
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print( [[row[i] for row in matrix] for i in range(4)] )
print(list(zip(*matrix)))



# Set Comprehensions + Dictionaries
a = {x for x in 'abracadabra' if x not in 'abc'} # Set
print(a)

b = {x: x**2 for x in (2, 4, 6)} # Dictionary
print(b)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v, end=".\n")

c = {(i, v)for i, v in enumerate(['jack','jill','ivy'])}
print(sorted(c, key = lambda s: s[1]))

import os, glob
# Files Size In Current Working Directory
d = {f: os.stat(f).st_size for f in glob.glob('*')}
print(d)



# Dictionaries, Sets and Zip
prices = {
'ACME': 'asd',
'AAPL': '355',
'IBM': 'ACME',
'HPQ': 'iuy',
'FB': 'IBM'
}
print(min(zip(prices.values(), prices.keys())))
print(prices.keys() & prices.values())



# Map (returns lazy iterable object)
# map(f, sequence1, sequence2) is equivalent to [f(x1, x2) for x1, x2 in zip(sequence1, sequence2)]
f = map(ord, 'The quick brown fox')
s = list(map(lambda x, y: x*y , itertools.count(), range(10)))
a = map(lambda x, y: x**2 + y, [0, 1, 2, 3], [4, 5, 6, 7])
print(type(a))
print(a)



# Filter (returns lazy iterable object)
trues = filter(None, [0, 1, False, True, [], [1, 2, 3]])        # Remove elements which evaluate to False
positives = filter(lambda x: x%2 == 0, [-3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])      # Even numbers
print(list(trues), list(positives))



# Sort Dictionary By Values
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75}

print(sorted(prices.values()))                        # Only Values
print(sorted(prices, key = prices.get))               # Only Keys
print(sorted(prices.items(), key=lambda x: x[1]))     # Tuples(Key,Value)



# Multidictionary
d = {}
pairs =[(x,y) for x in range(10) for y in ('a','b','c','d','e','f')]
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
print(d)

from collections import defaultdict
d = defaultdict(list)
for key, value in pairs:
d[key].append(value)



# Enumerate + Yield
def enumeratee(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

print(tuple(enumeratee(range(20))))



# Own Iterator with Yield
def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1:
        raise TypeError('requires at least one argument')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError('inclusive_range expected at most 3 arguments,\
                         got {}'.format(numargs))
    i = start
    while i <= stop:
        yield i
        i += step

for i in inclusive_range(5, 25, 3):
    print(i, end=' ')



# Change a Sequence You Are Iterating Over While Inside The Loop
words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
print(words)



# Finding the largest or smallest N items
import random
import heapq
a = random.sample(range(1000001),1000)
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
print(heapq.nsmallest(3, portfolio, key=lambda s: s['price']))
print(sorted(portfolio, key = lambda s: s['price'], reverse = False)[:3])



# Handling Exception (try, except, raise)
# raise without an argument re-raises the current exception
# NotImplementedError, IndexError, NameError, KeyError, ImportError, ValueError, TypeError, IOError, SyntaxError
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



# Pickle (Python objects converted into a byte stream)
import pickle
li = [2, "Hello", 3.14, "..."]
with open("Example.data", mode = "wb") as plik:
    pickle.dump(li, plik)

with open("Example.data", mode = "rb") as plik:
    example = pickle.load(plik)



# ZipFile Module
from zipfile import ZipFile
# We Don't Need To Use myzip.close()
with ZipFile('Zip.zip', 'w') as myzip:
    myzip.write(r'C:\Users\Shades\Desktop\Sc2.txt', 'Sc2.txt')



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





# TO DO
# prime numbers
def is_prime(x):
    if x <2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x% i == 0:
            return False
    return True



# GENERATORS
# =====================

# Send to yield

def reciver():
    while True:
        item = yield
        print('Got: ', item)

fun = reciver()
print(fun, dir(fun))

next(fun)
print(fun, dir(fun))

fun.send('hello')
next(fun)
fun.send('hello again')

fun.close()

# =====================

def chain(x, y):
    yield from x
    yield from y

a = [1, 2, 3]
b = ['a', 'b', 'c']

# for item in chain(a, b):
for item in chain(chain(a, a), chain(b, b)):
    print(item)

# =====================

Context Manager Example
# Automatically deleted temp directories

import tempfile
import shutil

class TempDir:
    def __enter__(self):
        self.dirname = tempfile.mkdtemp()
        return self.dirname

    def __exit__(self, exc, val, tb):
        shutil.rmtree(self.dirname)

with TempDir() as dirname:
    ...


# Its the same code, glued together differently
import tempfile
import shutil
from contexlib import contextmanager

@contextmanager
def tempdir():
    dirname = tempfile.mkdtemp()
    try:
        yield dirname
    finally:
        shutil.rmtree(dirname)

# =====================

import time

class TimeIi:

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc, val, tb):
        self.end = time.time()
        print('Overall time: ', self.end - self.start)


with TimeIi():
    ...

# =====================

# Threads
from concurrent.futures import ThreadPoolExecutor
import time

# Creating 8 workers
pool = ThreadPoolExecutor(8)

def func(x, y):
    time.sleep(5)
    return x + y

def handle_result(future_obj):
    try:
        result = future_obj.result()
        print('Got: ', result)
    except Exception as e:
        print('Failed: {} {}'.format(type(e).__name__, e))

# future = pool.submit(func, 2, 3)
# blocking and waiting for result
# print(future.result())
# future.add_done_callback(handle_result)



pool.submit(func, 2, 3).add_done_callback(handle_result)
pool.submit(func, 20, 30).add_done_callback(handle_result)
pool.submit(func, 200, 'J').add_done_callback(handle_result)
pool.submit(func, 2000, 3000).add_done_callback(handle_result)

print('Normal execution:')
print(func(2, 3))
print(func(20, 30))
print(func(200, 300))
print(func(2000, 3000))

# =====================

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
#   print(dict(row))                            # dict because of the row_factory
#   print(row['t1'], row['i1'])




# IMPORT LOGGING
import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')


logger = logging.getLogger('app.location')
logger.info('any message')



# REST - representational state transfer
# Podejście REST sugeruje przygotowanie struktury adresu URL dopasowanej do struktury danych
# RESTful URLs are very useful for designing CRUD interfaces(Create, Read, Update, and Delete)

# API - Application Programming Interface

# Runing python with -O option, allow to run python without active assertions

math.copysign(1, y)
math.log10(abs(y))
