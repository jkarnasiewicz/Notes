# -*- coding: utf-8 -*-
# raise from lambda !

# import shelve

# !!! check import order in metaprograming chapter

# I haven’t yet found a language that manages to be easy for beginners,
# practical for professionals and exciting for hackers in the way that Python is

# 'Only those who work make mistakes' - great advice to avoid being paralyzed by
# the fear of making errors

# 717 python jargon


a = [4]

def f(a):
	a.append(3)
	return a


print(f(a), a)
# print(f(a))
# print(a)





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
