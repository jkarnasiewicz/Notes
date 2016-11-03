# Django design patterns and best pratices

# app.py
Previously, there was no specific place for initializing the signal code. Typically, they
were imported or implemented in models.py (which was unreliable)





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




# MODELS
# Structural patterns

# Patterns – normalized models
# denormalization(speed of the queries) and normalization(space with consistent data)
Problem: By design, model instances have duplicated data that cause data inconsistencies.
Solution: Break down your models into smaller models through normalization.
Connect these models with logical relationships between them.



# Pattern – model mixins
# Smaller mixins are better. Whenever a mixin becomes large and violates the Single
# Responsibility Principle, consider refactoring it into smaller classes. Let a mixin do
# one thing and do it well
Problem: Distinct models have the same fields and/or methods duplicated violating
the DRY principle.
Solution: Extract common fields and methods into various reusable model mixins.



# Pattern – service/utils objects
Problem: Models can get large and unmanageable. Testing and maintenance
get harder as a model does more than one thing.
Solution: Refactor out a set of related methods(e.g. @staticmethod or celery tasks)
into a specialized 'service' or 'utils' object.



# Retrieval patterns
# This section contains design patterns that deal with accessing model properties or
# performing queries on them.

# Pattern – property field
Problem: Models have attributes that are implemented as methods. However, these
attributes should not be persisted to the database.
Solution: Use the property decorator on such methods(@property)
# If it is an expensive calculation, we might want to cache the result(@cached_property)



# Pattern – custom model managers
Problem: Certain queries on models are defined and accessed repeatedly
throughout the code violating the DRY principle.
Solution: Define custom managers to give meaningful names to common queries



# VIEWS
# Pattern – context enhancers
Problem: Several views need the same context variable
Solution: Create a mixin or context processors(TEMPLATE_CONTEXT_PROCESSORS)
that sets the shared context variable



# Pattern – services
# This form of a service is usually called a web Application Programming Interface (API).
Problem: Information from your website is often scraped and processed by
other applications.
Solution: Create lightweight services that return data in machine-friendly formats,
such as JSON or XML(e.g. Django REST framework)



# TEMPLATES
# Pattern – template inheritance tree
Problem: Templates have lots of repeated content in several pages.
Solution: Use template inheritance wherever possible and include snippets elsewhere.





# ADMIN
# Don't give admin access to end users

# Pattern – feature flags
# selected users within a controlled experiment, performance testing for new features
Problem: Publishing of new features to users and deployment of the corresponding
code in production should be independent.
Solution: Use feature flags to selectively enable or disable features after deployment





# FORMS
# Pattern – dynamic form generation
Problem: Adding form fields dynamically or changing form fields from what
has been declared.
Solution: Add or change fields during initialization of the form.

class PersonDetailsForm(forms.Form):
	name = forms.CharField(max_length=100)
	age = forms.IntegerField()

	def __init__(self, *args, **kwargs):
		upgrade = kwargs.pop("upgrade", False)
		super().__init__(*args, **kwargs)

		if upgrade:
			self.fields["first_class"] = forms.BooleanField(
				label="Fly First Class?")

# PersonDetailsForm(upgrade=True)



# Pattern – multiple form actions per view with prefix
form = SubscribeForm(prefix="offers")





# TESTING AND DEBUGGING

# Here are some qualities of a good test case (which is a subjective term, of course)
# in the form of an easy-to-remember mnemonic "F.I.R.S.T. class test case":
1. Fast: the faster the tests, the more often they are run. Ideally, your tests
should complete in a few seconds.
2. Independent: Each test case must be independent of others and can be
run in any order.
3. Repeatable: The results must be the same every time a test is run. Ideally,
all random and varying factors must be controlled or set to known values
before a test is run.
4. Small: Test cases must be as short as possible for speed and ease of
understanding.
5. Transparent: Avoid tricky implementations or ambiguous test cases.



# Perhaps, even more important are the don'ts to remember while writing test cases:
1. Do not (re)test the framework: Django is well tested. Dont check for URL
lookup, template rendering, and other framework-related functionality.
2. Do not test implementation details: Test the interface and leave the minor
implementation details. It makes it easier to refactor this later without
breaking the tests.
3. Test models most, templates least: Templates should have the least business
logic, and they change more often.
4. Avoid HTML output validation: Test views use their context variables
output rather than its HTML-rendered output.
5. Avoid using the web test client in unit tests: Web test clients invoke several
components and are therefore, better suited for integration tests.
6. Avoid interacting with external systems: Mock them if possible. Database is
an exception since test database is in-memory and quite fast.



# https://docs.python.org/3/library/unittest.html#assert-methods
# https://docs.djangoproject.com/en/1.10/topics/testing/tools/#assertions
assertWarns



# TestCase
# Before running each test, Django resets the database to its initial state



# Mocks (create new class for mocks in S5 file)
# Mock objects are objects that can test the behavior, and stubs are
# simply placeholder implementations


from django.test import TestCase
from unittest.mock import patch
from django.contrib.auth.models import User

class TestSuperHeroCheck(TestCase):
	def test_checks_superhero_service_obj(self):
		with patch("profiles.models.SuperHeroWebAPI") as ws:
			ws.is_hero.return_value = True
			u = User.objects.create_user(username="t")
			r = u.profile.is_superhero()
		ws.is_hero.assert_called_with('t')
		self.assertTrue(r)



# Pattern – test fixtures and factories

# fixtures
fixtures = ['posts']

# factory
class PostFactory:

	def make_post(self):
		return Post.objects.create(message="")

class PostTestCase(TestCase):

	def setUp(self):
		self.blank_message = PostFactory().makePost()

	def test_some_post_functionality(self):
		pass

# factory_boy library

# libraries: py.test, nose and coverage.py



# DEBUGGING
# stop a django application in the middle of execution
# assert False


# Logging
import logging
logger = logging.getLogger(__name__)

def complicated_view():
	logger.debug("Entered the complicated_view()!")



# The Django Debug Toolbar



# The Python debugger pdb
import pdb
pdb.set_trace()

# also try:
# ipdb
# pudb => import pudb; pudb.set_trace()



# Debugging Django templates
set TEMPLATE_DEBUG to True

# debug tag(dump all the variables)
<textarea onclick="this.focus();this.select()" style="width: 100%;">
	{% filter force_escape %}
		{% debug %}
	{% endfilter %}
</textarea>



# custom template tag debug
# templatetags/debug.py
import pudb as dbg
from django.template import Library, Node

register = Library()

class PdbNode(Node):

	def render(self, context):
		dbg.set_trace() # Debugger will stop here
		return ''

@register.tag
def pdb(parser, token):
	return PdbNode()

# template.html
{% load debug %}
{% for item in items %}
	{# Some place you want to break #}
	{% pdb %}
{% endfor %}

Within the debugger
print(context["item"])





# SECURITY
# Cross-site scripting (XSS)
# considered the most prevalent web application security flaw today,
# enables an attacker to execute his malicious scripts (usually JavaScript)
# on web pages viewed by users



# Cross-Site Request Forgery (CSRF)
# is an attack that tricks a user into making
# unwanted actions on a website, where they are already authenticated, while they
# are visiting another site. Say, in a forum, an attacker can place an IMG or IFRAME tag
# within the page that makes a carefully crafted request to the authenticated site.



# SQL injection
# is the second most common vulnerability of web applications,
# after XSS. The attack involves entering malicious SQL code into a query that
# gets executed on the database. It could result in data theft, by dumping database
# contents, or the distruction of data, say, by using the DROP TABLE command.



# Clickjacking('django.middleware.clickjacking.XFrameOptionsMiddleware')
# is a means of misleading a user to click on a hidden link or button in
# the browser when they were intending to click on something else. This is typically
# implemented using an invisible IFRAME that contains the target website over a
# dummy web page(shown here) that the user is likely to click on



# Shell injection
# As the name suggests, shell injection or command injection allows an attacker
# to inject malicious code to a system shell such as bash. Even web applications use
# command-line programs for convenience and their functionality. Such processes
# are typically run within a shell.



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




# PRODUCTION
# hosting options, including PaaS(platform as a service) and VPS(virtual private server)

Components of a stack
1. Which OS and distribution? For example: Debian, Red Hat, or OpenBSD.
2. Which WSGI server? For example: Gunicorn, uWSGI.
3. Which web server? For example: Apache, Nginx.
4. Which database? For example: PostgreSQL, MySQL, or Redis.
5. Which caching system? For example: Memcached, Redis.
6. Which process control and monitoring system? For example: Upstart,
   Systemd, or Supervisord.
7. How to store static media? For example: Amazon S3, CloudFront.





# PRODUCTION PERFORMANCE(DDP 175)
# profiling and finding bottleneck
# Frondend performance
1. Cache infinitely with CachedStaticFilesStorage
2. Use a static asset manager (e.g. django-pipeline or webassets)


# Backend performance
django-debug-toolbar
django-silk

enable the cached template loader in production

Reduce database hits with select_related: If you are using a
OneToOneField or a Foreign Key relationship, in forward direction,
for a large number of objects, then select_related() can perform a
SQL join and reduce the number of database hits.

Reduce database hits with prefetch_related: For accessing a
ManyToManyField method or, a Foreign Key relation, in reverse direction,
or a Foreign Key relation in a large number of objects, consider using
prefetch_related to reduce the number of database hits.

Fetch only needed fields with values or values_list: You can save time
and memory usage by limiting queries to return only the needed fields
and skip model instantiation using values() or values_list()

Denormalize models: Selective denormalization improves performance
by reducing joins at the cost of data consistency

Add an Index: If a non-primary key gets searched a lot in your queries,
consider setting that fields db_index to True in your model definition

Create, update, and delete multiple rows at once: Multiple objects can
be operated upon in a single database query with the bulk_create(),
update(), and delete() methods

Most production systems use a memory-based caching system such as Redis or
Memcached

Cached session backend
By default, Django stores its user session in the database. This usually gets
retrieved for every request. To improve performance, the session data can be
stored in memory by changing the SESSION_ENGINE setting. For instance,
add the following in settings.py to store the session data in your cache:
SESSION_ENGINE = "django.contrib.sessions.backends.cache"





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





# PYTHON FUNDAMENTALS
# Think of named references to objects rather than variables
# shallow copy - copy only the reference to the key, value paires not the objects themselves
# e.g.
# a = [[0, 1]]*4
# a[2].append(7)


# Dynamic type system
# In dynamic type system objects types are only resolved at runtime (w czasie wykonywania programu)

# Strong type system
# In a strong type system there is no implicit type conversion
# e.g. 'string' + 43 => TypeError



# Python name scopes(names are looked up in four nested scopes)
Local - inside the current function
Enclosing - any and all enclosing functions
Global - top-level of module
Built-in - provide by the builtins module



# Value equality vs. identity(id())
# Value comparison can be controlled program atically('==')
# [] == [] => True
Value - equivalent 'contents'

# 'is'
# [] is [] => False
Identity - same object



# Default argument expressions evaluated once, when def is executed
# Always use immutable objects as a default argument value



# raise without an argument re-raises the current exception



# output of print() can be redirected using the optional file argument


# Docstring
def sqrt(x):
	'''Compute square root using the method of Heron of Alexandria.

	Args:
		x: The number for which the square root is to be computed.

	Returns:
		The square root of x.

	Raises:
		ValueError: If x is negative.
	'''
	...


# prime numbers
def is_prime(x):
	if x <2:
		return False
	for i in range(2, int(sqrt(x)) + 1):
		if x% i == 0:
			return False
	return True



# ITERATION PROTOCOLS
# Iterable protocol
# Iterables are objects over which we can iterate item by item
Iterable objects can be passed to the built-in iter() function to get an iterator
iterator = iter(iterable)

# Iterator protocol
# we retrive an iterator from an iterable object using the built-in iter() function
# iterators produce items one-by-one from the underlying iterable series each time
# they are passed to the nuilt-in next() function
Iterator objects ca be passed to the built-in next() function to fetch the next item
item = next(iterator)


# GENERATORS
# generators are defined by any python function witch using the 'yield'
# keyword at least once in it's definition
specify iterable sequences - all generators are iterators
lazily evaluated - the next value in the sequence is computed on demand
can model infinite sequence - such as data streams with no definite end

# Stateful generators
generators resume execution
can maintain state in local variables
complex control flow
lazy evaluation

# generators comprehensions
(expr(item) for item in iterable)
