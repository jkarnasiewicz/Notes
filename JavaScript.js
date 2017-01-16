// GENERAL
// json - JavaScript Object Notation
// Shift + F4 open scratchpad in firefox

// JavaScript is a dynamically and weak typed language
// That means you dont have to specify the data type of a variable when you declare it, and data
// types are converted automatically as needed during script execution

// Scope in a programming language controls the visibility and lifetimes of variables and parameters

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
// However, variables that are hoisted will return a value of undefine



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



// List of all the methods in object
console.log(Object.getOwnPropertyNames(obj));

// View list of all JavaScript variables
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



// Using the arguments
function myConcat(separator) {
	let result = "";
	for (let i = 1; i < arguments.length; i++) {
		result += arguments[i] + separator;
	}
	return result;
}

myConcat(", ", "red", "orange", "blue");



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

// elements of array omitted when the array is defined are not listed when iterating by forEach
colors.forEach(function(color) {
	console.log(color); 			// 'red', 'green', 'blue'
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





// NUMBERS - Js numbers are 64-bit floating numbers
// +Infinity, -Infinity, and NaN
// Internationalization - Intl object is the namespace for the ECMAScript Internationalization API
var myNumber = Number("55");
if ( isNaN(myNumber) ) {
	console.log("It's not a number!");
}
// double negative - if NOT NOT a number
if ( !isNaN(myNumber) ) {
	console.log("It is a number!");
}



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





// STRINGS
// String literals 				"John's \n cat"

// var str = "this string \
// is broken \
// across multiple\
// lines."

// Template literals
// var name = "Bob", time = "today";
// `Hello ${name}, how are you ${time}?`


var phrase = "Don't mix your quotes.";
var phrase = "He said \"that's fine,\" and left. \u00A9";

phrase.toUpperCase();			// toLowerCase
phrase.concat('?!');
phrase.trim();					// trims whitespace from the beginning and end of the string
phrase.split(" ");
phrase.indexOf("fine");			// it returns -1 if the term is not found
phrase.slice(6, 5);				// find element with index 6, and get 5 characters from that element(included)

var str1 = "aardvark";
var str2 = "beluga";

// template literals
var a = 5, b = 10;
`Fifteen is ${a + b} and\n not ${2 * a + b}.`

if (  str1 < str2 ) { ... } 				// true

var str1 = "aardvark";
var str2 = "Beluga";

if (  str1 < str2 ) { ... } 				// false (Ascii table)





// REGULAR EXPRESSIONS
// RegExp literals 				var re = /ab+c/;

var myRE = /d(b+)d/g;					// g - global option, i - case-insensitive search, m - multi-line search
var myRE = new RegExp("d(b+)d", "g");
var myRe = new RegExp(/Integration Time \(usec\): (\d+) \(HR2B085\)/g);
var myString = "cdbbdbsb dbd";

// regexp methods
myRE.test(myString);					// return true or false

myRE.exec(myString);					// return array with first occurence of the regexp: ['dbbd', 'bb']
myRE.exec(myString);					// return next occurrence: ['dbd', 'b']

// regexp property
myRE.lastIndex;

// string methods
myString.match(myRE);					// returns an array of information or null on a mismatch: ["dbbd", "dbd"]
myString.search(myRE);					// returns the index of the match, or -1 if the search fails
myString.split(/db+d/);					// break a string into an array of substrings: ["c", "bsb ", ""]
myString.replace(myRE, new_string);		// replaces the matched substring with a replacement substring: 'c#bsb #'
// or
var re = /(\w+)\s(\w+)/;
var myString = "John Smith";
myString.replace(re, "$2, $1");

// example
var re = /(?:\d{3}|\(\d{3}\))([-\/\.])\d{3}\1\d{4}/; 	// \1 is one of the rememberd characters from [-\/\.]


/^hello/								// ^ at the start
/hello$/								// $ at the end
/hel+o/									// + "l" must appear once or more
/hel*o/									// * "l" must appear zero or more
/hel?o/									// ? "l" must appear zero or one
/hello|goodbye/							// | either/or
/he..o/									// . any character
/\wello/								// \w alphanumeric or _
/\bhello/								// \b word boundary, before hello must be space or new line
/[crnld]ope/							// [...] range of chars





// OBJECT CREATION
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



// Enumerate the properties of an object
for (let i in myCar) {
	console.log(i);
}

// or
Object.getOwnPropertyNames(myCar);





// PROTOTYPES
function Player(n, s, r) {
	this.name = n;
	this.score = s;
	this.rank = r;
}

Player.prototype.logInfo = function() {
	console.log("I am:", this.name);
};

Player.prototype.promote = function() {
	this.rank++;
	console.log("My new rank is:", this.rank);
};

var john = new Player("John", 5000, 3);
john.logInfo();
john.promote();





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
setTimeout(someFunction, 5000);					// trigger only once
setTimeout(function(){window.location.reload()}, 1000);
setInterval(someFunction, 5000);				// call function every 5 second

// Stop timer/Clear Interval
var intervalHandler = setInterval(changeImage, 3000;

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





// DOM - Document Object Model
var mainTitle = document.getElementById("mainTitle");
var myLinks = mainTitle.getElementsByTagName("a");

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
<input type="text" name="age" size=3 onChange="document.writeln(this.value);">






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



















// TO DO

// "use strict";

// Minification Tools: JSMin, YUI Compressor, Google Closure Compiler

// Code Quality Tool: JSLint

// JavaScript Libraries:
Google Closure Library
Mootools
Dojo
OpenLayer


// ==============================================
var searchString = "Now is the time and this is the time and that is the time";
var pattern = /t\w*e/g;
var matchArray;

// check for pattern with regexp exec, if not null, process
while((matchArray = pattern.exec(searchString)) != null) {
  console.log(matchArray);
  console.log(matchArray.index);
  console.log(matchArray.input);
  console.log(matchArray[0]);
  console.log(matchArray.length);
  console.log(Object.getOwnPropertyNames(matchArray));
  console.dir(matchArray);
}
// ==============================================

var pieceOfHtml = "<p>This is a <span>paragraph</span></p>";
pieceOfHtml = pieceOfHtml.replace(/</g,"&lt;");

// ==============================================
^ Matches beginning of input /^This/ matches This is...
$ Matches end of input /end$/ matches This is the end
* Matches zero or more times /se*/ matches seeee as well as se
? Matches zero or one time /ap?/ matches apple and and
+ Matches one or more times /ap+/ matches apple but not and
{n} Matches exactly n times /ap{2}/ matches apple but not apie
{n,} Matches n or more times /ap{2,}/ matches all p’s in apple and appple but not apie
{n,m} Matches at least n, at most m times /ap{2,4}/ matches four p’s in apppppple
. Any character except newline /a.e/ matches ape and axe
[...] Any character within brackets /a[px]e/ matches ape and axe but not ale
[^...] Any character but those within brackets /a[^px]/ matches ale but not axe or ape
\b Matches on word boundary /\bno/ matches the first no in nono
\B Matches on nonword boundary /\Bno/ matches the second no in nono
\d Digits from 0 to 9 /\d{3}/ matches '123' in 'Now in 123'
\D Any nondigit character /\D{2,4}/ matches 'Now' in 'Now in 123';
\w Matches word character (letters, digits, underscores) /\w/ matches j in javascript
\W Matches any nonword character (not letters, digits, \/W/ matches % in 100%
  or underscores)
\n Matches a line feed
\s A single whitespace character
\S A single character that is not whitespace
\t A tab
(x) Capturing parentheses
Remembers the matched characters




//
eval
bind
indexOf
fadeTo




// Metoda stringify przeprowadza konwersję obiektu JavaScript na ciąg tekstowy
JSON.stringify(results, null, 4)

// Metoda parse przetwarza ciąg tekstowy zawierający dane JSON na postać obiektu JavaScript
JSON.parse()

window.variable_name - gwarantuje pobranie obiektu globalnego
