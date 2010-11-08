<%inherit file="/xml.mako" />
<%def name="list_abilities(l)">
	% for ability in l:
		<ability>
			<name>${ability.name}</name>
			<skill>${str(ability.skill)}</skill>
		</ability>
	% endfor
</%def>
<category>
	% if c.cat.ability_groups:
		% for group in c.cat.ability_groups:
			<group name="${group.name}">
				${list_abilities(group.abilities)}
			</group>
		% endfor;
	% else:
		${list_abilities(c.cat.abilities)}
	% endif;
</category>
