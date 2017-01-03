// General
// json - JavaScript Object Notation
// Shift + F4 open scratchpad in firefox

// Pass message into console
console.log('Message');
console.info('Info sign');
console.warn('Warrning');
console.error('Error!')

// Assigment to variable
var a = 5, b = "str";
var c = true, d = false;



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
var a = 1;
while (a < 10) {
	console.log(a)
	a++
}


do {					// do...while loop will always happen at least once
	console.log(a);
	a++
}
while (a < 10);


var node = document.nameForm.nameSelect				// after dot, named attributes of the tags
for (var i = 1; i < node.options.length; i++) {
	if(node.options[i].selected) {
		numberSelected++;
	}
}


let arr = [3, 5, 7];
arr.foo = "hello";
// The for...in statement iterates a specified variable over all the
// enumerable properties of an object
for (let i in arr) {
	console.log(i);	// logs "0", "1", "2", "foo"
}

// The for...of statement creates a loop Iterating over iterable objects(including Array, Map, Set, arguments object),
// invoking a custom iteration hook with statements to be executed for the value of each distinct property.
for (let i of arr) {
	console.log(i); // logs 3, 5, 7
}


break;					// break jumps out of the loop
continue;				// done with this iteration



// OPERATORS
!=						// is not
<=						// less or equal to
>=						// greater or equal to
=						// assigment
==						// equality(js is compile variable))
===						// strict equality(checking the value and the type)
+=, -=					// increment/decrement
++a, a++ 				// adding 1 (prefix, postfix)
// If a is 3, then ++a sets a to 4 and returns 4, whereas a++ returns 3 and, only then, sets a to 4.

// Modulus(reszta z dzielenia)
2003 % 4				// remainder is 3

// Logical operators
&&						// and
||						// or
!						// not



// FUNCTIONS
function myFunction(x, y) {
	var myVar = x*y;
	return myVar;
}

myFunction(754, 346);



// ARRAYS
var mulitpleValues = [50, 60, "Mia", true]

// Array propertise
mulitpleValues.length;

// Array methods
mulitpleValues.reverse();	// to call a method
mulitpleValues.join();
mulitpleValues.sort();



// NUMBERS - Js numbers are 64-bit floating numbers
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



// OBJECT CREATION
var player = new Object();

// properties
player.name = "Fred";
player.score = 10000;
player.rank = 1;

// or
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



// PROTOTYPES (pseudo classes)
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



// EVENTS
window.onload = function() {					// Page fully loaded
	prepareEventHandlers();
}

function prepareEventHandlers() {
	myNewImage.onclick = function() {			// Anonymous function
		alert("You clicked the image");
	}
}

//
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



// HTML5 AND CANVAS




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
	...
	// window.innerHeight;
	// document.documentElement.clientWidth;
	// document.body.clientWidth;
};

window.onload = function() {
	...
};



// STYLE GUIDE
// Variables and functions in "camelcase":
var highScore;
function calculateDistance() {}
// Objects in "uppercase first letter"
var myDate = new Date();


// "use strict";


// CDN - Content Distribution Network
code.google.com/apis/libraries

// Minification Tools: JSMin, YUI Compressor, Google Closure Compiler(!:)

// Code Quality Tool: JSLint

// JavaScript Libraries:
jQuery, jQuery UI
Google Closure Library
Mootools
YUI Library
Dojo
Lightbox
Moofx
Aculo
OpenLayer

// Differences in HTML5
Modernizr


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
HTML5 - video 12.01
Html tabindex=1
eval
Countdown 14.01
resetPage();
bind
push
indexOf
fadeTo
typeof
trim
// list of all the methods in object
console.log(Object.getOwnPropertyNames(pattern));
console.dir(pattern);


// View list of all JavaScript variables
for(var b in window) { 
 	if(window.hasOwnProperty(b)) console.log(b); 
}
// or
console.log(Object.getOwnPropertyNames(String));

// To Do
// Join (array.join())
var fruits = ["Banana", "Orange", "Apple", "Mango"];
var energy = fruits.join(); 

// Metoda stringify przeprowadza konwersję obiektu JavaScript na ciąg tekstowy
JSON.stringify(results, null, 4)

// Metoda parse przetwarza ciąg tekstowy zawierający dane JSON na postać obiektu JavaScript
JSON.parse()

window.variable_name - gwarantuje pobranie obiektu globalnego
