function loadData(url) {
	$.get(url, null, onLoadData, 'xml')
}

function onLoadData(resp) {
	var groups, abilities, graph, new_div;
	graph = $('#graph')
	graph.empty();
	if ((groups = $(resp).find('group')).length) {
	} else {
		abilities = $(resp).find('ability');
		abilities.each(function () {
				new_div = $('<div><div class="graph-label"></div><div class="graph-bar"></div></div><br />');
				new_div.find('.graph-label').append($(this).find('name').text());
				graph.append(new_div);
				new_div.find('.graph-bar').animate({width: $(this).find('skill').text() + '%'}, 'slow');
			});
	}
}

function setupBtns () {
	var btns = $('.btn');
	btns.button();
	btns.each(function () {
			var url = $(this).attr('href');
			$(this).removeAttr('href');
			$(this).click(function () {loadData(url)});
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
