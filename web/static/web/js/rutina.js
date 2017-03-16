$(document).ready(function() {
	var rutinas = $('.rutina');
	$.each(rutinas, function(index, val) {
		var rutina = this;
		$(this).click(function(event) {
			event.preventDefault();
			$.get($(this).attr('href'));
		});
	});
});