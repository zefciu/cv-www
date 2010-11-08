function loadData(url) {
	$.get(url, null, onLoadData, 'xml')
}

function list_abilities(graph, abilities) {
	abilities.each(function () {
			new_div = $('<div><div class="graph-label"></div><div class="graph-bar"></div></div><br />');
			new_div.find('.graph-label').append($(this).find('name').text());
			skill = $(this).find('skill').text();
			new_div.attr('title', skill + '%');
			graph.append(new_div);
			bar_len = (parseInt(skill) * 6).toString();
			new_div.find('.graph-bar').animate({width: bar_len + 'px'}, 'slow');
		});
}

function onLoadData(resp) {
	var groups, abilities, graph, new_div;
	graph = $('#graph')
	graph.empty();
	if ((groups = $(resp).find('group')).length) {
		groups.each(function () {
				graph.append('<h3>' + $(this).attr('name') + '</h3>');
				list_abilities(graph, $(this).find('ability'));
			});
	} else {
		abilities = $(resp).find('ability');
		list_abilities(graph, abilities);
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
