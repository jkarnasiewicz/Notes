# Iterables, Iterators, Generators and Coroutines

# Iterables
# ===================================
# Any object from which the iter built-in function can obtain an iterator

# Whenever the interpreter needs to iterate over an object x, it automatically calls iter(x)
# The iter built-in function:
# 1. Checks whether the object implements, __iter__, and calls that to obtain an iterator
# 2. If __iter__ is not implemented, but __getitem__ is implemented, python creates
# an iterator that attempts to fetch items in order, starting from index 0 (zero);
# 3. If that fails, python raises TypeError, usually saying "'C' object is not iterable",
# where C is the class of the target object


# Iterable protocol
# __iter__ and __getitem__
# __iter__ method is called on initialization of an iterator, this should return an object that has a __next__ method

# Unpacking
# __iter__ or __getitem makes a object iterable; this is what makes unpacking work, e.g, x, y = my_object

    def __getitem__(self, index):
        return self.sequence[index]

# Iterables are objects over which we can iterate item by item (lists, dict, strings or files)
# there are many functions which consume these iterables, e.g. join, list

# Iterable objects can be passed to the built-in iter() function to get an iterator
# iterator = iter(iterable)

    def __iter__(self):
        return (item for item in self._items)

# other use of iter
# iterator = iter(callable, sentinel) - callable without arguments
# sentinel is a marker value which, when returned by the callable, causes
# the iterator to raise StopIteration instead of yielding the sentinel

with open('some_file.txt', 'rt') as f:
    for line in iter(lambda: f.readline().split(), 'END'):
    # for line in iter(f.readline, ''):
        print(line)





# Iterators
# ===================================

# Iterator protocol
# __iter__ and __next__ with raise StopIteration() when there are no more items

# we retrive an iterator from an iterable object using the built-in iter() function
# iterators produce items one-by-one from the underlying iterable series each time
# they are passed to the built-in next() function

# Iterator objects can be passed to build-in next() function to fetch the next item
# item = next(iterator)

class Sensor:

    def __iter__(self):
        # iterators should return self
        return self

    def __next__(self):
        return random.random()

sensor = Sensor()
timstamps = iter(datetime.datetime.now, None)

for stamp, value in itertools.islice(zip(timstamps, sensor), 10):
    print(stamp, value)
    time.sleep(3)



class Reverse:

    def __init__(self, sequence):
        self.sequence = sequence
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.sequence[self.index]
            self.index -= 1
        except IndexError:
            self.index = -1
            raise StopIteration
        return result

for i in Reverse([1, 3, 5, 7]):
    print(i)



# optimization in any/all
def gen():
    for i in [0, '1', 3, None, 'Ace']:
        yield i

g = gen()                                   # or just g = (n for n in [0, 0.0, 7, 8])
print(any(g))
print(next(g))

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

# A generator doesn’t 'return' values in the usual way: the return statement in the body
# of a generator function causes StopIteration to be raised by the generator object

# When a generator function is called, it returns a generator object without
# even beginning execution of the function. When next method is called for the first time,
# the function starts executing until it reaches yield statement
# The yielded value is returned by the next call

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










# Examples

# classic Iterator pattern
# ========================================================
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

s = Sentence('2323d 23f23fd 23d23d')
# print([i for i in s])
it = iter(s)
# print([i for i in s])
print(it)


# Iterator with yield
# ========================================================
class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        print('ITER')
        for word in self.words:
            yield word


s = Sentence('2323d 23f23fd 23d23d')
print([i for i in s])
it = iter(s)
print([i for i in s])
print(it)


# Iterator with generator function or generator expression
# ========================================================
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










# Coroutines
# ========================================================
# Like .__next__(), .send() causes the generator to advance to the next yield, but it
# also allows the client using the generator to send data into it: whatever argument is
# passed to .send() becomes the value of the corresponding yield expression inside the
# generator function body. In other words, .send() allows two-way data exchange between
# the client code and the generator — in contrast with .__next__() which only lets
# the client receive data from the generator

# This is such a major 'enhancement' that it actually changes the nature of generators:
# when used in this way, they become coroutines

# That’s the big advantage of having coroutines: functions that can be suspended and resumed
