<%inherit file="/skeleton.mako" />
<%def name="title()">
Umiejętności
</%def>

<div class="bar-container">
<div class="left-bar">
% for cat in c.cats:
	${h.link_to(cat.name, h.url_for(controller = 'abilities', action = 'get_abilities', slug = cat.slug), class_ = 'btn')}
% endfor
</div>
<div id="graph" />
<div class="clear" />
</div>
