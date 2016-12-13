$(document).ready(function() {
	var lights = $('.light');
	$.each(lights, function(index, val) {
		var light = this
		$('.estado',light).change(function(event) {
			$('#encendido',light).toggle("slide", { direction: "right" }, 1000);
			$('#apagado',light).toggle("slide", { direction: "right" }, 1000);
		});
	});
});