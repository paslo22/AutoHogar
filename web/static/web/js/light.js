$(document).ready(function() {
	var lights = $('.light');
	$.each(lights, function(index, val) {
		var light = this
		$('.estado',light).change(function(event) {
			$('#encendido',light).toggle(1000);
			$('#apagado',light).toggle(1000);
			$.post('luz/', {id:$(this).prop('value')});
		});
	});
});