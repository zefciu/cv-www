function loadData(ev) {
	$.get(ev.target.url, null, onLoadData, 'json')
}

function setupBtns () {
	var btns = $('.btn')
	btns.button();
	btns.each(function () {
			this.url = this.getAttr('href');
			this.removeAttr('href');
			this.click(loadData);
		});
}

$(function () {
	$('#main-tabs').tabs({
		load: function (ev, ui) {
			if ($(ui.tab).hasClass('apply-accordion')) {
				$('.accordion').accordion();
			}
			if ($(ui.tab).hasClass('apply-buttons')) {
				setupBtns();
			}
		}
	});
})
