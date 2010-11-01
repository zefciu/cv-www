% if c.ajax:
<%inherit file="/ajax.mako" />
% else:
<%inherit file="/standalone.mako" />
% endif
<%def name="title()">
${c.page.title}
</%def>

${c.page.content}
