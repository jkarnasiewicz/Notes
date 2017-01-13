# -*- coding: utf-8 -*-
# raise from lambda !

# We then saw how to delegate blocking jobs — such as saving a file — to a thread pool
# using the loop.run_in_executor method.

# must explicitly schedule execution
# loop.create_task(three_stages(request1))


# Metaprogramming

# + json.load/dump

# from urllib.request import urlopen
# import warnings
# import os
# import json
# URL = 'http://www.oreilly.com/pub/sc/osconfeed'
# JSON = 'data/osconfeed.json'

# def load():
#     if not os.path.exists(JSON):
#         msg = 'downloading {} to {}'.format(URL, JSON)
#         warnings.warn(msg)
#         # multiple with statement  
#         with urlopen(URL) as remote, open(JSON, 'wb') as local:
#             local.write(remote.read())

#     with open(JSON) as fp:
#         return json.load(fp)

# Exploring JSON-like data with dynamic attributes
# from collections import abc, namedtuple

# City = namedtuple('City', 'name population')
# van = City('Vancouver', 800000)
# a = {'a': {'example': {'qwe': '3 332  23d32d3d23', 'van': (33, van, 33)}, 'list': [-1, -7, 'a', 'r', 6]}, 'b': 5, 'c': [3, 7], 'van': van}


# class FrozenJSON:
#     """A read-only façade for navigating a JSON-like object
#     using attribute notation
#     """
#     def __init__(self, mapping):
#         self.__data = dict(mapping)

#     def __getattr__(self, name):
#         if hasattr(self.__data, name):
#             # searching for method object e.g dict.keys()
#             return getattr(self.__data, name)
#         else:
#             return FrozenJSON.build(self.__data[name])

#     @classmethod
#     def build(cls, obj):
#         if isinstance(obj, abc.Mapping):
#             return cls(obj)
#         elif isinstance(obj, abc.MutableSequence):
#             print('list', obj)
#             return [cls.build(item) for item in obj]
#         else:
#             print('obj', obj)
#             return obj

# fj = FrozenJSON(a)
# print(fj.a.list[3])


# alternatively implementing with __new__
# from collections import abc
# class FrozenJSON:
#     """A read-only façade for navigating a JSON-like object
#     using attribute notation
#     """
#     def __new__(cls, arg):
#         if isinstance(arg, abc.Mapping):
#             return super().__new__(cls)
#         elif isinstance(arg, abc.MutableSequence):
#             return [cls(item) for item in arg]
#         else:
#             return arg

#     def __init__(self, mapping):
#         self.__data = {}
#         for key, value in mapping.items():
#             if iskeyword(key):
#                 key += '_'
#             self.__data[key] = value

#     def __getattr__(self, name):
#         if hasattr(self.__data, name):
#             return getattr(self.__data, name)
#         else:
#             return FrozenJSON(self.__data[name])



# import keyword
# print(len(keyword.kwlist))


# This is a common shortcut to build an instance with attributes created from keyword arguments
# updating an instance __dict__ with a mapping is a quick way to create a bunch of attributes in that instance9
# class Record:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#     def __eq__(self, other):
#         if isinstance(other, Record):
#             return self.__dict__ == other.__dict__
#         else:
#             return NotImplemented


# Custom exceptions are usually marker classes, with no body. A docstring
# explaining the usage of the exception is better than a mere pass statement.
# class MissingDatabaseError(RuntimeError):
#     """Raised when a database is required but was not set."""

# vars returns the __dict__ of obj, vars(obj) == obj.__dict__

# property
# properties are class attributes designed to manage instance attributes !!!!!!!!!!!!!!!!!!

# Properties override instance attributes(Instance attribute does not shadow class property)
# Properties are always class attributes, but they actually manage attribute access in the
# instances of the class.


# New class property shadows existing instance attribute
# Class.data = property(lambda self: 'the "data" prop value')

# The main point of this section is that an expression like obj.attr does not search for
# attr starting with obj. The search actually starts at obj.__class__, and only if there is
# no property named attr in the class, Python looks in the obj instance itself


# documentation of the properties

# class Foo:
#     @property
#     def bar(self):
#         "The bar attribute"
#         return self.__dict__['bar']

#     @bar.setter
#     def bar(self, value):
#         return 5

# help(Foo)
# help(Foo.bar)

# Remember: the right side of an assignment is evaluated first, so when quantity() is invoked, the price class attribute doesn’t even exist

# Property factory
# def quantity(storage_name):

#     def qty_getter(instance):
#         # qty_getter references storage_name, so it will be preserved in the closure of
#         # this function; the value is retrieved directly from the instance.__dict__ to
#         # bypass the property and avoid an infinite recursion
#         return instance.__dict__[storage_name]

#     def qty_setter(instance, value):
#         if value > 0:
#             instance.__dict__[storage_name] = value
#         else:
#             raise ValueError('value must be > 0')
#     return property(qty_getter, qty_setter, doc='quantity property factory')


# class LineItem:
#     weight = quantity('weight')
#     price = quantity('price')

#     def __init__(self, description, weight, price):
#         self.description = description
#         self.weight = weight
#         self.price = price

#     def subtotal(self):
#         return self.weight * self.price


# a = quantity('help')
# print(a.fset.__closure__[0].cell_contents)
# nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)



# Essential attributes and functions for attribute handling

# obj.__class__ is the same as type(obj)
# Python looks for special methods such as __getattr__ only in an object’s class, and not in the instances themselves

# __dict__
# A mapping that stores the writable attributes of an object or class. An object that
# has a __dict__ can have arbitrary new attributes set at any time

# __slots__
# An attribute that may be defined in a class to limit the attributes its instances can
# have. __slots__ is a tuple of strings naming the allowed attributes

# + obok getattr, setattr, hasattr
# vars([object])
# Returns the __dict__ of object; vars can’t deal with instances of classes that define
# __slots__ and don’t have a __dict__ (contrast with dir, which handles such instances).
# Without an argument, vars() does the same as locals(): returns a dict
# representing the local scope.

# __getattr__(self, name)
# Called only when an attempt to retrieve the named attribute fails, after the obj,
# Class and its superclasses are searched. The expressions obj.no_such_attr, get
# attr(obj, 'no_such_attr') and hasattr(obj, 'no_such_attr') may trigger
# Class.__getattr__(obj, 'no_such_attr'), but only if an attribute by that name
# cannot be found in obj or in Class and its superclasses.

# __getattribute__(self, name)
# Always called when there is an attempt to retrieve the named attribute, except when
# the attribute sought is a special attribute or method. Dot notation and the get
# tattr and hasattr built-ins trigger this method. __getattr__ is only invoked after
# __gatattribute__, and only when __gatattribute__ raises AttributeError. To
# retrieve attributes of the instance obj without triggering an infinite recursion, implementations
# of __getattribute__ should use super().__getattri
# bute__(obj, name).


# Uniform Access Principle (or a variation of it) is the fact that
# function calls and object instantiation use the same syntax in Python: my_obj =
# foo(), where foo may be a class or any other callable



# Attribute Descriptors are a way of reusing the same access logic in multiple attributes. For example,
# field types in ORMs such as the Django ORM and SQL Alchemy are descriptors,
# managing the flow of data from the fields in a database record to Python object attributes
# and vice-versa



# class Quantity:
#     def __init__(self, storage_name):
#         self.storage_name = storage_name

#     def __set__(self, instance, value):
#         if value > 0:
#             instance.__dict__[self.storage_name] = value
#         else:
#             raise ValueError('value must be > 0')


# class LineItem:
#     weight = Quantity('weight')
#     price = Quantity('price')

#     def __init__(self, description, weight, price):
#         self.description = description
#         self.weight = weight
#         self.price = price

#     def subtotal(self):
#         return self.weight * self.price

# instance.__dict__[self.storage_name] = value
# the tempting but bad alternative would be:
# self.__dict__[self.storage_name] = value

# To understand why this would be wrong, think about the meaning of the first two
# arguments to __set__: self and instance. Here, self is the descriptor instance, which
# is actually a class attribute of the managed class. You may have thousands of LineI
# tem instances in memory at one time, but you’ll only have two instances of the descriptors:
# LineItem.weight and LineItem.price. So anything you store in the descriptor
# instances themselves is actually part of a LineItem class attribute, therefore it is shared
# among all LineItem instances


# Property factory versus descriptor class
# def quantity():
#     try:
#         quantity.counter += 1
#     except AttributeError:
#         quantity.counter = 0

#     storage_name = '_{}:{}'.format('quantity', quantity.counter)

#     def qty_getter(instance):
#         return getattr(instance, storage_name)

#     def qty_setter(instance, value):
#         if value > 0:
#             setattr(instance, storage_name, value)
#         else:
#             raise ValueError('value must be > 0')

#     return property(qty_getter, qty_setter)



# Template Method design pattern:
# A template method defines an algorithm in terms of abstract operations that subclasses
# override to provide concrete behavior

# Class.descriptor_name triggers the descriptor __get__ method, passing None as the second argument (instance)

# Overriding Descriptor/data descriptors
# A descriptor that implements the __set__ method it called an overriding descriptor,
# because although it is a class attribute, a descriptor implementing __set__ will override
# attempts to assign to instance attributes. This is how Example 20-2 was implemented.
# Properties are also overriding descriptors: if you don’t provide a setter function, the
# default __set__ from the property class will raise AttributeError to signal that the
# attribute is read-only

# Overriding descriptor without __get__/data descriptors without __get__
# Usually, overriding descriptors implement both __set__ and __get__, but it’s also possible
# to implement only __set__, as we saw in Example 20-1. In this case, only writing
# is handled by the descriptor. Reading the descriptor through an instance will return the
# descriptor object itself because there is no __get__ to handle that access. If a namesake
# instance attribute is created with a new value via direct access to the instance
# __dict__, the __set__ method will still override further attempts to set that attribute,
# but reading that attribute will simply return the new value from the instance, instead of
# returning the descriptor object. In other words, the instance attribute will shadow the
# descriptor, but only when reading

# Non-overriding descriptor/non-data descriptors
# If a descriptor does not implement __set__, then it’s a non-overriding descriptor. Setting
# an instance attribute with the same name will shadow the descriptor, rendering it
# ineffective for handling that attribute in that specific instance. Methods are implemented
# as non-overriding descriptors

# The bound method object also has a __call__ method, which handles the actual invocation.
# This method calls the original function referenced in __func__, passing the
# __self__ attribute of the method as the first argument. That’s how the implicit binding
# of the conventional self argument works



# Descriptor usage tips
# 1. Use property to keep it simple
# The property built-in actually creates overriding descriptors implementing both
# __set__ and __get__, even if you do not define a setter method. The default __set__
# of a property raises AttributeError: can't set attribute, so a property is the easiest
# way to create a read-only attribute, avoiding the issue described next.
# 2. Read-only descriptors require __set__
# If you use a descriptor class to implement a read-only attribute you must remember to
# code both __get__ and __set__, otherwise setting a namesake attribute on an instance
# will shadow the descriptor. The __set__ method of a read-only attribute should just
# raise AttributeError with a suitable message 5.
# 3. Validation descriptors can work with __set__ only
# In a descriptor designed only for validation, the __set__ method should check the value
# argument it gets, and if valid, set it directly in the instance __dict__ using the descriptor
# instance name as key. That way, reading the attribute with the same name from the
# instance will be as fast as possible, as it will not require a __get__. See the code for
# Example 20-1.
# 4. Caching can be done efficiently with __get__ only
# If you code just the __get__ method you have a non-overriding descriptor. These are
# useful to make some expensive computation and then cache the result by setting an
# attribute by the same name on the instance. The namesake instance attribute will shadow
# the descriptor, so subsequent access to that attribute will fetch it directly from the instance
# __dict__ and not trigger the descriptor __get__ anymore.
# 5. Non-special methods can be shadowed by instance attributes
# Because functions and methods only implement __get__, they do not handle attempts
# at setting instance attributes with the same name, so a simple assignment like
# my_obj.the_method = 7 means that further access to the_method through that instance
# will retrieve the number 7 — without affecting the class or other instances. However,
# this issue does not interfere with special methods. The interpreter only looks for special
# methods in the class itself, in other words, repr(x) is executed as
# x.__class__.__repr__(x), so a __repr__ attribute defined in x has no effect of
# repr(x). For the same reason, the existence of an attribute named __getattr__ in an
# instance will not subvert the usual attribute access algorithm.



# Metaprogramming
# Invoking type with three arguments is a common way of creating a class dynamically
# type(my_object) to get the class of the object — same as my_object.__class__

# Class decorators are a simpler way of doing something that
# previously required a metaclass: customizing a class the moment it’s created

# At import time, the interpreter parses the source code of a .py module in one pass from
# top to bottom, and generates the bytecode to be executed. That’s when syntax errors
# may occur. If there is an up-to-date .pyc file available in the local __pycache__, those
# steps are skipped because the bytecode is ready to run

# That’s why the border between “import time” and “run time” is
# fuzzy: the import statement can trigger all sorts of “run time” behavior

# In the usual case, this means that the interpreter defines top level
# functions at import time, but executes their bodies only when — and if — the functions
# are invoked at run time

# For classes, the story is different: at import time, the interpreter executes the body of
# every class, even the body of classes nested in other classes. Execution of a class body
# means that the attributes and methods of the class are defined, and then the class object
# itself is built. In this sense, the body of classes is “top level code”: it runs at import time

# A metaclass is a class factory, except that instead of a function, like record_factory from Example 21-2, a metaclass is written as a class

# The classes object and type have a unique relationship: object is an
# instance of type, and type is a subclass of object. This relationship
# is “magic”: it cannot be expressed in Python because either class would
# have to exist before the other could be defined. The fact that type is
# an instance of itself is also magical

# Every class is an instance of type, directly or indirectly, but only metaclasses are also subclasses of type

# The important takeaway here is that all classes are instances of type, but metaclasses
# are also subclasses of type, so they act as class factories. In particular, a metaclass can
# customize its instances by implementing __init__. A metaclass __init__ method can
# do everything a class decorator can do, but its effects are more profound, as the next exercise demonstrates.

# class MetaAleph(type):

#     @classmethod
#     def __prepare__(cls, name, bases):
#         return collections.OrderedDict()

#     def __init__(cls, name, bases, dic):
#         def inner_2(self):
#             pass

#     cls.method_z = inner_2


# class ClassFive(metaclass=MetaAleph):

#     def __init__(self):
#         pass

#     def method_z(self):
#         pass

# When coding a metaclass, it’s conventional to replace self by cls.
# For example, in the __init__ method of the metaclass, using cls as
# the name of the first argument makes it clear that the instance under
# construction is a class

# The body of __init__ defines an inner_2 function, then binds it to cls.method_z. The
# name cls in the signature of MetaAleph.__init__ refers to the class being created, e.g.
# ClassFive. On the other hand, the name self in the signature of inner_2 will eventually
# refer to an instance of the class we are creating, e.g. an instance of ClassFive.

# The __prepare__ method is invoked by
# the interpreter before the __new__ method in the metaclass to create the mapping that
# will be filled with the attributes from the class body
# @classmethod
#   def __prepare__(cls, name, bases):
#       pass

# metaclasses are used in frameworks and libraries that help programmers perform, among other tasks:
# • attribute validation;
# • applying decorators to many methods at once;
# • object serialization or data conversion;
# • object-relational mapping;
# • object-based persistency;
# • dynamic translation of class structures from other languages


# Class metaprogramming is about creating or customizing classes dynamically. Classes
# in Python are first-class objects, so we started the chapter by showing how a class can
# be created by a function invoking the type built-in metaclass

# !!! check import order in metaprograming chapter
# but clearly a lot of code runs triggered by the import statement

# I haven’t yet found a language that manages to be easy for beginners, practical for professionals
# and exciting for hackers in the way that Python is

# “Only those who work make mistakes" - great advice to avoid being paralyzed by the fear of making errors

# 717 python jargon





# Additional topics
# Everything is executed at the module level when Python first imports a module. Function bodies
# (and generator expression bodies) are the exception here, not the rule. Python executes everything
# to create the objects contained in a module; like everything in Python, classes are objects, and so are functions.
# The only reason a class body uses a separate code object is because a class body is executed in a separate namespace,
# with that namespace then forming the class attributes. Class bodies are not the only such namespaces;
# set and dict comprehensions, and in Python 3, list comprehensions are also executed with a separate namespace,
# scoping their locals. So functions and generator expressions are the exception, expressly because their whole
# purpose is to be executed at a later time. Note that the function definition is executed:

# import shelve

























# JavaScript The Good Parts
# JavaScript is an important language because it is the language of the web browser. Its
# association with the browser makes it one of the most popular programming languages in the world

# The API of the browser, the Document Object Model (DOM) is quite awful, and JavaScript is unfairly blamed

# literal - notations for atomic values
# In computer science, a literal is a notation for representing a fixed value in source code.
# Almost all programming languages have notations for atomic values such as integers,
# floating-point numbers, and strings, and usually for booleans and characters;
# some also have notations for elements of enumerated types and compound values such as
# arrays, records, and objects. An anonymous function is a literal for the function type


# When used inside of a function, the var statement defines the function’s private variables

# The switch, while, for, and do statements are allowed to have an optional label prefix
# that interacts with the break statement

# A function always returns a value. If the return value is not specified, then undefined is returned

# If the function was invoked with the new prefix and the return value is not an object, then this (the new object) is returned instead

# throw/try/catch

# Scope in a programming language controls the visibility and lifetimes of variables and parameters

# This is possible because the function has access to the context in which it was created. This is called closure.

# global object - window.foo

# A JavaScript literal represents a value of a specific type, such as a quoted string (String),
# floating-point number (Number), or boolean (Boolean): "this is a string", 1.45, true
# A JavaScript primitive is an instance of a particular data type, and there are five such in
# the language: String, Number, Boolean, null, and undefined

# 'hello' === new String('hello') // false, literal(typeof => string) vs primitive(typeof => object)

# undefine, NaN, null

# Declarations
# There are three kinds of declarations in JavaScript.
# var - Declares a variable, optionally initializing it to a value.
# let - Declares a block scope local variable, optionally initializing it to a value.
# const - Declares a read-only named constant. 

# hoisting
# Another unusual thing about variables in JavaScript is that you can refer to a variable
# declared later, without getting an exception. This concept is known as hoisting;
# variables in JavaScript are in a sense "hoisted" or lifted to the top of the
# function or statement. However, variables that are hoisted will return a value of undefine

# Global variables
# Global variables are in fact properties of the global object.
# In web pages the global object is window, so you can set and access global variables
# using the window.variable syntax



# !
# let allows you to declare variables that are limited in scope to the block, statement,
# or expression on which it is used. This is unlike the var keyword,
# which defines a variable globally, or locally to an entire function regardless of block scope.

# JavaScript, blocks do not have scope; only functions have scope
# starting with ECMAScript Edition 6, let and const declarations allow you to create block-scoped variables

# When used inside a block, let limits the variable's scope to that block.
# Note the difference between var whose scope is inside the function where it is declared.
# var a = 1;
# var b = 2;

# if (a === 1) {
#   var a = 11; // the scope is global
#   let b = 22; // the scope is inside the if-block

#   console.log(a);  // 11
#   console.log(b);  // 22
# } 

# console.log(a); // 11
# console.log(b); // 2



# A var has function scope (it declares a variable that's visible throughout the function) even though it looks like it has block scope.

# At the top level of programs and functions, let, unlike var, does not create a property on the global object. For example:
# var x = 'global';
# let y = 'global';
# console.log(this.x); // "global"
# console.log(this.y); // undefined



# Adopt let and const(and ===). Stop using var !
# let x = 'x';

# Constants
# You can create a read-only, named constant with the const keyword
# const PI = 3.14;
# A constant cannot change value through assignment or be re-declared
# while the script is running. It has to be initialized to a value.

# JavaScript is a dynamically typed language.
# That means you dont have to specify the data type of a variable when you declare it,
# and data types are converted automatically as needed during script execution

# .toString()
# parseInt()   function parses a string argument and returns an integer of the specified radix
# parseInt("11", 2); // 3
# parseFloat() function parses a string argument and returns a floating point number.
# typeof
# addEventListener

# Literals
# You use literals to represent values in JavaScript.
# These are fixed values, not variables, that you literally provide in your script.
# Array literals 				var coffees = ["French Roast", "Colombian", "Kona"];
# Boolean literals 				true and false, Boolean("");  // false
# Floating-point literals 		-3.1E+12
# Integers 						-345
# Object literals 				var car = { myCar: "Saturn", getCar: carTypes("Honda"), special: sales };
# RegExp literals 				var re = /ab+c/;
# String literals 				"John's \n cat"
# !!!!IMP
# Template literals
# 	var name = "Bob", time = "today";
# 	`Hello ${name}, how are you ${time}?`

# var str = "this string \
# is broken \
# across multiple\
# lines."

# FUBAR (fucked up beyond all recognition)

# Exception
# var log = console.log;
# try {
#   throw "myException"; // generates an exception
# }
# catch (e) {
#   // statements to handle any exceptions
#   log(e); // pass exception object to error handler
# }
# finally {
#   log("finally over");
# }



# Promise
# function imgLoad(url) {
#   return new Promise(function(resolve, reject) {
#     var request = new XMLHttpRequest();
#     request.open('GET', url);
#     request.responseType = 'blob';
#     request.onload = function() {
#       if (request.status === 200) {
#         resolve(request.response);
#       } else {
#         reject(Error('Image didn\'t load successfully; error code:' 
#                      + request.statusText));
#       }
#     };
#     request.onerror = function() {
#       reject(Error('There was a network error.'));
#     };
#     request.send();
#   });
# }



# For example, getting all the nodes of a tree structure (e.g. the DOM)
# is more easily done using recursion:

# function walkTree(node) {
# 	if (node == null) {
#     return;
#   }
#   log('AAAA');
#   if(node.nodeName === 'P') {
#     log('BBB');
#     node.style.color = "purple";
#   }
  
#   for (var i = 0; i < node.childNodes.length; i++) {
#     walkTree(node.childNodes[i]);
#   }

# }

# walkTree(document.body);



# closures(function factories, and secure variable of the outer function)
# ! Be careful - the magical this variable is very tricky in closures.
# They have to be used carefully, as what this refers to depends completely
# on where the function was called, rather than where it was defined.

# A closure is the combination of a function and the scope object in which it was created. Closures let you save state

# function outside(x) {
# 	function inside(y) {
# 		return Math.pow(x, y);
# 	}
# 	return inside;
# }

# fn_inside = outside(3)
# fn_inside(3);



# function createPet(name) {
#   var sex;
  
#   return {
#     setName: function(newName) {
#       name = newName;
#     },
	
#     getName: function() {
#       return name;
#     },
	
#     getSex: function() {
#       return sex;
#     },
	
#     setSex: function(newSex) {
#       if(typeof newSex === "string" && (newSex.toLowerCase() === "male" || newSex.toLowerCase() === "female")) {
#         sex = newSex;
#       }
#     }
#   }
# }

# var pet = createPet("Vivie");
# log(pet.getName());                  // Vivie

# log(pet.setName("Oliver"));
# log(pet.setSex("male"));
# log(pet.getSex());                   // male
# log(pet.getName());                  // Oliver



# Using the arguments
# function myConcat(separator) {
#    let result = "";
#    for (let i = 1; i < arguments.length; i++) {
#       result += arguments[i] + separator;
#    }
#    return result;
# }

# myConcat(", ", "red", "orange", "blue");



# Default parameters
# function multiply(a, b=1) {
#   return a*b;
# }

# multiply(5);



# Rest parameters/Spread syntax
# function multiply(multiplier, ...theArgs) {
#   return theArgs.map(x => multiplier * x);
# }

# var arr = multiply(2, 1, 2, 3);
# console.log(arr); // [2, 4, 6]



# Arrow functions
# var a = ["Hydrogen", "Helium", "Lithium", "Beryllium"];
# var a2 = a.map(function(s){ return s.length }); // old
# var a3 = a.map(s => s.length); // new


# Lexical this
# function Person(){
#   this.age = 0;

#   setInterval(() => {
#     // |this| properly refers to the person object, dont need to use 'var self = this;'
#     this.age++;
#   }, 1000);
# }

# var p = new Person();



# Comparison
# Strict equal (===) 	Returns true if the operands are equal and of the same type
# Strict not equal (!==) 	Returns true if the operands are of the same type but not equal, or are of different type.

# Bitwise operators
# AND 15 & 9 	9 	1111 & 1001 = 1001
# OR  15 | 9 	15 	1111 | 1001 = 1111

# Unary operators
# delete objectName.property;

# typeof myFun;         // returns "function"
# typeof "round";       // returns "string"
# typeof 4;        	    // returns "number"
# typeof new Date();    // returns "object"
# typeof doesntExist;   // returns "undefined"
# typeof true; 		    // returns "boolean"
# typeof null; 		    // returns "object"



# Relational operators
# in - propNameOrNumber in objectName
# var trees = ["redwood", "bay", "cedar", "oak", "maple"];
# 0 in trees;        // returns true
# 6 in trees;        // returns false
# "bay" in trees;    // returns false (you must specify the index number,
#                    // not the value at that index)
# "length" in trees; // returns true (length is an Array property)
# "PI" in Math;          // returns true

# var mycar = { make: "Honda", model: "Accord", year: 1998 };
# "make" in mycar;  // returns true

# The instanceof operator returns true if the specified object is of the specified object type
# instanceof - objectName instanceof objectType
# var theDay = new Date(1995, 12, 17);
# if (theDay instanceof Date) {
#   // statements to execute
# }



# Expresions
# this
# <p>Enter a number between 18 and 99:</p>
# <input type="text" name="age" size=3 onChange="document.writeln(this.value);">


# Comprehensions

# Array comprehensions.
# [for (x of y) x]
# var abc = [ "A", "B", "C" ];
# [for (letters of abc) letters.toLowerCase()]; // [ "a", "b", "c" ]

# Generator comprehensions.
# (for (x of y) y)



# new
# You can use the new operator to create an instance of a user-defined
# object type or of one of the built-in object types. Use new as follows:

# var objectName = new objectType([param1, param2, ..., paramN]);



# Spread operator
# The spread operator allows an expression to be expanded in places where multiple arguments
# (for function calls) or multiple elements (for array literals) are expected

# var parts = ['shoulder', 'knees'];
# var lyrics = ['head', ...parts, 'and', 'toes'];

# function f(x, y, z) {return x + y + z }
# var args = [0, 1, 2];
# f(...args);



# Numbers(+Infinity, -Infinity, and NaN)
# Hexadecimal numbers(0123456789abcdef)
# Internationalization - Intl object is the namespace for the ECMAScript Internationalization API



# RegExp
# x(?=y) 	Matches 'x' only if 'x' is followed by 'y'. This is called a lookahead.
# For example, /Jack(?=Sprat)/ matches 'Jack' only if it is followed by 'Sprat'. /Jack(?=Sprat|Frost)/ matches 'Jack' only if it is followed by 'Sprat' or 'Frost'. However, neither 'Sprat' nor 'Frost' is part of the match results.


# x(?!y) Matches 'x' only if 'x' is not followed by 'y'. This is called a negated lookahead.
# For example, /\d+(?!\.)/ matches a number only if it is not followed by a decimal point. The regular expression /\d+(?!\.)/.exec("3.141") matches '141' but not '3.141'.

# (?:x) Matches 'x' but does not remember the match. The parentheses are called non-capturing parentheses,



# Arrays
# Arrays are container-like values that can hold other values. The values inside an array are called elements
# var array = [100, "paint", [200, "brush"], false];
# array[array.length - 1] = "yellow"

# be careful, this add property to the array, instead of an array element
# array[3.4] = 'orange';


# length
# array.length
# Writing a value that is shorter than the number of stored items truncates the array;
# writing 0 empties it entirely
# array['length'] = 3

# let cats = [];
# cats[30] = ['Dusty'];
# cats.length;				// 31


# // concat method - returns a new array that combines the values of two arrays.
# var new_array = ["tortilla chips"].concat(["salsa", "queso", "guacamole"]);

# // joins all elements of an array into a string
# ['red', 'green', 'blue'].join('-'); 		// "red-green-blue"

# // pop method - removes the last element in the array and returns that element’s value
# ["Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"].pop();

# // push method - adds an elements to the array and returns the array’s length
# ["John", "Kate"].push('Jill', 'Ivy');

# // shift method removes the first element from an array and returns that element
# ["1", "2", "3"].shift(); 						// 1

# // unshift method adds one or more elements to the front of an array and returns the new length of the array
# ["1", "2", "3"].unshift("-1", "0"); 			// ["0", "-1", "1", "2", "3"]

# // slice method extracts a section of an array and returns a new array
# ["a", "b", "c", "d", "e"].slice(1, 4);			// [ "b", "c", "d"]

# // splice(index, count_to_remove, addElement1, addElement2, ...)
# removes elements from an array and (optionally) replaces them.
# It returns the items which were removed from the array
# ["1", "2", "3", "4", "5"].splice(1, 3, "a", "b", "c", "d");

# // map method returns a new array of the return value from executing callback on every array item
# ['a', 'b', 'c'].map(item => item.toUpperCase()); 							// ['A', 'B', 'C']

# // filter method returns a new array containing the items for which callback returned true
# ['a', 10, 'b', 20, 'c', 30].filter(item => typeof item === 'number'); 	// [10, 20, 30]

# // reduce method applies callback(firstValue, secondValue) to reduce the list of items down to a single value
# [10, 20, 30].reduce((first, second) => first + second, 0);				// 60

# // sort method sorts the elements of an array
# ["Wind", "Rain", "Fire"].sort();

# // reverse method - returns a copy of the array in opposite order
# ["a", "b", "c"].reverse();



# iterating over arrays
# var colors = ['red', 'green', , 'blue'];

# for(let i of colors) {
#   console.log(i);			// 'red', 'green', undefined, 'blue'
# }

# elements of array omitted when the array is defined are not listed when iterating by forEach
# colors.forEach(function(color) {
#   console.log(color); 	// 'red', 'green', 'blue'
# });



# Sets
# Set objects are collections of values. You can iterate its elements in insertion order.
# A value in a Set may only occur once; it is unique in the Set's collection
# let mySet = new Set();
# mySet.add(1);
# mySet.add("some text");
# mySet.add("foo");

# mySet.has(1);			// true
# mySet.delete("foo");
# mySet.size;			// 2

# for (let item of mySet) {
# 	console.log(item);
# }



# Objects
# Object literal
# var myHonda = {color: "red", wheels: 4, engine: {cylinders: 4, size: 2.2}};

# var myCar = new Object();
# myCar.make = "Ford";
# myCar.model = "Mustang";
# myCar['year'] = 1969;

# Enumerate the properties of an object
# for (let i in myCar) {
# 	console.log(i);
# }

# or
# Object.getOwnPropertyNames(myCar);



# Prototype
# function Person(name, sex) {
# 	this.name = name;
# 	this.sex = sex;
# }

# var rand = new Person("Rand McKinnon", "M");
# var ken = new Person("Ken Jones", "M");

# The following code adds a age property to all objects of type person
# Person.prototype.age = 20;

# adding new method to Person object
# Person.prototype.fullName = function() {
# 	return `${this.name} ${this.sex}`;
# };

# !
# Person.prototype is an object shared by all instances of Person.
# It forms part of a lookup chain (that has a special name, "prototype chain"):
# any time you attempt to access a property of Person that isn't set,
# JavaScript will check Person.prototype to see if that property exists there instead.
# As a result, anything assigned to Person.prototype becomes available to all instances
# of that constructor via the this object.

# add things to the prototype of built-in JavaScript objects
# String.prototype.reversed = function reversed() {
# 	let r = "";
# 	for (let i = this.length - 1; i >= 0; i--) {
# 		r += this[i];
# 	}
# 	return r;
# };

# 'Ivy'.reversed()



# As mentioned before, the prototype forms part of a chain.
# The root of that chain is Object.prototype, whose methods include toString()
# — it is this method that is called when you try to represent an object as a string.
# This is useful for debugging our Person objects:

# var s = new Person("Simon", "M");
# s; // [object Object]

# Person.prototype.toString = function() {
#   return '<Person: ' + this.fullName() + '>';
# }

# s.toString(); // "<Person: Simon M>"



# call and apply
# apply() has a sister function named call, which again lets you set this but takes
# an expanded argument list as opposed to an array.

# theFunction.apply(valueForThis, arrayOfArgs)
# theFunction.call(valueForThis, arg1, arg2, ...)

# function lastNameCaps() {
# 	return this.last.toUpperCase();
# }
# var s = new Person("Simon", "Willison");
# lastNameCaps.call(s);
# // Is the same as:
# s.lastNameCaps = lastNameCaps;
# s.lastNameCaps();



# Using this for object references
# In general, 'this' refers to the calling object in a method
# <input type="text" name="age" size="3" onChange="validate(this, 18, 99)">



# Comparing Objects
# In JavaScript objects are a reference type. Two distinct objects are never equal,
# even if they have the same properties. Only comparing the same object reference
# with itself yields true





# Iterators
# In JavaScript an iterator is an object that provides a next() method which returns
# the next item in the sequence. This method returns an object with two properties:
# done and value
# function makeIterator(array){
#     var nextIndex = 0;
	
#     return {
#        next: function(){
#            return nextIndex < array.length ?
#                {value: array[nextIndex++], done: false} :
#                {done: true};
#        }
#     }
# }
# var it = makeIterator(['yo', 'ya']);
# it.next().value; // 'yo'
# it.next().value; // 'ya'
# it.next().done;  // true



# Generators
# A generator is a special type of function that works as a factory for iterators.
# A function becomes a generator if it contains one or more yield expressions
# and if it uses the function* syntax
# function* idMaker(){
# 	console.log('Start');
# 	var index = 0;
# 	while(true)
# 		yield index++;
# }

# var gen = idMaker();
# gen.next().value; // 0
# gen.next().value; // 1
# gen.next().value; // 2



# Iterables
# In order to be iterable, an object must implement the @@iterator method,
# meaning that the object (or one of the objects up its prototype chain)
# must have a property with a Symbol.iterator key

# built-in iterables: String, Array, TypedArray, Map, Set

# var myIterable = {
#   container: ['a', 'b', 'c'],
#   [Symbol.iterator]: function*() {
#    yield* this.container;				// yield from ?
#   }
# };

# for (let i of myIterable) {
#   ...
# }
# or(unpacking)
# [...myIterable]



# Send to yield
# A value passed to next() will be treated as the result of the last yield expression
# that paused the generator
# function* seq() {
# 	let result = 0;
# 	while(true) {
# 		let current = yield result++;
# 		if(current) {
#     		result = current;
#     	}
#   	}
# }

# a = seq();
# a.next().value;
# a.next(10).value;
# a.next().value;

# Generators have a return(value) method that returns the given value and finishes the generator itself



# Class
# JavaScript classes are syntactical sugar over JavaScript's existing prototype-based inheritance.
# The class syntax is not introducing a new object-oriented inheritance model to JavaScript.
# JavaScript classes provide a much simpler and clearer syntax to create objects and deal with inheritance.

# let log = console.log;

# class Polygon {
# 	constructor(height, width) {
# 		this.height = height;
# 		this.width = width;
# 	}
	
# 	toString() {
# 		return `Polygon (${this.height}x${this.width})`;
# 	}
#   // property
# 	get area() {
# 		return this.callArea();
# 	}
	
# 	callArea() {
# 		return this.height*this.width;
# 	}
# 	// Static methods are called without instantiating their class and are also not callable when the class is instantiated.
# 	static diagonal(x, y) {
# 		return Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2));
# 	}
# }

	
# // inheritance
# class Square extends Polygon {
# 	toString() {
# 		// The super keyword is used to call functions on an object's parent
# 		log(super.toString()); // 'Polygon (7x3)'
# 		return `Square (${this.height}x${this.width})`;
# 	}
# }	

	
# let p = new Polygon(185, 90);
# log(p, p.toString());
# log(p.area, p.callArea())
# log(Polygon.diagonal(3, 4));


# let s = new Square(7, 3);
# log(s, s.toString());
# log(s.area, s.callArea())
# log(Square.diagonal(6, 8));


# var li = [' cherries', ' oranges', ' apples', ' bananas'];
# li.forEach(function(elmnt,indx,arry) {
# 	arry[indx] = elmnt.trim();
# });

# 16
