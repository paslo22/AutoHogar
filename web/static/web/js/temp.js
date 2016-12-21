$(document).ready(function() {
	var temps = $('.temp');
	$.each(temps, function(index, val) {
		setTimeout(function() {
			$.get('termometro/', {id:$('.temp').prop('id')}, function(data) {
				console.log(data)
				$('.tempText').text('Temperatura: '++' °C')
			});
		},500)
	});
});