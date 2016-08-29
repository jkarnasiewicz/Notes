$(document).ready(function() {
	// $('.img').slideToggle(4000);animate({
	// $('.img').toggle('slow');
	$('.img').fadeToggle(3000).animate({
		// 'width': '+=100px'
		// 'opacity': 0.5,
	});
	// var img = ''
	$('.img').on('mouseenter', function() {
		// img = $(this).attr('src');
		// $(this).attr('src', 'apple.jpg');
		// console.log($(this).siblings('.text:first').text());
		$(this).siblings('.text:first').show();
	});
	$('.img').on('mouseleave', function() {
		// $(this).attr('src', img);
		// console.log($(this).find('.text').text());
		$(this).siblings('.text:first').hide();
	});
	$('.text').on('mouseenter', function(e) {
		// e.stopPropagation();
		$(this).show();
		// $('.img').addClass('#content .img:hover');
		// $('.img:first').css('opacity', 1);
		// $(this).siblings('.img:first').css('opacity', 1);
	});
	$('.text').on('mouseleave', function(e) {
		// e.stopPropagation();
		$(this).hide();
		// $('.img').removeClass('#content .img:hover');
		// $('.img:first').css('opacity', 0.6);
		// $(this).siblings('.img:first').css('opacity', 0.6);
	});
	// $('.text').on('hover', function(e) {
	// 	e.preventDefault();
	// });
	// $('.img').slideToggle(4000);
	// $('.img').toggle('easeOutBounce');
	// $('.img').toggle('slow');
	// $('.img').show('easeOutBounce');
	// $('.img').animate({
	// 	// 'width': '+=100px',								  // width cut by 30px from default value
	// 	'margin-right': '400px',
	// 	'opacity': 1,
	// }, 5000,
	// 	'swing'										  // easing, options: 'linear' etc.
	// );	
});