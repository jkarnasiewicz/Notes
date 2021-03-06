// Instead window.onload the jQuery library provides a page start routine that waits
// for DOM elements to be loaded, but does not wait for images or other media to finish loading
$(document).ready(function(){
	// code goes here
});

// Alternative version if other libraries use the $ sign
jQuery(document).ready(function($){
	$('')
	// code goes here
});

// or
var $new_sign = jQuery.noConflict();
// and then
$new_sign("#elem").fadeOut('slow');



// Pass messages and variables into console
console.log('Message');
window.tmp = 12;



// Selecting elements (always returning list)
$('#header');                           // by id
$('.inline_block');                     // by class
$('h3');                	            // by tag
$('[href]') 				            // by attributes
$('[role=banner]');     	            // by attributes of the selector which have specify value

$('span', $(this));                     // selecting all span elements within $(this) context

$('li ul');                             // every single ul element in li tag
$('li > ul');                           // all unordered list that are (only) children of list item
$("#tours > .class1, .class2");

$("input[name^='news']");               // find all inputs with an attribute name that starts with 'news'
$("[id^='section'] > [id^='pre']");
$("input[name$='letter']");             // finds all inputs with an attribute name that ends with 'letter'

$('li:even');                           // pseudo-selectors
$('ul:odd');
$('ul:last');
$('.panel:not(:first)');

$("p:contains('packages')");            // find any paragraph that contain the word "packages"
$('a:visible');
$(item).is(':hidden')



// Traversing (faster than selectors)
$('li').first().next();                 // second li tag
$('li').last().prev();                  // penult li tag

$('li').filter('.onsale');
$('#col_3').closest('.list');           // going up the DOM looking for class .list

$('#col_3').find('a');                  // finding all 'a' elements inside id=col_3 tag, not only direct children
$('#col_3').children();                 // all direct children
$('#col_3').children('a');              // all direct children that are 'a' element

$('#col_3').parent();                   // parent element
$('#col_3').parents();                  // all parents, too the root element
$('#col_3').parents('ol');              // all parents, that are 'ol' element

$('#col_3').siblings();                 // the same level that id='col_3'



// Atributes and properties
$(this);
$('#bakcpack').prop('checked');
$('#bakcpack').prop({
	'disabled': true,
	'checked': false
});
$('.checkbox').find('input[type=checkbox]').prop('disabled', true);
$('.checkbox').find('input[type=checkbox]').prop('disabled', !$(this).prop('checked'));   // is not

$('a:first').attr('href');                                // the value of the attribute href for first 'a' tag
$('a:first').attr('href', 'contact.html ');
$('#formContact').attr('action', 'contact-submitted-nosub.html');

$('#target').offset();									  // coordinates of the element
$('[role=banner]').length;



// Reading and changing values
$("header").html();                                       // reading html content
$("header").text();                                       // reading text/values
$("header").text().trim();                                // reading text with no addintional white spaces
$("#test").text($(this).find('option:selected').text());
$("input:radio[name=station2]:checked").val();

$("header").html('<h1>Hello!</h1>');                      // changing html content



// Css
$("li").not( ":even" ).css({'background-color': 'red',
                            'border-color': '1px solid #967'});
$('#graph').css('display', 'block') === $('#graph').show()      // show is prefer



// Add, remove, toggle and check classes
$('#boxes').find('li:nth-child(2)').addClass('selected');
$('#boxes').find('li:nth-child(3)').removeClass('selected');
$('#boxes').find('li:nth-child(2)').toggleClass('selected');

$('#boxes').hasClass('highlighted');                                // if() {} else {}



// Adding, modifying, and removing content dynamically
var new_node = $('<p>New node</p>');                                // creating new node
$('#group-friends').prepend(new_node);                              // first child element after selected tag
$('#group-friends').append('<input type='text' value='John' placeholder="Friend\'s name">');
$('#group-friends').after(new_node);                                // next sibling element after selected tag
$('#group-friends').before(new_node);

$('#image').clone().appendTo($(this)).addClass('.ghost'); 
// .prependTo(), .insertAfter(), .insertBefore()

$('#group-pets').find('input:last').remove();
// removes the matched element from the DOM completely

$('#group-pets').detach();
// is like remove(), but keeps the stored data and events associated with the matched elements

$('#group-friends').find('.group:first').clone();       // copy element



// Triggering a change with events
// add even handler
$('selector').on('click', myHandlerFunction);
// on mouse events: dbclick, focusin, focusout, mousedown,
// mouseup, mousemove, mouseout, mouseover, mouseleave, mouseenter

$('#name').on('keyup', myHandlerFunction);                    // on keyboard events: keypress, keydown
// multiple event registration
$('#name').on('change focuse', myHandlerFunction);            // on form events: blur, select, submit

$('#filters').on('mouseenter', '.onsale', function(event) {
    event.stopPropagation();
    // the browser will still handle the click event but will prevent it from 'bubbling up' to each parent node
    event.preventDefault();
    // prevent default behavior of the browser, e.g: prevent poping on top of the page
    // ....
});

// remove event handler
$('selector').off('click');
$('selector').off('click', myHandlerFunction);

// triger event
$('#name').on('submit', function(event) {                   // we pass triggered event to the function
    $('#id_field').trigger('change');                       // trigger 'change' event
});



// Animations
$('#flower-item').find('li:nth-child(2) a').hide(2000);
// 2 seconds == 2000 miliseconds CSS "display" property to none

$('#flower-item').find(':hidden').show(2000);

$('#flower-item').toggle('fast');
$('#flower-item').fadeToggle('slow');                     // combine fadeIn and fadeOut
$('#flower-item').slideToggle(4000);					  // combine slideUp and slideDown



// Tooltip
$('#flower-item').find('a').on('mouseenter mouseleave', function(e){
	e.preventDefault();
	$(this).children('.info').fadeToggle('slow');
})



// Animate numeric properties
$('#flower-item').animate({'opacity': '1', 'top': '-14px'}, 'fast');
// fast - 200, normal - 400, slow - 600 milliseconds

$('#flower-item').find('a').on('click', function(e){
	e.preventDefault();
	$(this).find('img').animate({
		'width': '30px',								  // or '50%', width set to 30px
		'width': '-=30px',								  // width cut by 30px from default value
		'margin-left': '400px',
		'opacity': 0,
		'left': $('#target').offset().left - $('#current').offset().left,
		'top': $('#target').offset().top - $('#current').offset().top,
	}, 2000,
		'swing',										  // easing, options: 'linear' etc.
		function() {
			$(this).remove();							  // Callback function triggerd when the animation ends
		}
	);
})



// Chaining
var grid = $('#grid')
    .find('li')
    .css('background', '#600')
    .animate({width: '-=100'}, 2000)
    .fadeOut()
    .fadeIn('slow');



// AJAX (technologia oferująca asynchroniczną funkcjonalność)
// Ajax pozwala na żądanie danych z serwera oraz wczytanie ich bez konieczności odświeżenia całej strony

// Na początku Ajax był akronimem oznaczającym technologie używane podczas wykonywania żądań
// asynchronicznych, takich jak asynchroniczny JavaScript i XML. Od tamtego czasu
// wiele się zmieniło, technologie są rozwijane, a pojęcie Ajax oznacza teraz grupę
// technologii oferujących asynchroniczną funkcjonalność w przeglądarce internetowej.
$('#update').load('update_data.html #content');

$.getJSON('data.json', function(data) {
	var output = '<ul>';
	$.each(data, function(key, val) {
		output += '<li>' + val.name + '</li>';
	});
	output += '</ul>';
	$('#update').append(output);
});


// dynamic content
$('nav a').on('click', function(e) {
    e.preventDefault();
    var url = this.href;

    $('nav a.current').removeClass('current');
    $(this).addClass('current');

    $('#container').remove();
    $('#content').load(url + ' #content').hide().fadeIn('slow');
});



// dynamic search
$('#search').keyup(function() {
    var searchField = $('#search').val();
    var myExp = new RegExp(searchField, "i");
    $.getJSON('data.json', function(data) {
        var output = '<ul class="searchresults">';
        $.each(data, function(key, val) {
            if ((val.name.search(myExp) != -1) ||
            (val.bio.search(myExp) != -1)) {
                output += '<li>';
                output += '<h2>'+ val.name +'</h2>';
                output += '<img src="images/'+ val.shortname +'_tn.jpg" alt="'+ val.name +'" />';
                output += '<p>'+ val.bio +'</p>';
                output += '</li>';
            }
        });
        output += '</ul>';
        $('#update').html(output);
    });
});



function delete_record(data_url) {
    var data = {};
    ...
    $.ajax({
        url: data_url,
        type: "POST",
        data: data,
        timeout: 2000,
        beforeSend: function (request) {
            $("body").css("cursor", "wait");
        },
        success: function(json) {
            if (!json.success) {
                $.smallBox({
                    title: gettext("Error!"),
                    content: json.msg,
                    color: "#953b39",
                    iconSmall: "fa fa-cross bounce animated",
                    timeout: 4000,
                    sound: false
                });
            } else {
                ...
                $.smallBox({
                    title: gettext("Success!"),
                    content: json.msg,
                    color: "#739E73",
                    iconSmall: "fa fa-thumbs-up bounce animated",
                    timeout: 4000,
                    sound: false
                });
            }
        },
        error: function(xhr, errmsg, err) {
            show_error(xhr);
        },
        complete: function() {
            $("body").css("cursor", "default");
        }
    });
}



// submiting forms
$('#submit-button').click(function(e) {
    e.preventDefault();
    var form = $('#document-form');
    $.ajax({
        url: form.attr('action'),
        type: 'POST',
        data: form.serialize(),
        beforeSend: function (request) {
            $("body").css("cursor", "wait");
        },
        success: function(data) {
            if(data.success) {
                window.location = data.redirect;
                return;
            }
            if(data.form) {
                $('#modal .modal-content').html(data.form);
                return;
            }
            $('#modal .modal-content').html(data);
        },
        error: function(xhr, errmsg, err) {
            show_error(xhr);
        },
        complete: function() {
            $("body").css("cursor", "default");
        }
    });
});



$(function() {
    $('#submit-button').click(function(e) {
      $('#import-form').submit();
    });

    $('#import-form').submit(function(e) {
        var form = $(this);
        $.ajax({
            url: form.attr('action'),
            type: 'POST',
            dataType: "json",
            data: new FormData( this ),
            processData: false,
            contentType: false,
            cache: false,                           // Prevent caching AJAX call's
            crossDomain: true,
            beforeSend: function () {

            },
            // .done()
            success: function(data) {
                if(data.success) {
                    window.location = data.redirect;
                    return;
                }
                if(data.form) {
                    $('#modal .modal-content').html(data.form);
                    return;
                }
                $('#modal .modal-content').html(data);
                $("#container").html($(json.html_data).find("#container")).hide().fadeIn(400);
            },
            // .fail()
            error: function() {

            },
            // .always()
            complete: function() {
                
            }
        });
        e.preventDefault();
    });
});



// TYPE TESTING FUNCTIONS
$.type(object)
$.isArray(array)
$.isFunction(func)
// Optional arguments
// var funcToCall = $.isFunction(arg1) ? arg1 : $.isFunction(arg2) ? arg2 : arg3;
$.isEmptyObject(object)
$.isPlainObject(object)
$.isXmlDoc(doc)
$.isNumeric(number)
$.isWindow(window)



// UTILITY FUNCTIONS
var myArray = [1, 2, 3, 3, 4, 4, 5]
// $.inArray returns index
if($.inArray(4, myArray) != -1) {
    console.log("4 is in the array")
}

// unique
$.unique(myArray);

// merge
$.merge(myArray, myArray2);

// map
var newArray = $.map(myArray, function(item, index) {
    return item * 2;
});

// grep (filter)
var greppedArray = $.grep(myArray, function(item) {
    return item%2 == 0;
})

// makeArray returns simple javascript array with nodes
$.makeArray($("div"));

// getScript, execute script from the url (like ajax call)
// it is non blocking call
$.getScript(url, function(data, textStatus) {

});



// pushStack function
// jQuery plugin, simple method, stack
$.fn.everyThird = function() {
    var arr = [];
    $.each(this, function(idx, item) {
        if(idx%3 == 0) {
            arr.push(item)
        }
    })
    return this.pushStack(arr, "everyThird", "");
}

// every div has bold font but every third div has red color
$("#clickme").click(function() {
    $("div").everyThird().css("color", "Red").end().css("font-weight", "bold");
});



// each function
// $.each(collection, callback(index, element))
// $(selector).each(acllback(index, element))
$("div").each(function(index, element) {
    var wrappedElem = $(elem);
    wrappedElem.addClass("myclass");
    // terminated loop before it finished: return false;
});

$('input[name={{ form.products.html_name }}]:checked').each(function() {
    $('input[name={{ form.free_items.html_name }}][value=' + $(this).val() + ']').prop('disabled', true);
});



// parseJSON
// turns a json string into javascript objects
var myObject = $.parseJSON(jsonString);



// extend
// creating copy of the object not reference
var animal = {
    eat: function() {}
}

var dog = {
    bark: function() {}
}

$.extend(true, dog, animal);
dog.eat();



// proxy, setting the value for 'this' keyword in the event handler
// $.proxy(handler, context);
var eventHandler = { ... }
$("#clickme").click($.proxy(eventHandler.clickButtonHandler, eventHandler));



// IIFE - Immediately-Invoked Function Expression (executed immediately)
(function($) {
    ...
})(jQuery);



// ADDING UTILITY METHODS AND PLUGINS
// Adding utility methods that are part of jQuery
(function($) {
    $.log = function(value) {
        if(console) {
            console.log(value);
        }
    }
    $.log.group = function(value) {
        if(console && console.group) {
            console.group(value);
        }
    }
    $.log.groupEnd = function() {
        if(console && console.group) {
            console.groupEnd();
        }
    }
})(jQuery);

$(function() {
    $.log.group('my group');
    $.log('hi there');
    $.log.groupEnd();
});



// Basic plugin pattern
// fn property(object) - prototype for jQuery object
(function($) {
    $.fn.myPlugin = function() {
        return this;
    };
})(jQuery);
// that is why we have $('div').myPlugin();
// 'this' in myPlugin is $('div')



// Plugin with parameters
(function($) {
    $.fn.myPlugin = function(options) {
        var settings = {};
        $.extend(settings, this.myPlugin.defaults, options);
        return this.css('background-color', settings.backColor);
    }

    $.fn.myPlugin.defaults = {
        backColor: 'orange'
    };
})(jQuery);

$(function() {
    $('#div').myPlugin();                               // default option
    $('#div').myPlugin({'backColor': 'yellow'});
});

// Tracking state Plaugin
// use closures to maintain plugin-level state(outside )
// use this.data() to maintain node-level state



// Custom Selectors
(function($) {
    $.expr[':'].every = function(elem, idx, meta, items) {
        return (idx + 1) % parseFloat(meta[3]) == 0;
    }
})(jQuery);

$(function() {
    $("div:every(4)").css('background-color', 'red');
});



// DATA STORING
// Data method (storing data in jQuery(cache) not in Html(it dont change html))
// keys - case sensitive
// Reserved keys: 'events', 'handle', "_anything that starts with an underscore"
$('#div').data("three", 3);
var _number = $('#div').data("three");

// storing js objects
var object = { val1: 3, val2: "hi"}
$('#div').data("object", object);
$('#div').data("object").val1;

// storing js functions
function myFunc() {
    console.log("called my function");
}

$('#div').data("func", myFunc);
$('#div').data("func")();

// $.data()
// $.data(object, 'key', value)
// the fastest storing method
var div = $("#div");
$.data(div.get(0), 'number', 25);

var val = $.data(div.get(0), 'number');
// all data
var data = div.data();

// data events (lising to events)
div.on('setData', function(e, key, value) { console.log('data set', key, value); });
div.on('changeData', function(e, key, value) { console.log('data change', key, value); });

div.on('get Data', function(e, key, value) { return 25; });

// Remove data
div.removeData('number');

// remove all data
div.removeData();



// DEFERRED, PROMISE
// Deferred
// an object for holding & calling a queue of success/failure/complete callbacks
// allows multiple callback registration
// allows registration of callbacks at any time

// Promise object
// don't have succes and fail methods
// other objects can't decide to reject or recive that object

// $.when
// combine 1 or more deferred objects
// return a promise, not a deferred object
// only resolves if all subordinate defferred objects resolve
// rejects instantly if any subordinate deferred objects reject


// Execute the function myFunc when both ajax requests are successful,
// or myFailure if either one has an error
$.when( $.ajax( "/page1.php" ), $.ajax( "/page2.php" ) )
    .then( myFunc, myFailure );

// The method will resolve its master Deferred as soon as all the Deferreds resolve,
// or reject the master Deferred as soon as one of the Deferreds is rejected.
// If the master Deferred is resolved, the doneCallbacks for the master Deferred are executed
var d1 = $.Deferred();
var d2 = $.Deferred();
 
$.when( d1, d2 ).done(function ( v1, v2 ) {
    console.log( v1 ); // "Fish"
    console.log( v2 ); // "Pizza"
});
 
d1.resolve( "Fish" );
d2.resolve( "Pizza" );



// JQUERY PERFORMANCE
// - Caching selections and other items (outside of loops)
// - Use element properties when possible (instead of jQuery, e.g. .attr())
// - Use traversing, e.g. $('#div').find('.title')
// - Use one append
// - Insert using a containing element (.append('<div>' + appendString + '</div>');)

// Profile performance
console.profile('description');
// code
console.profileEnd('description');

// Manual timing
console.time('description');
// code
console.timeEnd('description');

// Writing
var appendString = "";
$.each(arr, function() {
    appendString += "<div>" + this + "</div>";
});

$('#parent').append('<div>' + appendString + '</div>');
