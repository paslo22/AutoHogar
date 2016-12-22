$(document).ready(function() {
//	var temps = $('.temp');
//	$.each(temps, function(index, val) {
		setTimeout(obtenerTemp,2000)
//	});
});

function obtenerTemp() {
	$.get('termometro/', {id:$('.temp').prop('id')}, function(data) {
		console.log(data)
		$('.tempText').text(data['t']+'°C')
		setTimeout(obtenerTemp,25000)
	});
};