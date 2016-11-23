# REST - representational state transfer
# Podejście REST sugeruje przygotowanie struktury adresu URL dopasowanej do struktury danych
# RESTful URLs are very useful for designing CRUD interfaces(Create, Read, Update, and Delete)

# API - Application Programming Interface



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
