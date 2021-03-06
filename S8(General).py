# REST - Representational State Transfer
Podejście REST sugeruje przygotowanie struktury adresu URL dopasowanej do struktury danych
RESTful URLs are very useful for designing CRUD interfaces(Create, Read, Update, and Delete)

# API - Application Programming Interface
An API is a defined interface that acts like a handshake between software components,
allowing one component to access another even though the components have been
developed separately.

# ORM - Object-Relational Mapping

# CDN - Content Distribution Network

# KISS - KISS principle is an acronym for "Keep it simple, stupid"

# FUBAR - fucked up beyond all recognition

# XML - Extensible Markup Language

# SVG - Scalable Vector Graphics

# Blob - Binary Large Object

# PID - Process IDentifier

# NPM - Node Package Manager

# SSL - Secure Socket Layer

# CORS - Cross-Origin Resource Sharing

# BIT - Binary Digit(0 or 1)

# EAFP
Easier to ask for forgiveness than permission. This common Python coding style assumes the
existence of valid keys or attributes and catches exceptions if the assumption proves false.
This clean and fast style is characterized by the presence of many try and except statements.
The technique contrasts with the LBYL style common to many other languages such as C

# LBYL
Look before you leap. This coding style explicitly tests for pre-conditions before
making calls or lookups. This style contrasts with the EAFP approach and is characterized
by the presence of many if statements. In a multi-threaded environment,
the LBYL approach can risk introducing a race condition between 'the looking' and
'the leaping'. For example, the code, if key in mapping: return mapping[key] can
fail if another thread removes key from mapping after the test, but before the lookup.
This issue can be solved with locks or by using the EAFP approach

# Uniform Access Principle
(or a variation of it) is the fact that function calls and object instantiation use the
same syntax in Python: my_obj = foo(), where foo may be a class or any other callable

# DES - discrete event simulation
Intuitively, turn-based games are examples of discrete event simulations: the state of the
game only changes when a player moves, and while a player is deciding the next move,
the simulation clock is frozen. Real time games, on the other hand, are continuous
simulations where the simulation clock is running all the time, the state of the game is
updated many times per second and slow players are at a real disadvantage

# REDIS
Redis is in-memory data structure store, used as a database, cache and message broker

# Algorytm deterministyczny
Algorytm, którego działanie jest całkowicie zdeterminowane przez warunki początkowe (wejście).
Oznacza to, że kilkukrotne uruchomienie takiego algorytmu doprowadzi za każdym razem do
takiego samego wyniku. Algorytmy deterministyczne stanowią główny obszar badań informatycznych
i są najczęściej stosowane, ponieważ mogą być łatwo realizowane na współczesnych komputerach

# Hexadecimal numbers(0123456789abcdef)

















# PYTHON/LANGUAGE

# Is Python interpreted or compiled?
In the case of CPython, the answer really is 'sort of both'. Specifically, with CPython, code
is first compiled and then interpreted. More precisely, it is not precompiled to native machine
code, but rather to bytecode. While machine code is certainly faster, bytecode is more portable
and secure. The bytecode is then interpreted in the case of CPython (or both interpreted and
compiled to optimized machine code at runtime in the case of PyPy).

# How does Python handle the memory management?
Python uses private heaps to maintain its memory. So the heap holds all the Python objects and
the data structures. This area is only accessible to the Python interpreter, programmers can’t
use it. And it’s the Python memory manager that handles the Private heap. It does the required
allocation of the heap for Python objects. Python employs a built-in garbage collector, which
salvages all the unused memory and offloads it to the heap space.

# Unittest
unittest supports test automation, sharing of setup and shutdown code for tests, aggregation of
tests into collections, and independence of the tests from the reporting framework. The unittest
module provides classes that make it easy to support these qualities for a set of tests.
Key elements of the unittest framework: test fixtures, test cases, test suites, test runners
and mocks(mock allows you to replace parts of your system under test with mock objects and make
assertions about how they are to be used. Keeping as much 'slow code' as possible out of the
automated test runs, namely filesystem and network access

# Protocols and duck typing
In the context of Object Oriented Programming, a protocol is an informal interface,
defined only in documentation and not in code. For example, the sequence protocol in
python entails just the __len__ and __getitem__ methods. Any class Spam that implements
those methods with the standard signature and semantics can be used anywhere
a sequence is expected. Whether Spam is a subclass of this or that is irrelevant, all that
matters is that it provides the necessary methods

We say it is a sequence because it behaves like one, and that is what matters

# Interface
interface is: the subset of an object’s public methods that enable it to play a specific
role in the system. That’s what is implied when the python documentation mentions
'a file-like object' or 'an iterable', without specifying a class

# Protocol
protocols are interfaces, but because they are informal — defined only by documentation
and conventions — protocols cannot be enforced like formal interfaces can. A protocol may be
partially implemented in a particular class, and that’s OK

# Duck typing
this can be accomplished without inheritance, in the spirit of
duck typing: you just implement the methods needed for your objects to behave as
expected
# or
operating with objects regardless, of their types, as long as they implement certain protocols



# Functional programming
is a way of abstracting out the complexity of an application, replacing complicated loops and
conditional statements with nice, clean function calls

# Imperative programing
approach using conditionals, loops, and associated procedures



# Special methods
the Python interpreter is the only frequent caller of most special methods



# with blocks
The with statement was designed to simplify the try/finally pattern which guarantees
that some operation is performed after a block of code, even if the block is aborted
because of an exception, a return or sys.exit() call. The code in the finally clause
usually releases a critical resource or restores some previous state that was temporarily
changed

with blocks don’t define a new scope, as functions and modules do

with is not just for resource management, but it’s a tool for factoring out common
setup and tear down code, or any pair of operations that need to be done before and
after another procedure



# Unsigned/Signed
unsigned integers can hold a larger positive value, and no negative value
signed integers can hold both positive and negative numbers



# Container sequences
list, tuple, dict, set and collections.deque can hold items of different types
# Flat sequences
str, bytes, bytearray, memoryview and array.array hold items of one type

Container sequences hold references to the objects they contain, which may be of any
type, while flat sequences physically store the value of each item within its own memory
space, and not as distinct objects. Thus, flat sequences are more compact, but they are
limited to holding primitive values like characters, bytes and numbers



# Dictionaries
1: Keys must be hashable objects
	An object is hashable if all of these requirements are met:
	1. It supports the hash() function via a __hash__() method that always returns the
	same value over the lifetime of the object.
	2. It supports equality via an __eq__() method.
	3. If a == b is True then hash(a) == hash(b) must also be True.

2: dicts have significant memory overhead
3: Key search is very fast(example of trading space for time)
4: Key ordering depends on insertion order
5: Adding items to a dict may change the order of existing keys



# Normalizing Unicode text
from unicodedata import normalize, name
def nfc_equal(str1, str2):
	return normalize('NFC', str1) == normalize('NFC', str2)

def fold_equal(str1, str2):
	return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold())

# Sorting Unicode text
Python sorts sequences of any type by comparing the items in each sequence one by
one. For strings, this means comparing the code points. Unfortunately, this produces
unacceptable results for anyone who uses non-ASCII characters

# Sorting with the Unicode Collation Algorithm
import pyuca
coll = pyuca.Collator()
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=coll.sort_key)



# Identity and value
With reference variables it makes much more sense to say that the variable is assigned to an object, and not the
other way around. After all, the object is created before the assignment. right-hand side of an assignment happens first
variables just hold references to object

Every object has an identity, a type and a value. An object’s identity never changes once
it has been created; you may think of it as the object’s address in memory. The 'is' operator
compares the identity of two objects; the id() function returns an integer representing
its identity.

The == operator compares the values of objects (the data they hold), while 'is' compares
their identities

The is operator is faster than ==, because it cannot be overloaded, so Python does not
have to find and invoke special methods to evaluate it, and computing is as simple as
comparing two integer ids



# Default values
The problem is that each default value is evaluated
when the function is defined — i.e. usually when the module is loaded — and the
default values become attributes of the function object



# Reference assigment, copy and deepcopy
	a = b: Reference assignment, a and b points to the same object

	a ---,
		 v
		 {1: L}
		 ^   |
	b ---'   '----> [1,2,3]

	a = b.copy(): Shallow copying, a and b will become two isolated objects, but their contents still share the same reference

	a ---> {1: L}
			   |
			   >---> [1,2,3]
			   |
	b ---> {1: M}

	a = copy.deepcopy(b): Deep copying, a and bs structure and content become completely isolated

	a ---> {1: L}
			   ‘-----> [1,2,3]
	b ---> {1: M}
			   ‘-----> [1,2,3]

# Make a copy
Unless a method is explicitly intended to mutate an object received
as argument, you should think twice before aliasing the argument
object by simply assigning it to an instance variable in your class. If
in doubt, make a copy



# References
The fact that variables hold references has many practical consequences in Python programming
1. Simple assignment does not create copies
2. Augmented assignment with +=, *= creates new objects if the left-hand variable is
bound to an immutable object, but may modify a mutable object in-place
3. Assigning a new value to an existing variable does not change the object previously
bound to it. This is called a rebinding: the variable is now bound to a different object.
If that variable was the last reference to the previous object, that object will be
garbage collected
4. Function parameters are passed as aliases, which means the function may change
any mutable object received as an argument. There is no way to prevent this, except
making local copies or using immutable objects (eg. passing a tuple instead of a
list)
5. Using mutable objects as default values for function parameters is dangerous because
if the parameters are changed in-place then the default is changed, affecting
every future call that relies on the default



# Private attribute
if you name an instance attribute in the form __mood (two leading
underscores and zero or at most one trailing underscore), Python stores the name in
the instance __dict__ prefixed with a leading underscore and the class name, so in the
Dog class, __mood becomes _Dog__mood



# NotImplemented vs NotImplementedError
Do not confuse NotImplemented with NotImplementedError. The first, NotImplemented is a special
singleton value that an infix operator special method should return to tell the interpreter it
cannot handle a given operand. In contrast, NotImplementedError is an exception that stub
methods in abstract classes raise to warn that they must be overwritten by subclasses

If an infix operator method raises an exception, it aborts the operator dispatch algorithm.
In the particular case of TypeError, it is often better to catch it and return NotImplemented.
This allows the interpreter to try calling the reversed operator method which may correctly handle
the computation with the swapped operands, if they are of different types



















# Network

# WebSockets
WebSockets is an advanced technology that makes it possible to open an interactive
communication session between the users browser and a server. With this API, you can
send messages to a server and receive event-driven responses without having to poll
the server for a reply

# WebSockets 101 and HTTP
Normally, Django uses HTTP to communicate between the client and server:
The client sends an HTTP request to the server.
Django parses the request, extracts a URL, and then matches it to a view.
The view processes the request and returns an HTTP response to the client.

Unlike HTTP, the WebSockets protocol allows bi-directional communication,
meaning that the server can push data to the client without being prompted by the user.
With HTTP, only the client that made a request receives a response. With WebSockets,
the server can communicate with multiple clients simultaneously.
We send WebSockets messages using the ws:// prefix, as opposed to http://.



# The layers operating below the socket() API are two different protocols(UDP and TCP)

# TCP
The Transmission Control Protocol supports two-way conversations made of streams of
bytes by sending (or perhaps re-sending), receiving, and re-ordering small network messages
called packets.

# UDP

# IP
The Internet Protocol knows how to send packets between different computers.
The Internet Protocol is a scheme for imposing a uniform system of addresses on all of the Internet-connected
computers in the entire world and to make it possible for packets to travel from one end of the Internet to the other

# Link layer
The 'link layer' at the very bottom, consists of network hardware devices such as Ethernet
ports and wireless cards, which can send physical messages between directly linked
computers.



# Decoding
Decoding is what happens when bytes are on their way into your application and you need to figure out what they
mean.

# Translating from the outside world of bytes to Unicode characters.
input_bytes = b'\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00'
input_characters = input_bytes.decode('utf-16')
print(repr(input_characters))



# Encoding
Encoding is the process of taking character strings that you are ready to present to the outside world and turning
them into bytes using one of the many encodings that digital computers use when they need to transmit or store
symbols using the bytes that are their only real currency

# Translating characters back into bytes before sending them.
output_characters = 'We copy you down, Eagle.\n'
output_bytes = output_characters.encode('utf-8')
print(repr(output_bytes))





# Simple Python server
python -m http.server 9000

# DNS - Domain Name System

# Protocol(protokół) e.g. Http, Https



# Status code:
# 2XX Success
200 Ok
201 Created

# 3XX Redirection
301 Moved Permanently (Trwale przeniesiony – żądany zasób zmienił swój URI i w przyszłości zasób powinien być szukany pod wskazanym nowym adresem)
302 Found (Znaleziono – żądany zasób jest chwilowo dostępny pod innym adresem a przyszłe odwołania do zasobu powinny być kierowane pod adres pierwotny)
304 Not Modified

# 4XX Client Error
400 Bad Request (Nieprawidłowe zapytanie – żądanie nie może być obsłużone przez serwer z powodu błędnej składni zapytania)
403 Forbidden (Zabroniony – serwer zrozumiał zapytanie lecz konfiguracja bezpieczeństwa zabrania mu zwrócić żądany zasób)
404 Not Found

# 5XX Server Error
500 Internal Server Error
503 Service Unavailable
























# PYTHON 2 VS PYTHON 3
difference in the way Python 3 treats strings.
In Python 2, the human-readable representation of a class can be returned by
__str__() (bytes) or __unicode__() (text). However, in Python 3 the readable
representation is simply returned by __str__() (text).



All classes inherit from the object class
Python 2 has two kinds of classes: old-style (classic) and new-style. New-style classes
are classes that directly or indirectly inherit from object. Only the new-style classes
can use Pythons advanced features, such as slots, descriptors, and properties. Many
of these are used by Django. However, classes were still old-style by default for
compatibility reasons.
In Python 3, the old-style classes dont exist anymore. As seen in the following table,
even if you dont explicitly mention any parent classes, the object class will be
present as a base. So, all the classes are new-style.



Calling super() is easier



Relative imports must be explicit
no  "import models"
yes "from . import models"



HttpRequest and HttpResponse have str and bytes types
Essentially, for the HttpRequest and HttpResponse objects:
- Headers will always be the str objects
- Input and output streams will always be the byte objects



Exception syntax changes and improvements
In Python 3, you cannot use the comma-separated syntax for the except clause.
Use the as keyword instead
In Python 3, all the exceptions must be derived (directly or indirectly) from
BaseException. In practice, you would create your custom exceptions by deriving
from the Exception class
As a major improvement in error reporting, if an exception occurs while handling an
exception, then the entire chain of exceptions are reported



Standard library reorganized and new features
asyncio: This contains asynchronous I/O, event loop, coroutines, and tasks
unittest.mock: This contains the mock object library for testing
pathlib: This contains object-oriented file system paths
statistics: This contains mathematical statistics functions



Using Pyvenv and Pip
python -m venv djenv
...
pip install django



1. print() is now a function: Previously, it was a statement, that is, arguments
were not in parenthesis.
2. Integers dont overflow: sys.maxint is outdated, integers will have
unlimited precision.
3. Inequality operator <> is removed: Use != instead.
4. True integer division: In Python 2, 3 / 2 would evaluate to 1. It will be
correctly evaluated to 1.5 in Python 3.
5. Use range instead of xrange(): range() will now return iterators as
xrange() used to work before.
6. Dictionary keys are views: dict and dict-like classes (such as QueryDict)
will return iterators instead of lists for the keys(), items(), and values()
method calls
7. The ordering comparison operators (<, <=, >=, >) now raise a TypeError
exception when the operands don’t have a meaningful natural ordering
e.g. None < None now raises a TypeError
8. nonlocal doesnt exist in python 2

























# SECURITY

# Hashing(MD5, SHA-0, SHA-1 and SHA-2)
A hash is a string or number generated from a string of text. The resulting string or
number is a fixed length, and will vary widely with small variations in input. The best
hashing algorithms are designed so that its impossible to turn a hash back into its
original string.
Hashing is great for usage in any instance where you want to compare a value with a
stored value, but cant store its plain representation for security reasons

# Encrypting(AES, PGP)
Encryption turns data into a series of unreadable characters, that arent of a fixed
length. The key difference between encryption and hashing is that encrypted strings
can be reversed back into their original decrypted form if you have the right key

There are two primary types of encryption, symmetric key encryption and public key
encryption. In symmetric key encryption, the key to both encrypt and decrypt is exactly
the same. Public key encryption by comparison has two different keys, one used to encrypt
the string (the public key) and one used to decrypt it (the private key). The public key
is is made available for anyone to use to encrypt messages, however only the intended
recipient has access to the private key, and therefore the ability to decrypt messages



# Cross-site scripting (XSS)
considered the most prevalent web application security flaw today,
enables an attacker to execute his malicious scripts (usually JavaScript)
on web pages viewed by users



# Cross-Site Request Forgery (CSRF)
is an attack that tricks a user into making
unwanted actions on a website, where they are already authenticated, while they
are visiting another site. Say, in a forum, an attacker can place an IMG or IFRAME tag
within the page that makes a carefully crafted request to the authenticated site.



# SQL injection
is the second most common vulnerability of web applications,
after XSS. The attack involves entering malicious SQL code into a query that
gets executed on the database. It could result in data theft, by dumping database
contents, or the distruction of data, say, by using the DROP TABLE command.



# Clickjacking('django.middleware.clickjacking.XFrameOptionsMiddleware')
is a means of misleading a user to click on a hidden link or button in
the browser when they were intending to click on something else. This is typically
implemented using an invisible IFRAME that contains the target website over a
dummy web page(shown here) that the user is likely to click on



# Shell injection
As the name suggests, shell injection or command injection allows an attacker
to inject malicious code to a system shell such as bash. Even web applications use
command-line programs for convenience and their functionality. Such processes
are typically run within a shell.



# A handy security checklist
1. Dont trust data from a browser, API, or any outside sources: This is a
fundamental rule. Make sure you validate and sanitize any outside data.
2. Dont keep SECRET_KEY in version control: As a best practice, pick
SECRET_KEY from the environment. Check out the django-environ package.
3. Dont store passwords in plain text: Store your application password hashes
instead. Add a random salt as well.
4. Dont log any sensitive data: Filter out the confidential data such as credit
card details or API keys from your log files.
5. Any secure transaction or login should use SSL: Be aware that
eavesdroppers in the same network as you are could listen to your web
traffic if is not in HTTPS. Ideally, you ought to use HTTPS for the entire site.
6. Avoid using redirects to user-supplied URLs: If you have redirects such as
http://example.com/r?url=http://evil.com, then always check against
whitelisted domains.
7. Check authorization even for authenticated users: Before performing
any change with side effects, check whether the logged-in user is allowed
to perform it.
8. Use the strictest possible regular expressions: Be it your URLconf or
form validators, you must avoid lazy and generic regular expressions.
9. Dont keep your Python code in web root: This can lead to an accidental
leak of source code if it gets served as plain text.
10. Use Django templates instead of building strings by hand: Templates
have protection against XSS attacks.
11. Use Django ORM rather than SQL commands: The ORM offers protection
against SQL injection.
12. Use Django forms with POST input for any action with side effects: It might
seem like overkill to use forms for a simple vote button. Do it.
13. CSRF should be enabled and used: Be very careful if you are exempting
certain views using the @csrf_exempt decorator.
14. Ensure that Django and all packages are the latest versions: Plan for
updates. They might need some changes to be made to your source code.
However, they bring shiny new features and security fixes too.
15. Limit the size and type of user-uploaded files: Allowing large file uploads
can cause denial-of-service attacks. Deny uploading of executables or scripts.
16. Have a backup and recovery plan: Thanks to Murphy, you can plan for an
inevitable attack, catastrophe, or any other kind of downtime. Make sure
you take frequent backups to minimize data loss.


























# Gathering requirements:

1. Talk directly to the application owners even if they are not technical savvy.
2. Make sure you listen to their needs fully and note them.
3. Dont use technical jargon such as "models". Keep it simple and use end-user
   friendly terms such as a "user profile".
4. Set the right expectations. If something is not technically feasible or difficult,
   make sure you tell them right away.
5. Sketch as much as possible. Humans are visual in nature. Websites more so.
   Use rough lines and stick figures. No need to be perfect.
6. Break down process flows such as user signup. Any multistep functionality
   needs to be drawn as boxes connected by arrows.
7. Finally, work through the features list in the form of user stories or in any
   easy way to understand the form.
8. Play an active role in prioritizing the features into high, medium,
   or low buckets.
9. Be very, very conservative in accepting new features.
10. Post-meeting, share your notes with everyone to avoid misinterpretations.

+. Single-page document that quickly tells what the site is meant to be
