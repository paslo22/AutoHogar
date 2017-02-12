$(document).ready(function() {
	var temps = $('.temp');
//	$.each(temps, function(index, val) {
	if (temps.length) {
		setTimeout(obtenerTemp,2000)
	}
//	});
});

function obtenerTemp() {
	setTimeout(obtenerTemp,60000)
	$.get('termometro/', {id:$('.temp').prop('id')}, function(data) {
		$('.tempText').text(data['t']+'°C')
	});
};