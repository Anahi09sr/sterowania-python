
	$(window).scroll(function() {
		$('.entrance').each(function(){
		var imagePos = $(this).offset().top;

		var topOfWindow = $(window).scrollTop();
			if (imagePos < topOfWindow+400) {
				$(this).addClass("slideUp");
			}
		});
	});

	$('#animatedElement').click(function() {
		$(this).addClass("slideUp");
	});

    // $('.hover').hover(function() {
	// 	$(this).addClass("pulse");
	// });
