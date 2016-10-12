// Wait for the document to be fully loaded and ready before working with it
// DOM - Document Object Model
$(document).ready(function(){
	// code goes here
});

// Alternative version if other libraries use the $ sign
jQuery(document).ready(function($){
	$('')
	// code goes here
});



// Pass message into console
console.log('Message');
window.tmp = 12;



// Selecting elements (always returning list)
$('#header');               // by id
$('.inline_block');         // by class
$('h3');                	// by tag
$('[href]') 				// by attributes
$('[role=banner]');     	// by attributes of the selector which have specify value

$('li ul');                 // every single ul element in li tag
$('li > ul');               // all unordered list that are (only) children of list item
$("#tours > .class1, .class2");

$("input[name^='news']");               // find all inputs with an attribute name that starts with 'news'
$("[id^='section'] > [id^='pre']");
$( "input[name$='letter']" );           // finds all inputs with an attribute name that ends with 'letter'

$('li:even');                           // pseudo-selectors
$('ul:odd');
$('ul:last');

$("p:contains('packages')");            // find any paragraph that contain the word "packages"
$('a:visible');



// Traversing (faster than selectors)
$('li').first().next();     // second li tag
$('li').last().prev();      // penult li tag

$('li').filter('.onsale');
$('#col_3').closest('.list');   // going up the DOM looking for class .list

$('#col_3').find('a');      // finding all 'a' elements inside id=col_3 tag, no only direct children
$('#col_3').children();     // all direct children
$('#col_3').children('a');  // all direct children that are 'a' element

$('#col_3').parent();       // parent element
$('#col_3').parents();      // all parents, too the root element
$('#col_3').parents('ol');  // all parents, that are 'ol' element

$('#col_3').siblings();     // the same level that id='col_3'



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
$('#graph').css('display', 'block') === $('#div-graph').show()      // show is prefer



// Add, remove, toggle and check classes
$('#boxes').find('li:nth-child(2)').addClass('selected');
$('#boxes').find('li:nth-child(3)').removeClass('selected');
$('#boxes').find('li:nth-child(2)').toggleClass('selected');

$('#boxes').hasClass('highlighted');                       // if() {} else {}



// Adding, modifying, and removing content dynamically
var new_node = $('<p>New node</p>');                       // creating new node
$('#group-friends').prepend(new_node);                     // first child element after selected tag
$('#group-friends').append('<input type='text' value='John' placeholder="Friend\'s name">');
$('#group-friends').after(new_node);                       // next sibling element after selected tag
$('#group-friends').before(new_node);

$('#image').clone().appendTo($(this)).addClass('.ghost'); 
// .prependTo(), .insertAfter(), .insertBefore()

$('#group-pets').find('input:last').remove();
// removes the matched element from the DOM completely

$('#group-pets').detach();
// is like remove(), but keeps the stored data and events associated with the matched elements

$('#group-friends').find('.group:first').clone();       // copy element



// Triggering a change with events
$('#name').on('click', myFunction);
// on mouse events: dbclick, focusin, focusout, mousedown,
// mouseup, mousemove, mouseout, mouseover, mouseleave, mouseenter

$('#name').on('keyup', myFunction);             // on keyboard events: keypress, keydown
$('#name').on('change', myFunction);            // on form events: focuse, blur, select, submit

$('#filters').on('mouseenter', '.onsale', function(event) {
    event.stopPropagation();
    // the browser will still handle the click event but will prevent it from 'bubbling up' to each parent node
    event.preventDefault();
    // prevent default behavior of the browser, e.g: prevent poping on top of the page
    // ....
});

$('#name').on('submit', function(event) {           	  // we pass triggered event to the function
    $('#id_field').trigger('change');                     // trigger 'change' event
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



// Ajax (technologia oferująca asynchroniczną funkcjonalność)
// Ajax pozwala na żądanie danych z serwera oraz wczytanie ich bez konieczności odświeżenia całej strony
$('#update').load('update_data.html #content');

$.getJSON('data.json', function(data) {
	var output = '<ul>';
	$.each(data, function(key, val) {
		output += '<li>' + val.name + '</li>';
	});
	output += '</ul>';
	$('#update').append(output);
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



// Dynamic Search
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



// Submiting forms
$('#submit-button').click(function(e) {
    e.preventDefault();
    var form = $('#document-form');
    $.ajax({
        url: form.attr('action'),
        type: 'POST',
        data: form.serialize(),
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
            data: new FormData( this ),
            processData: false,
            contentType: false,
            cache: false,                           // Prevent caching AJAX call's
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


// To Do
$.Nazwa = function(){}// new variable
// Na początku Ajax był akronimem oznaczającym technologie używane podczas wykonywania żądań
// asynchronicznych, takich jak omówione powyżej — asynchroniczny JavaScript i XML. Od tamtego czasu
// wiele się zmieniło, technologie są rozwijane, a pojęcie Ajax oznacza teraz grupę technologii oferujących
// asynchroniczną funkcjonalność w przeglądarce internetowej.

$('input[name={{ form.products.html_name }}]:checked').each(function() {
    $('input[name={{ form.free_items.html_name }}][value=' + $(this).val() + ']').prop('disabled', true);
});

$.items = $('input[name={{ form.products.html_name }}]');

$('nav a').on('click', function(e) { // Użytkownik kliknął łącze.
    e.preventDefault(); // Zatrzymanie wczytywania nowego łącza.
    var url = this.href; // Pobranie wartości atrybutu href.

    $('nav a.current').removeClass('current'); // Usunięcie klasy current.
    $(this).addClass('current'); // Określenie nowego elementu jako bieżącego.

    $('#container').remove(); // Usunięcie starej zawartości.
    $('#content').load(url + ' #content').hide().fadeIn('slow'); // Nowa zawartość.
});
