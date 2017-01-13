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
		for word in self.words:
			yield word


s = Sentence("At Wit's End")
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
# A coroutine is syntactically like a generator: just a function with the yield keyword in
# its body. However, in a coroutine, yield usually appears on the right side of an expression,
# e.g. data = yield, and it may or may not produce a value — if there is no expression
# after the yield keyword, the generator yields None. The coroutine may receive
# data from the caller, which uses .send(data) instead of next(...) to feed the coroutine.
# Usually, the caller pushes values into the coroutine

# Like .__next__(), .send() causes the generator to advance to the next yield, but it
# also allows the client using the generator to send data into it: whatever argument is
# passed to .send() becomes the value of the corresponding yield expression inside the
# generator function body. In other words, .send() allows two-way data exchange between
# the client code and the generator — in contrast with .__next__() which only lets
# the client receive data from the generator

# This is such a major 'enhancement' that it actually changes the nature of generators:
# when used in this way, they become coroutines

# Informal definition of a coroutine:
# a generator function driven by a client sending it data through .send(...) calls or yield from

# The big advantage of having coroutines/generators -> functions that can be suspended and resumed

def simple_coro(a):
	print('-> Started: a =', a)
	b = yield a
	print('-> Received: b =', b)
	c = yield a + b
	print('-> Received: c =', c)
	print(a, b, c)
	return 'msg'

my_coro2 = simple_coro(14)
print(next(my_coro2))
print(my_coro2.send(28))
my_coro2.send(99)



# coroutine decorator(initialization next() is unnecessary)
from functools import wraps
def coroutine(func):
	"""Decorator: primes `func` by advancing to first `yield`"""
	@wraps(func)
	def primer(*args,**kwargs):
		gen = func(*args,**kwargs)
		next(gen)
		return gen
	return primer



# generator.throw(exc_type[, exc_value[, traceback]])
# Causes the yield expression where the generator was paused to raise the exception
# given. If the exception is handled by the generator, flow advances to the next
# yield, and the value yielded becomes the value of the generator.throw call. If the
# exception is not handled by the generator, it propagates to the context of the caller

# throw exception
class DemoException(Exception):
	"""An exception type for the demonstration."""

def demo_finally():
	print('-> coroutine started')
	try:
		while True:
			try:
				x = yield
			except DemoException:
				print('*** DemoException handled. Continuing...')
			else:
				print('-> coroutine received: {!r}'.format(x))
	finally:
		print('-> coroutine ending')

co = demo_finally()
next(co)
co.send(22)
co.send(47)
co.throw(DemoException)
co.send(7)



# return value from coroutine
from collections import namedtuple
Result = namedtuple('Result', 'count average')

def averager():
	total = 0.0
	count = 0
	average = None
	while True:
		term = yield
		if term is None:
			break
		total += term
		count += 1
		average = total/count
	return Result(count, average)

coro_avg = averager()
next(coro_avg)
coro_avg.send(10)
coro_avg.send(30)
coro_avg.send(6.5)
try:
	coro_avg.send(None)
except StopIteration as exc:
	result = exc.value

print(result)



# generator.close()
# Causes the yield expression where the generator was paused to raise a Generator
# Exit exception. No error is reported to the caller if the generator does not handle
# that exception or raises StopIteration — usually by running to completion. When
# receiving a GeneratorExit the generator must not yield a value, otherwise a Run
# timeError is raised. If any other exception is raised by the generator, it propagates
# to the caller.










# Yield From
# ========================================================
# The first thing to know about yield from is that it is a completely new language construct.
# It does so much more than yield that the reuse of that keyword is arguably misleading

# Similar constructs in other languages are called await and that is a much better name
# because it conveys a crucial point: when a generator gen calls yield from subgen(), the
# subgen takes over and will yield values to the caller of gen; the caller will in effect
# drive subgen directly. Meanwhile gen will be blocked, waiting until subgen terminantes

# * The main feature of yield from is to open a bidirectional channel from the outermost
# caller to the innermost subgenerator, so that values can be sent and yielded back and
# forth directly from them, and exceptions can be thrown all the way in without adding
# a lot of exception handling boilerplate code in the intermediate coroutines. This is
# what enables coroutine delegation in a way that was not possible before

# * In the case of yield from, the interpreter not only consumes the StopIteration,
# but its value attribute becomes the value of the yield from expression itself

# One of the main reasons why the yield from construct was added to Python 3.3 has to
# do with throwing exceptions into nested coroutines. The other reason was to enable
# coroutines to return values more conveniently

# The first thing the yield from x expression does with the x object is to call iter(x) to
# obtain an iterator from it. This means that x can be any iterable

# Since the delegating generator works as a pipe, you can connect any number of them in a
# pipeline: one delegating generator uses yield from to call a subgenerator, which itself
# is a delegating generator calling another subgenerator with yield from and so on.
# Eventually this chain must end in a simple generator that uses just yield, but it may
# also end in any iterable object

# Generators can be used as an alternative to threads and callbacks to support concurrency
# Event-driven frameworks like Tornado and asyncio use a main loop to drive coroutines
# executing concurrent activities with a single thread of execution

# Three main components of any significant use of yield from:
# the delegating generator (defined by the use of yield from in its body), the
# subgenerator activated by yield from and the client code that actually drives the
# whole setup by sending values to the subgenerator through the pass-through channel
# established by yield from in the delegating generator



# Example of flattening a nested sequence using subgenerators
from collections.abc import Iterable

def flatten(items, ignore_types=(str, bytes)):
	for x in items:
		if isinstance(x, Iterable) and not isinstance(x, ignore_types):
			yield from flatten(x)
		else:
			yield x


nubers = [1, 2, [3, 4, [5, 6], 7], 8]
# Produces 1 2 3 4 5 6 7 8
for x in flatten(nubers):
	print(x)

names = ['Dave', 'Paula', ['Thomas', 'Lewis']]
# Produces Dave Paula Thomas Lewis
for x in flatten(names):
	print(x)










# Concurrency(threads and processes) and Asynchronous(coroutines and callbacks)
# =============================================================================
# Modern CPUs with GHz clocks run billions of cycles per second. Let’s say that a CPU runs
# exactly 1 billion cycles per second. That CPU can make 333,333,333 L1 cache reads in one
# second, or 4 (four!) network reads in the same time

# Blocking I/O and the GIL
# The CPython interpreter is not thread-safe internally, so it has a Global Interpreter Lock
# (GIL) which allows only one thread at a time to execute Python bytecodes. That’s why
# a single Python process usually cannot use multiple CPU cores at the same time.
# When we write Python code we have no control over the GIL, but a built-in function
# or an extension written in C can release the GIL while running time consuming tasks.
# In fact, a Python library coded in C can manage the GIL, launch its own OS threads and
# take advantage of all available CPU cores. This complicates the code of the library
# considerably, and most library authors don’t do it

# Every blocking I/O function in the Python standard library releases the GIL, allowing
# other threads to run. The time.sleep() function also releases the GIL. Therefore, Python
# threads are perfectly usable in I/O bound applications, despite the GIL

# Launching processes with concurrent.futures
# The documentation page for the concurrent.futures package is subtitled 'Launching
# parallel tasks'. The package does enable truly parallel computations because it supports
# distributing work among multiple Python processes using the ProcessPoolExecutor
# class — thus bypassing the GIL and leveraging all available CPU cores, if you need to
# do CPU-bound processing

# Launching threads with concurrent.futures
# Python threads are well suited for I/O intensive and bound applications, despite the
# GIL: every standard library I/O function written in C releases the GIL, so while a given
# thread is waiting for I/O, the Python scheduler can switch to another thread

# highest level of abstraction
# 	=> concurrent.futures.ThreadPoolExecutor/ProcessPoolExecutor modules
# lower level of abstraction(build own solution out of basic components(more flexible)
# 	=> threading and multiprocessing modules



# Concurrency with futures
from concurrent import futures
import time

# Creating 8 workers
pool = futures.ThreadPoolExecutor(8)				# ProcessPoolExecutor(os.cpu_count())

def func(x, y):
	time.sleep(5)
	return x + y

def handle_result(future_obj):
	try:
		result = future_obj.result()
		print('Got: ', result)
	except Exception as e:
		print('Failed: {} {}'.format(type(e).__name__, e))

# sequential execution
print(func(2, 3))
print(func(20, 30))
print(func(200, 300))
print(func(2000, 3000))



# submit and add_done_callback
for i in range(4):
	pool.submit(func, 2*10**i, 3*10**i).add_done_callback(handle_result)



# submit and as_completed
# create list with futures
to_do = []
for i in range(4):
	# submit schedules the callable to be executed, and returns a future representing this pending operation
	future = pool.submit(func, 2*10**i, 3*10**i)
	to_do.append(future)

result = []
# as_completed yields futures as they are completed
for future in futures.as_completed(to_do):
	res = future.result()
	result.append(res)

print(result)



# map
with futures.ThreadPoolExecutor(8) as executor:
	# create generator
	res = executor.map(func, [2, 20, 200, 2000], [3, 30, 300, 3000])
	print(list(res))

# map vs submit/as_completed
# The executor.map function is easy to use but it has a feature that may or may not be
# helpful, depending on your needs: it returns the results exactly in the same order as the
# calls are started: if the first call takes 10s to produce a result, and the others take 1s each,
# your code will block for 10s as it tries to retrieve the first result of the generator returned
# by map. After that, you’ll get the remaining results without blocking because they will be done.
# That’s ok when you must have all the results before proceeding, but often it’s preferable to get
# the results as they are ready, regardless of the order they were submitted. To do that, you need
# a combination of the executor.submit method and the futures.as_completed function




# To keep a program alive despite the inevitable blocking functions there are two solutions:
# using threads or asynchronous calls — the latter being implemented as callbacks or coroutines
# Coroutines solve the main problems of callbacks: loss of context when carrying out multi-step
# asynchronous tasks, and lack of a proper context for error handling

# Threads versus Coroutines
# if you’ve done any non-trivial programming with threads, you know how challenging it is to
# reason about the program because the scheduler can interrupt a thread at any time. You must
# remember to hold locks to protect the critical sections of your program, to avoid getting
# interrupted in the middle of a multi-step operation — which could leave data in an invalid
# state. With coroutines, everything is protected against interruption by default. You must
# explicitly yield to let the rest of the program run. Instead of holding locks to synchronize
# the operations of multiple threads, you have coroutines that are 'synchronized' by definition:
# only one of them is running at any time. And when you want to give up control, you use yield
# or yield from to give control back to the scheduler. That’s why it is possible to safely
# cancel a coroutine: by definition, a coroutine can only be cancelled when it’s suspended at a
# yield point, so you can perform cleanup by handling the CancelledError exception

# You don’t need my_future.add_done_callback(...) because you can simply put whatever
# processing you would do after the future is done in the lines that follow yield
# from my_future in your coroutine. That’s the big advantage of having coroutines:
# functions that can be suspended and resumed



# Spinner with threading
import itertools, sys, threading, time

class Signal:
	go = True


def spin(msg, signal):
	write, flush = sys.stdout.write, sys.stdout.flush
	for char in itertools.cycle('|/-\\'):
		status = char + ' ' + msg
		write(status)
		flush()
		# The trick to do text-mode animation: move the cursor back with backspace characters (\x08)
		write('\x08' * len(status))
		time.sleep(.1)
		if not signal.go:
			break
	write(' ' * len(status) + '\x08' * len(status))


def slow_function():
	# pretend waiting a long time for I/O
	time.sleep(3)
	return 42


def supervisor():
	signal = Signal()
	spinner = threading.Thread(target=spin, args=('thinking!', signal))
	print('spinner object:', spinner)
	spinner.start()
	result = slow_function()
	signal.go = False
	spinner.join()
	return result


def main():
	result = supervisor()
	print('Answer:', result)

if __name__ == '__main__':
	main()



# Spinner with asyncio/coroutines
import asyncio, itertools, sys

@asyncio.coroutine
def spin(msg):
	write, flush = sys.stdout.write, sys.stdout.flush
	for char in itertools.cycle('|/-\\'):
		status = char + ' ' + msg
		write(status)
		flush()
		write('\x08' * len(status))
		try:
			yield from asyncio.sleep(.1)
		except asyncio.CancelledError:
			break
	write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_function():
	# pretend waiting a long time for I/O
	yield from asyncio.sleep(3)
	return 42


@asyncio.coroutine
def supervisor():
	spinner = asyncio.async(spin('thinking!'))
	print('spinner object:', spinner)
	result = yield from slow_function()
	spinner.cancel()
	return result


def main():
	loop = asyncio.get_event_loop()
	result = loop.run_until_complete(supervisor())
	loop.close()
	print('Answer:', result)


if __name__ == '__main__':
	main()










# Asyncio
# =============================================================================

# Asyncio uses a stricter definition of 'coroutine'. A coroutine suitable for use with the
# asyncio API must use yield from and not yield in its body. Also, an asyncio coroutine should
# be driven by a caller invoking it through yield from or by passing the coroutine to one of the
# asyncio functions such as asyncio.async(...)

# Using yield from with a future automatically takes care of waiting for it to finish, without blocking
# the event loop — because in asyncio, yield from is used to give control back to the event loop
