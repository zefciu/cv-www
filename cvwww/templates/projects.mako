<%inherit file="/skeleton.mako" />
<%def name="title()">Projekty</%def>
<div class="accordion">
% for project in c.projects:
	<h3><a href="#">${project.name}</a></h3>
	<div>
	${project.description}
	% if project.url_source is not None:
	<div>${h.link_to('Link do źródeł', project.url_source)}</div>
	% endif
	% if project.url_application is not None:
	<div>${h.link_to('Link do demonstracji', project.url_application)}</div>
	% endif
	% for ability in project.abilities:
		${ability.name}
	% endfor
	</div>
% endfor
</div>
