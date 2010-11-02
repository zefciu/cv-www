% if c.ajax:
<%inherit file="/ajax.mako" />
% else:
<%inherit file="/standalone.mako" />
% endif
<%def name="title()">Projekty</%def>
<div class="accordion">
% for project in c.projects:
	<h3>${project.name}</h3>
	<div>
	${project.description}
	% for ability in project.abilities:
		$project.abilities
	% endfor
	</div>
% endfor
</div>
