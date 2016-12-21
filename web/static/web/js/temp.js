$(document).ready(function() {
	var temps = $('.temp');
	$.each(temps, function(index, val) {

		setTimeout(function() {
			console.log($('.temp'))
			$.get('termometro', {id:$('.temp').prop('id')}, function(data) {
				console.log()
			});
		},500)
	});
});