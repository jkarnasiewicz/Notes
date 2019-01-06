# Design Patterns
Well-known solutions to recurring problems - widely accepted solutions by the software
development community

# Why use design patterns?
Systematic reuse of design ideas or best practices yields lower cost and higher quality

# Important characteristics
1. Incomplite by design to promote customization

2. Knowing when to use a design pattern and when not to use it, is crucial, especially
because the design patterns can cause more problems instead of solving problems when
they are misused (e.g. side effects, such as worse performance when you're trying to
use one of the design patterns to accomplish better security)


# Design patterns types
1. creational, used to create objects in a systematic way, e.g. polymorphism, interfaces
   --> flexibility
    a) factory (uncertainties in types of objects)
    b) abstract factory (useful when a client expects to receive a family of related objects
       at a given time, but dont have to know which family it is until run time)
    c) singleton (global variable in an object-oriented way => only one instance needed)
    d) builder (try to solve problems with excessive number of constructors)
    e) prototype (cloning as good alternative for creating many identical objects individually)
2. structural, establishes useful relationships between software components in certain
   settings or configurations, e.g. inheritance, interfaces
   --> different goals yield different structures
    a) decorator (add new features to an existing object, apply dynamic changes)
    b) proxy (middleman, postpone object creation unless absolutely necessary,
       clients interacting with a proxy)
    c) adapter (converts the interface of a class into another one a client is expecting
       using uniform interface)
    d) composite (recursive tree data structure(composite/child, catalog/file objects))
    e) bridge (untangle an unnecessary complicated class hierarchy, especially when
       implementation specific classes are mixed together with implementation-independent
       classes)

    class DrawingAPIOne(object):
        "Implementaion-specific abstraction: concrete class one"
        def draw_circle(self, radious):
            pass

    class DrawingAPITwo(object):
        "Implementaion-specific abstraction: concrete class two"
        def draw_circle(self, radious):
            pass

    class Circle(object):
        "Implementation-independent abstraction"
        def __init__(self, radius, drawing_api):
            self._radius = radius
            self._drawning_api = drawing_api

        def draw(self):
            "Implermentaion-specific abstraction taken care of by another class: DrawingAPI"
            self._drawning_api.draw_circle(self._radius)

        def scale(self, percent):
            "Implementation-independent"
            self._radius *= percent

    circle1 = Circle(3, DrawingAPIOne())
    circle1.draw()
    circle2 = Circle(7, DrawingAPITwo())
    circle2.draw()



3. behavioral, best pratices of objects interaction(how objects interact with each other),
   e.g. methods and their signatures, interfaces
   --> define the protocols in between this objects, when they trying to work together to
   accomplish common goal




In the world of software, the term design pattern refers to a general repeatable
solution to a commonly occurring problem in software design

Each pattern describes a problem, which occurs over and over again in our environment,
and then describes the core of the solution to that problem in such a way that you can
use this solution a million times over, without ever doing it the same way twice

# Observer pattern - Spreading information to all listeners
This is the basic pattern in which an object tells other objects about something
interesting

# Strategy pattern - Changing the behavior of an algorithm
Sometimes, the same piece of code must have different behavior for different
invocation by different clients

# Singleton pattern - Providing the same view to all
The singleton pattern maintains the same state for all instances of a class

# Template pattern - Refining algorithm to use case(Inheritance, overide methods)

# Template Method design pattern
A template method defines an algorithm in terms of abstract operations that subclasses
override to provide concrete behavior

# Adaptor pattern - Bridging class interfaces
This pattern is used to adapt a given class to a new interface

    def __getattr__(self, attr):
      return getattr(self.fish, attr)

# Facade pattern - Hiding system complexity for a simpler interface

# Flyweight pattern - Consuming less memory with shared objects

# Command pattern - Easy-execution management for commands (83 Python Unlock)

# Abstract factory
class Animal(six.with_metaclass(abc.ABCMeta, object)):
    """ clients only need to know this interface for animals"""
    @abc.abstractmethod
    def sound(self, ):
        pass

# Registry pattern - Adding functionality from anywhere in code to class

# State pattern - Changing execution based on state





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
This section contains design patterns that deal with accessing model properties or
performing queries on them.

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
Solution: Use template inheritance wherever possible and include snippets elsewhere

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





# Peter Norvig Design Patterns book
# The message from Peter Norvig’s design patterns slides is that the Command and Strategy
# patterns — along with Template Method and Visitor — can be made simpler or even
# 'invisible' with first class functions, at least for some applications of these patterns

# Python has first-class functions and first-class types, features that Norvig claims affect
# 10 of the 23 patterns

# The authors are explicit right at the beginning of their book that
# 'some of our patterns are supported directly by the less common object-oriented languages'


# Url
https://www.linkedin.com/learning/python-design-patterns/welcome?autoplay=true&trk=course_tocItem&upsellOrderOrigin=trk_default_learning
