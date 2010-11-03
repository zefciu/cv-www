## vim: set fileencoding=utf-8

<%inherit file="/base.mako" />
<%def name="head()"> 
	${h.javascript_link(h.url_for('/js/jquery.js'))}
	${h.javascript_link(h.url_for('/js/jquery-ui.js'))}
	${h.javascript_link(h.url_for('/js/main-tabs.js'))}
	${h.stylesheet_link(h.url_for('/css/jquery-ui/jquery-ui.css'))}
	${h.stylesheet_link(h.url_for('/css/main.css'))}
</%def>
<div id="main-tabs">
	<ul>
		<li>${h.link_to(u'Dane osobowe', h.url_for(controller = 'pages', action = 'get_page', slug='dane'))}</li>
		<li>${h.link_to(u'Doświadczenie', h.url_for(controller = 'pages', action = 'get_page', slug='doswiadczenie'))}</li>
		<li>${h.link_to(u'Umiejętności', h.url_for(controller = 'abilities', action = 'index'), class_="apply-buttons")}</li>
		<li>${h.link_to(u'Projekty', h.url_for(controller = 'projects', action = 'index'), class_="apply-accordion")}</li>
	</ul>
