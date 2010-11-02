$(function () {
	$('#main-tabs').tabs({
		load: function (ev, ui) {
			if ($(ui.tab).hasClass('apply-accordion')) {
				console.log($('.accordion'));
				$('.accordion').accordion();
			}
		}
	});
})
