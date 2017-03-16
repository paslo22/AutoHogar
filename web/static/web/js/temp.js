$(document).ready(function() {
	$('select').material_select();
	var temps = $('.temp');
//	$.each(temps, function(index, val) {
	if (temps.length) {
		setTimeout(obtenerTemp,2000)
	}
//	});
	$('select').change(function(event) {
		$.post('/web/tempDeseada/', {id:$('.temp').prop('id'),tempDeseada:$(this).val()});
	});
});

function obtenerTemp() {
	setTimeout(obtenerTemp,60000)
	$.get('/web/termometro/', {id:$('.temp').prop('id')}, function(data) {
		$('.tempText').text(data['t']+'°C')
	});
};