$(document).ready(function() {
	var garages = $('.garage');
	$.each(garages, function(index, val) {
		var garage = this
		$('.abrirG',garage).click(function(event) {
			event.preventDefault();
			$.post('garage/', {id:$('input',$(this)).val(),op:'abrir'});
		});
		$('.cerrarG',garage).click(function(event) {
			event.preventDefault();
			$.post('garage/', {id:$('input',$(this)).val(),op:'cerrar'});
		});
	});
});