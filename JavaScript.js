// GENERAL
// json - JavaScript Object Notation
// Shift + F4 open scratchpad in firefox
// url: about:config - firefox’s advanced settings

// JavaScript is a dynamically and weak typed language
// That means you dont have to specify the data type of a variable when you declare it, and data
// types are converted automatically as needed during script execution

// Scope in a programming language controls the visibility and lifetimes of variables and parameters


// Strict mode is more restricted version of the JavaScript language
// (typos in variable names in assignment throw an error, assignments that would normally fail quietly
// now throw an error, attempting to delete an undeletable property fails, using nonunique property names,
// using nonunique function parameter names)
'use strict';

// Global variables
// Global variables are in fact properties of the global object. In web pages the global object
// is window, so you can set and access global variables using the window.variable syntax

// JavaScript, blocks do not have scope; only functions have scope starting with ECMAScript
// Edition 6, let and const declarations allow you to create block-scoped variables

// Let, Const and Var
// let and const(read-only) allows you to declare variables that are limited in scope to the
// block, statement, or expression on which their are used. This is unlike the var keyword, which
// defines a variable globally, or locally to an entire function regardless of block scope

var a = 1;
var b = 2;

if (a === 1) {
	var a = 11; // the scope is global
	let b = 22; // the scope is inside the if-block

	console.log(a);  	// 11
	console.log(b);  	// 22
} 

console.log(a); 		// 11
console.log(b); 		// 2

// At the top level of programs and functions, let, unlike var, does not create a property on
// the global object(window):
var x = 'global';
let y = 'global';
console.log(this.x); // "global"
console.log(this.y); // undefined

// Constants
// You can create a read-only, named constant with the const keyword, const PI = 3.14;
// A constant cannot change value through assignment or be re-declared while the script is
// running. It has to be initialized to a value

// Hoisting
// Another unusual thing about variables in JavaScript is that you can refer to a variable
// declared later, without getting an exception. This concept is known as hoisting; variables
// in JavaScript are in a sense "hoisted" or lifted to the top of the function or statement
// (the top of their current scope). However, variables that are hoisted will return a value
// of undefine
console.log(a); // undefined
var a = 1;



// A function always returns a value. If the return value is not specified, then undefined is returned

// New
// You can use the 'new' operator to create an instance of a user-defined object type or of one of
// the built-in object types. Use new as follows:
// var objectName = new objectType([param1, param2, ..., paramN]);

// If the function was invoked with the new prefix and the return value is not an object, then this
// (the new object) is returned instead



// literal - notations for atomic values
// In computer science, a literal is a notation for representing a fixed value in source code
// Almost all programming languages have notations for atomic values such as integers,
// floating-point numbers, and strings, and usually for booleans and characters;
// some also have notations for elements of enumerated types and compound values such as
// arrays, records, and objects. An anonymous function is a literal for the function type

// A JavaScript primitive is an instance of a particular data type, and there are five such in
// the language: String, Number, Boolean(true or false), null, and undefined

// 'hello' === new String('hello') => false, literal(typeof => string) vs primitive(typeof => object)



// Comparing Objects
// In JavaScript objects are a reference type. Two distinct objects are never equal, even if they
// have the same properties. Only comparing the same object reference with itself yields true



// Be careful
// Calling function with different numbers of arguments
// don't use ==/!=, console.log('' == '0',  0 == '', 0 == '0');
// console.log([] == [], [] == 0, false == [], !![0], !![1], 1 == [[1]], 0 == [[0]], ['010'] - [4]);
// '3' + [1, 4]; 				// '31,4'
// typeof NaN === 'number'		// true
// NaN === NaN 					// false
// var t1 = new Date(), t2 = new Date(); 
// The Date instance subtraction operator returns miliseconds, but ! sum returns concatenated string
// Global Variables
// Semicolon Insertion


// List of all the properties in object
Object.getOwnPropertyNames(obj);
// or
console.dir(obj);

// View list of all JavaScript properties
for(var b in window) { 
	if(window.hasOwnProperty(b)) console.log(b); 
}





// BUILT-IN
// typeof operator returns a string indicating the type of the unevaluated object
typeof obj
// typeof myFun;         	// returns "function"
// typeof "round";       	// returns "string"
// typeof 4;        	    // returns "number"
// typeof new Date();    	// returns "object"
// typeof doesntExist;   	// returns "undefined"
// typeof true; 		    // returns "boolean"
// typeof null; 		    // returns "object"

// function parses a string argument and returns an integer of the specified radix
parseInt("11", 2);				// 3

// function parses a string argument and returns a floating point number
parseFloat('2.718');			// 2.718

// function evaluates JavaScript code represented as a string
eval("2 + 2");             		// returns 4

// method returns a string representing the object
obj.toString()







// CONDITIONAL STATEMENTS
if (time < 10) {
	greeting = "Good morning";
}
else if (time < 20) {
	greeting = "Good day";
}
else {
	greeting = "Good evening";
}

// Ternary, condition ? true : false
var ter = ( a > b ) ? a : b;





// LOOPS
// while
var a = 1;
while (a < 10) {
	console.log(a)
	a++
}



// do...while loop will always happen at least once
do {
	console.log(a);
	a++
}
while (a < 10);



// for
var node = document.nameForm.nameSelect				// after dot, named attributes of the tags
for (var i = 1; i < node.options.length; i++) {
	if(node.options[i].selected) {
		numberSelected++;
	}
}


let arr = [3, 5, 7];
arr.foo = "hello";
// The for...in statement iterates a specified variable over all the enumerable properties of an object
for (let i in arr) {
	console.log(i);	// logs "0", "1", "2", "foo"
}



// The for...of statement creates a loop Iterating over iterable objects(including Array, Map, Set, arguments object),
// invoking a custom iteration hook with statements to be executed for the value of each distinct property
for (let i of arr) {
	console.log(i); // logs 3, 5, 7
}



// The switch statement can be used for multiple branches based on a number or string
switch(action) {
	case 'draw':
		drawIt();
		break;
	case 'eat':
		eatIt();
		break;
	default:
		doNothing();
}



break;					// break jumps out of the loop
continue;				// done with this iteration





// OPERATORS
<=						// less or equal to
>=						// greater or equal to
=						// assigment
==						// equal
!=						// not equal
===						// strict equality(checking the value and the type)
+=, -=					// increment/decrement
++a, a++ 				// adding 1 (prefix, postfix)
// If a is 3, then ++a sets a to 4 and returns 4, whereas a++ returns 3 and, only then, sets a to 4

// Modulus(reszta z dzielenia)
2003 % 4				// remainder is 3

// Logical operators
&&						// and
||						// or
!						// not

// Bitwise operators
15 & 9 	9 			// and, 1111 & 1001 = 1001
15 | 9 	15 			// or, 1111 | 1001 = 1111

// Delete
delete objectName.property;



// in - propNameOrNumber in objectName
var trees = ["redwood", "bay", "cedar", "oak", "maple"];
0 in trees;        	// returns true
6 in trees;        	// returns false
"bay" in trees;    	// returns false (you must specify the index number, not the value at that index)
"length" in trees; 	// returns true (length is an Array property)
"PI" in Math;       // returns true

var mycar = { make: "Honda", model: "Accord", year: 1998 };
"make" in mycar;  	// returns true



// instanceof
// The instanceof operator returns true if the first object is instance of the second one
// objectName instanceof objectType
var theDay = new Date(1995, 12, 17);
if (theDay instanceof Date) {
	// statements to execute
}






// EXCEPTION
try {
	throw "myException";	// generates an exception
}
catch (e) {
	// statements to handle any exceptions
	log(e);					// pass exception object to error handler
}
finally {
	log("finally over");
}





// NUMBERS - Js numbers are 64-bit floating numbers
// +Infinity, -Infinity, and NaN
// Internationalization - Intl object is the namespace for the ECMAScript Internationalization API

// A decimal number can be converted to another radix, in a range from 2 to 36
var decNum = 55;
var octNum = decNum.toString(8); 	// value of 67 octal
var hexNum = decNum.toString(16); 	// value of 37 hexadecimal
var binNum = decNum.toString(2); 	// value of 110111 binary

// Convert degrees to radians
var radians = degrees * (Math.PI / 180);
// Length of a circular arc - multiplying the circle’s radius times the angle of the arc in radians
var arclength = radius * radians;



// Math object
Math.PI;
Math.round(200.67);
Math.max(a, b, c);
Math.min(a, b, c);
Math.random();
Math.floor((Math.random() * 100) + 1);
Math.pow(2, 4);
Math.sqrt(4);
Math.log(x);		// lnx
Math.exp(x);    	// e**x

// isNaN
var myNumber = Number("55");
if ( isNaN(myNumber) ) {
	console.log("It's not a number!");
}
// double negative - if NOT NOT a number
if ( !isNaN(myNumber) ) {
	console.log("It is a number!");
}





// STRINGS

// String literals
var phrase = "Don't mix your quotes.";

// String object
var phrase = String("He said \"that's fine,\" and left. \u00A9");

// Template literal
var name = "Bob", time = "today";
`Hello ${name}, how are you ${time}?`

var a = 5, b = 10;
`Fifteen is ${a + b} and\n not ${2 * a + b}.`

// String methods
phrase.toUpperCase();			// or toLowerCase()
phrase.concat('?!');			// combines the text of one or more strings and returns a new string
phrase.trim();					// returns a copy of the string with beginning and ending whitespace characters removed
phrase.split(" ");
phrase.indexOf("fine");			// it returns -1 if the term is not found
phrase.slice(6, 10);			// find element with index 6, and get all characters up to index 10(last one not included)

phrase.startsWith('Don\'t', 0); // optional integer as second parameter - where begin the search
phrase.endsWith('quotes.');		// optional integer as second parameter - where terminate the search
phrase.contains('mix');			// shim needed, <script type="text/javascript" src="es6-shim.js"></script>

// String comparison
var str1 = "aardvark";
var str2 = "beluga";
if (  str1 < str2 ) { ... } 				// true


var str1 = "aardvark";
var str2 = "Beluga";
if (  str1 < str2 ) { ... } 				// false (Ascii table)





// JSON
// JSON.stringify() method converts a JavaScript value to a JSON string, optionally replacing
// values if a replacer function is specified, or optionally including amount of spaces
JSON.stringify([1, 'false', false], null, 4)

// JSON.parse() method parses a JSON string, constructing the JavaScript value or object described
// by the string
JSON.parse('[1, 5, "false"]')





// REGULAR EXPRESSIONS

// RegExp literals
var myRE = /d(b+)d/g;		// g - global option, i - case-insensitive search, m - multi-line search

// RegExp object
var myRE = new RegExp("d(b+)d", "g");
var myRe = new RegExp(/Integration Time \(usec\): (\d+) \(HR2B085\)/g);
var myString = "cdbbdbsb dbd";

// regexp property
myRE.lastIndex;

// regexp methods
myRE.test(myString);					// return true or false

myRE.exec(myString);					// return array with first occurence of the regexp: ['dbbd', 'bb']
myRE.exec(myString);					// return next occurrence: ['dbd', 'b']

// check for pattern with regexp exec, if not null, process
while((matchArray = pattern.exec(searchString)) != null) {
	console.log(matchArray);
	console.log(matchArray.index);								// The index of the located match
	console.log(matchArray.input);								// The original input string
	console.log(matchArray[0]);									// The matched value, or [1],…,[n]+ for parenthesized substring matches, if any
	console.log(matchArray.length);
	console.log(Object.getOwnPropertyNames(matchArray));
	console.dir(matchArray);
}



// string methods
myString.match(myRE);					// returns an array of information or null on a mismatch: ["dbbd", "dbd"]
myString.search(myRE);					// returns the index of the match, or -1 if the search fails
myString.split(/db+d/);					// break a string into an array of substrings: ["c", "bsb ", ""]
myString.replace(myRE, new_string);		// replaces the matched substring with a replacement substring: 'c#bsb #'

// or
var re = /(\w+)\s(\w+)/;
var myString = "John Smith";
myString.replace(re, "$2, $1");			// other patterns: $& inserts matched substring

/^hello/								// ^ matches beginning of input, matches hello...
/hello$/								// $ matches end of input
/hel+o/									// + "l" must appear once or more
/hel*o/									// * "l" must appear zero or more
/hel?o/									// ? "l" must appear zero or one
/hello|goodbye/							// | either/or
/he..o/									// . any character
/\wello/								// \w alphanumeric or _
/\bhello/								// \b word boundary, before hello must be space or new line
/[crnld]ope/							// [...] range of chars
/[^crnld]ope/							// any character but those within brackets range
/ap{2}/									// matches exactly 2 times, matches apple but not apie
/ap{2,}/								// matches 2 or more times,  matches all p’s in apple and appple but not apie
/ap{2,4}/								// matches at least 2, at most 4 times, matches four p’s in apppppple => "apppp"



// Lookahead
x(?=y) 	Matches 'x' only if 'x' is followed by 'y'
For example, /Jack(?=Sprat)/ matches 'Jack' only if it is followed by 'Sprat'

/Jack(?=Sprat|Frost)/ matches 'Jack' only if it is followed by 'Sprat' or 'Frost'
However, neither 'Sprat' nor 'Frost' is part of the match results.


// Negated lookahead
x(?!y) Matches 'x' only if 'x' is not followed by 'y'
For example, /\d+(?!\.)/ matches a number only if it is not followed by a decimal point
The regular expression /\d+(?!\.)/.exec("3.141") matches '141' but not '3.141'

// Capturing parentheses
(x) Matches 'x' and remember the match

// Non-capturing parentheses
(?:x) Matches 'x' but does not remember the match



// Replacing harmful signs
var pieceOfHtml = "<p>This is a <span>paragraph</span></p>";
pieceOfHtml = pieceOfHtml.replace(/</g,"&lt;");



// Example with remembered group
// \1 is one of the rememberd characters from [-\/\.]
var re = /(?:\d{3}|\(\d{3}\))([-\/\.])\d{3}\1\d{4}/;



// Example with 'while'
var searchString = "Now is the time and this is the time and that is the time";
var pattern = /t\w*e/g;
var matchArray;





// ARRAYS
// Arrays are container-like objects that can hold other values. The values inside an array are
// called elements

// Array literal
var array = [100, "paint", [200, "brush"], false];
array[array.length - 1] = "yellow"

// Be careful, using non integer index adds property to the array, instead of an array element
array[3.4] = 'orange';


// array.length - last index of the array+1
// Writing a value that is shorter than the number of stored items truncates the array, writing 0
// empties it entirely
array['length'] = 3

let cats = [];
cats[30] = ['Dusty'];
cats.length;				// 31



// concat method - returns a new array that combines the values of two arrays.
var new_array = ["tortilla chips"].concat(["salsa", "queso", "guacamole"]);

// joins all elements of an array into a string
['red', 'green', 'blue'].join('-'); 									// "red-green-blue"

// indexOf(searchElement, fromIndex) method returns the first index at which a given element can be found in the array, or -1 if it is not present
[1, 3, 7, 11, 3].indexOf(3, 2);											// 4

// pop method - removes the last element in the array and returns that element’s value
["Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"].pop();

// push method - adds an elements to the array and returns the array’s length
["John", "Kate"].push('Jill', 'Ivy');

// shift method removes the first element from an array and returns that element
["1", "2", "3"].shift(); 												// 1

// unshift method adds one or more elements to the front of an array and returns the new length of the array
["1", "2", "3"].unshift("-1", "0"); 									// ["-1", "0", "1", "2", "3"]

// slice method extracts a section of an array and returns a new array
["a", "b", "c", "d", "e"].slice(1, 4);									// [ "b", "c", "d"]

// splice(index, count_to_remove, addElement1, addElement2, ...)
// removes elements from an array and (optionally) replaces them
// it returns the items which were removed from the array
["1", "2", "3", "4", "5"].splice(1, 3, "a", "b", "c", "d");

var charSets = ["ab","bb","cd","ab","cc","ab","dd","ab"];
// replace all occurrence of the element
while (charSets.indexOf("ab") != -1) {
	charSets.splice(charSets.indexOf("ab"), 1, "**");		// ["**", "bb", "cd", "**", "cc", "**", "dd", "**"]
}
// delete all new element
while(charSets.indexOf("**") != -1) {
	charSets.splice(charSets.indexOf("**"), 1); 			// ["bb", "cd", "cc", "dd"]
}

// map method returns a new array of the return value from executing callback on every array item
['a', 'b', 'c'].map(item => item.toUpperCase()); 						// ['A', 'B', 'C']

// filter method returns a new array containing the items for which callback returned true
['a', 10, 'b', 20, 'c', 30].filter(item => typeof item === 'number'); 	// [10, 20, 30]

// reduce method applies callback(firstValue, secondValue) to reduce the list of items down to a single value
[10, 20, 30].reduce((first, second) => first + second, 0);				// 60

// sort method sorts the elements of an array
["Wind", "Rain", "Fire"].sort();

// reverse method - returns a copy of the array in opposite order
["a", "b", "c"].reverse();



// iterating over arrays
var colors = ['red', 'green', , 'blue'];

for(let i of colors) {
	console.log(i);					// 'red', 'green', undefined, 'blue'
}

// elements of array omitted when the array is defined are not listed when iterating by forEach(modifies an array)
colors.forEach(function(element, index, array) {
	console.log(element); 			// 'red', 'green', 'blue'
	array[index] = element.toUpperCase();

});



// Comprehensions
// Array comprehensions: [for (x of y) function(x)]
var abc = [ "A", "B", "C" ];
[for (letters of abc) letters.toLowerCase()]; 	// [ "a", "b", "c" ]

// Generator comprehensions: (for (x of y) y)





// SETS
// Set objects are collections of values. You can iterate its elements in insertion order. A value
// in a Set may only occur once; it is unique in the Set's collection
let mySet = new Set();
mySet.add(1);
mySet.add("some text");
mySet.add("foo");

mySet.has(1);			// true
mySet.delete("foo");
mySet.size;				// 2

for (let item of mySet) {
	console.log(item);
}





// DATES
var today = new Date();						// without 'new', get string representation of date
var day = new Date(1906, 11, 25, 6, 30, 0); // year, month, day, hour, minute, seconds
var Xmas95 = new Date("December 25, 1995 13:30:00");

// date methods
today.getMonth();				// returns 0-11
today.getFullYear();			// YYYY
today.getDate();				// 1-31 day of month
today.getDay();					// 0-6 day of week, where 0 == sunday
today.getHours();				// 0-23

today.getTime();				// milliseconds since 1/1/1970

today.setMonth(5);
today.setFullYear(2012);

day.setTime(Date.parse("Aug 9, 1995"));





// TIMERS
// setTimeout - trigger only once after 5 seconds
setTimeout(someFunction, 5000);
setTimeout(function(){window.location.reload()}, 1000);

// setInterval - call function every 5 seconds
setInterval(someFunction, 5000);

// Stop timer/Clear Interval
var intervalHandler = setInterval(changeImage, 3000);

myImage.onclick = function() {
	clearInterval(intervalHandler);
}

// Very simple slider
var image = document.getElementById('img-id');
var images = ['1.jpg', '2.png', '3.gif']
var index = 0;

function changeImage() {
  image.setAttribute("src", images[index]);
  index++
  if (index == 3) {
	index = 0;
  }
}

setInterval(changeImage, 3000);





// FUNCTIONS
function myFunction(x, y) {
	let myVar = x*y;
	return myVar;
}

myFunction(754, 346);



// Getting all the nodes of a tree structure(e.g. the DOM) using recursion
function walkTree(node) {
	if (node == null) {
		return;
	}
	if(node.nodeName === 'P') {
		node.style.color = "purple";
	}

	for (let i = 0; i < node.childNodes.length; i++) {
		walkTree(node.childNodes[i]);
	}
}

walkTree(document.body);



// Default parameters
function mul(a, b=1) {
	return a*b;
}

mul(5);



// Rest parameters/Spread syntax
// The spread operator allows an expression to be expanded in places where multiple arguments
// (for function calls) or multiple elements (for array literals) are expected
function multiply(multiplier, ...theArgs) {
	return theArgs.map(x => multiplier * x);
}

multiply(2, 1, 2, 3);			// [2, 4, 6]

// Unpacking
var parts = ['shoulder', 'knees'];
var lyrics = ['head', ...parts, 'and', 'toes'];



// Destructuring assignment(simplify array assignment)
var stateValues = [459, 144, 96, 34, 0, 14];
var [Arizona, Missouri, Idaho, Nebraska, Texas, Minnesota] = stateValues;
Missouri; 						// 144



// Using the arguments
function myConcat(separator) {
	let result = "";
	for (let i = 1; i < arguments.length; i++) {
		result += arguments[i] + separator;
	}
	return result;
}

myConcat(", ", "red", "orange", "blue");



// Optional argument
var myObject = {
	value: 0,
	increment: function (inc) {
		this.value += typeof inc === 'number' ? inc : 1;
	}
};

myObject.increment( );
myObject.value 						// 1

myObject.increment(2);
myObject.value 						// 3



// Arrow functions
var a = ["Hydrogen", "Helium", "Lithium", "Beryllium"];
a.map(function(s){ return s.length }); 		// old
a.map(s => s.length); 						// new



// Lexical this
function Person(){
	this.age = 0;
	setInterval(() => {
		// |this| properly refers to the person object, dont need to use 'var self = this;'
		this.age++;
	}, 1000);
}

var p = new Person();



// Closure
// A closure is the combination of a function and the scope object in which it was created. Closures
// let you save state and have acces to the context in which was created
// Be careful - the magical this variable is very tricky in closures. They have to be used carefully,
// as what this refers to depends completely on where the function was called, rather than where it
// was defined.

function outside(x) {
	function inside(y) {
		return Math.pow(x, y);
	}
	return inside;
}

fn_inside = outside(3)
fn_inside(3);



// Disabling/hiding access to the name and sex variables
function createPet(name) {
	var sex;
  
	return {
		setName: function(newName) {
			name = newName;
		},
	
		getName: function() {
			return name;
		},
	
		getSex: function() {
			return sex;
		},
	
		setSex: function(newSex) {
			if(typeof newSex === "string" && (newSex.toLowerCase() === "male" || newSex.toLowerCase() === "female")) {
				sex = newSex;
			}
		}
	}
}

var pet = createPet("Vivie");
pet.getName();                  // Vivie

pet.setName("Oliver");
pet.setSex("male");

pet.getSex();                   // male
pet.getName();                  // Oliver





// OBJECTS
var player = new Object();

// adding properties
player.name = "Fred";
player.score = 10000;
player['rank'] = 1;

// or as a object literal
var player1 = { name: "Fred", score: 10000, rank: 1 };
var player2 = { name: "John", score: 9000, rank: 2 };

// Creating methods for objects
function playerDetails() {
	console.log(this.name + " has a rank of: " + this.rank + " and a score of " + this.score);
}

player1.Details = playerDetails;
player2.Details = playerDetails;

// and displaying results
player1.Details();
player2.Details();





// PROTOTYPES
function Person(name, sex) {
	this.name = name;
	this.sex = sex;
}

var rand = new Person("Rand McKinnon", "M");
var ken = new Person("Ken Jones", "M");

// Person.prototype is an object shared by all instances of Person. It forms part of a lookup
// chain (that has a special name, "prototype chain"): any time you attempt to access a property
// of Person that isn't set, javascript will check Person.prototype to see if that property exists
// there instead. As a result, anything assigned to Person.prototype becomes available to all
// instances of that constructor via the 'this' object

// Adding a age property to all objects of type person
Person.prototype.age = 20;

// Adding new method to Person objects
Person.prototype.fullName = function() {
	return `${this.name} ${this.sex}`;
};

rand.age;
ken.fullName();

// The prototype forms part of a chain. The root of that chain is Object.prototype, whose methods
// include toString() — it is this method that is called when you try to represent an object as a
// string. This is useful for debugging our Person objects

Person.prototype.toString = function() {
	return '<Person: ' + this.fullName() + '>';
}

ken.toString();



// Adding methods to the prototype of built-in JavaScript objects
String.prototype.reversed = function reversed() {
	let r = "";
	for (let i = this.length - 1; i >= 0; i--) {
		r += this[i];
	}
	return r;
};

'Ivy'.reversed()



// Call and Apply(using free function as a instance method)
// apply() has a sister function named call, which again lets you set this but takes an expanded
// argument list as opposed to an array

// theFunction.apply(valueForThis, arrayOfArgs)
// theFunction.call(valueForThis, arg1, arg2, ...)

function lastNameCaps() {
	return this.name.toUpperCase();
}

var s = new Person("Lee Ji Min", "W");
lastNameCaps.call(s);
// Is the same as:
s.lastNameCaps = lastNameCaps;
s.lastNameCaps();



// Flattening a Two-Dimensional Array
var flat = [].concat.apply([], [1, 2, [3, 4], [5, 6], 7, 8]);





// CLASS
// JavaScript classes are syntactical sugar over JavaScript's existing prototype-based inheritance
// The class syntax is not introducing a new object-oriented inheritance model to JavaScript
// JavaScript classes provide a much simpler and clearer syntax to create objects and deal with
// inheritance

class Polygon {
	constructor(height, width) {
		this.height = height;
		this.width = width;
	}
	
	toString() {
		return `Polygon (${this.height}x${this.width})`;
	}
	// property
	get area() {
		return this.callArea();
	}
	
	callArea() {
		return this.height*this.width;
	}
	// Static methods are called without instantiating their class and are also not callable when
	// the class is instantiated
	static diagonal(x, y) {
		return Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2));
	}
}

	
// Inheritance and super
class OtherPolygon extends Polygon {
	toString() {
		// The super keyword is used to call functions on an object's parent
		log('Calling super: ', super.toString()); 		// 'Polygon (7x3)'
		return `OtherPolygon (${this.height}x${this.width})`;
	}
}	


// Creating instances
let p = new Polygon(185, 90);
p.toString();
p.area
Polygon.diagonal(3, 4);


let op = new OtherPolygon(7, 3);
op.toString();
op.area;
OtherPolygon.diagonal(6, 8);





// ITERATORS, GENERATORS AND ITERABLES
// Iterators
// In JavaScript an iterator is an object that provides a next() method which returns the next
// item in the sequence. This method returns an object with two properties: done and value

function makeIterator(array){
	var nextIndex = 0;
	return {
	   next: function(){
		   return nextIndex < array.length ?
			   {value: array[nextIndex++], done: false} :
			   {done: true};
	   }
	}
}

var it = makeIterator(['yo', 'ya']);
it.next().value; 		// 'yo'
it.next().value; 		// 'ya'
it.next().done;  		// true



// Generators
// A generator is a special type of function that works as a factory for iterators. A function
// becomes a generator if it contains one or more yield expressions and if it uses the function* syntax

function* idMaker(){
	console.log('Start');
	var index = 0;
	while(true)
		yield index++;
}

var gen = idMaker();
gen.next().value; 			// 0
gen.next().value; 			// 1
gen.next().value; 			// 2



// Iterables
// In order to be iterable, an object must implement the @@iterator method, meaning that the object
// (or one of the objects up its prototype chain) must have a property with a Symbol.iterator key

// built-in iterables: String, Array, TypedArray, Map, Set

var myIterable = {
	container: ['a', 'b', 'c'],
	[Symbol.iterator]: function*() {
		yield* this.container;				// like python yield from
	}
};

for (let i of myIterable) {
	i;										// a, b, c
}

// or(unpacking)
[1, 3, 5, ...myIterable]



// Send to yield
// A value passed to next() will be treated as the result of the last yield expression that paused
// the generator

function* seq() {
	let result = 0;
	while(true) {
		let current = yield result++;
		if(current) {
			result = current;
		}
	}
}

a = seq();
a.next().value;
a.next(10).value;
a.next().value;

// Generators have a return(value) method that returns the given value and finishes the generator itself





// PROMISE
function imgLoad(url) {
	return new Promise(function(resolve, reject) {
		var request = new XMLHttpRequest();
		request.open('GET', url);
		request.responseType = 'blob';
		request.onload = function() {
			if (request.status === 200) {
				resolve(request.response);
			}
			else {
				reject(Error('Image didn\'t load successfully; error code:' + request.statusText));
			}
		};
		request.onerror = function() {
			reject(Error('There was a network error.'));
		};
		request.send();
	});
}





// DOM - Document Object Model
var mainTitle = document.getElementById("mainTitle");
var myLinks = mainTitle.getElementsByTagName("a");
var thumbnails = document.getElementsByClassName('thumbnails');



// use querySelector to find all second table cells
var cells = document.querySelectorAll("td:nth-of-type(2)");
// convert to numbers, and sum the numbers
var sum = 0;
for (var i = 0; i < cells.length; i++) {
	sum+=parseFloat(cells[i].firstChild.data);
}



myLinks.length;
mainTitle.innerHTML;
mainTitle.nodeType;
mainTitle.childNodes.length;

myElement.style.display = "block" or "none";	// display or hide object
myElement.style.width = "230px";
myElement.style.color = "#ff0000";
myElement.style.left = "40px";
myElement.style.backgroundRepeat = "repeat-x";

myElement.className = "someCSSclass" or "";		// set css class to myElement

myElement.getAttribute("align");
myElement.setAttribute("align", "right");

// Creating DOM elements
var myNewElement = document.createElement("li");
var myText = document.createTextNode("New list item text");
myNewElement.appendChild(myText);
myNewElement.insertBefore(myNewElement, secondItem);
document.getElementById("sidebar").appendChild(myNewElement);


// Using this for object references
// In general, 'this' refers to the calling object in a method
<input type="text" name="age" size="3" onChange="validate(this, 18, 99)">
document.writeln(
	`<input type="text" name="age" size=3 onkeyup="document.writeln('<br>' + this.value);">`
);





// EVENTS
// Attach a event to the document
document.addEventListener("click", function(){			// document.removeEventListener
	document.body.style.backgroundColor = "red";
});

window.onload = function() {					// Page fully loaded
	prepareEventHandlers();
}

function prepareEventHandlers() {
	myNewImage.onclick = function() {			// Anonymous function
		alert("You clicked the image");
	}
}


someField.onfocus = function() {
	if (someField.value == "something") {
		someField.value = "";
	}
};
someField.onblure = function() {
	if ( someField.value == "") {
		someField.value = "your something!";
	}
};
someField.onchnage = function() {
	...
}
someField.onkeypress
someField.onkeydown
someField.onkeyup


// When clicking on a button, execute the first event handler, and
// stop the rest of the event handlers from being executed
event.stopImmediatePropagation()





// FORMS
document.forms.form_ID					// getting form by id=form_ID
document.forms.form_ID.input_id			// input object within the form
document.forms[0].elements[0];

textField.value;						// value of the text field
checkBox.checked;						// true or false

// Select-one
mySelect.selectedIndex;

// Select-multiple
mySelect.options[x].selectedIndex;		// check all the options

// Submit
someField.onsubmit = function() {
	...
	return false;						// to stop the form from submitting
}





// AJAX: Asynchronous JavaScript And XML
// Create the request
var myRequest;
// feature check
if (window.XMLHttpRequest) {
	myRequest = new XMLHttpRequest();
} else if (window.ActiveXObject) {
	myRequest = new ActiveXObject("Microsoft.XMLHTTP");
}
// create an event handler for our request to call back
myRequest.onreadystatechange = function() {
	console.log("We were called!");
	console.log(myRequest.readyState);
	if (myRequest.readyState === 4) {
		var p = document.createElement("p");
		var t = document.createTextNode(myRequest.responseText);
		p.appendChild(t);
		document.getElementById("mainContent").appendChild(p);
	}
};
// open and send it
myRequest.open('GET', 'simple.txt', true);
// any parameters
myRequest.send(null);





// RESIZE
window.onresize = function() {
	// window.innerHeight;
	// document.documentElement.clientWidth;
	// document.body.clientWidth;
};

window.onload = function() {
	...
};





// JavaScript Libraries
Google Closure Library
Mootools
Dojo
OpenLayer
Code Quality Tool, JSLint
Minification Tools: JSMin, YUI Compressor, Google Closure Compiler
