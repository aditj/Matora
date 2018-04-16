$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				mains : $('#mains').val(),
				
			},
			type : 'POST',
			url : '/process'
		})
		

		event.preventDefault();

	});

});
