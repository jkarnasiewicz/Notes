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
# # Generator elementow
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
d = {f: os.stat(f).st_size for f in glob.glob('*')} # Files Size In Current Working Directory
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
s = list(map(lambda x, y: x*y , itertools.count(), range(10))))
a = map(lambda x, y: x**2 + y, [0, 1, 2, 3], [4, 5, 6, 7])
print(type(a))
print(a)



# Filter (returns lazy iterable object)
trues = filter(None, [0, 1, False, True, [], [1, 2, 3]])        # Remove elements which evaluate to False
positives = filter(lambda x: x%2 == 0, [-3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])      # Even numbers
print(list(trues), list(positives))



# Reduce - repeatedly apply a function to the elements of a sequence, reducing them to a single value
# reduce(function, sequence, initial value)
from functools import reduce
print(reduce(lambda x, y: x*y, range(10), 1))



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



# Itertools
from itertools import chain, product, permutations
sorted(chain(collection_1, collections_2), key=lambda instance: instance.name.lower())
print(list(product([1, 2], repeat=2)))
print(list(permutations([1, 2, 3, 4], 3)))



# Handling Exception (try, except, raise)
# NotImplementedError, IndexError, NameError, KeyError, ImportError, ValueError, IOError, SyntaxError
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



# ZipFile Module
from zipfile import ZipFile
with ZipFile('Zip.zip', 'w') as myzip:                              # We Don't Need To Use myzip.close()
    myzip.write(r'C:\Users\Shades\Desktop\Sc2.txt', 'Sc2.txt')



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
def function(inst):
    """Do nothing, but document it.
    No, really, it doesn't do anything.

    :param inst: an instance of :class: ClassName
    """
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
