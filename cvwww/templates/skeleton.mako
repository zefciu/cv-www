<%inherit file="/base.mako" />

<%def name="head()">
% if not c.ajax:
<title>${next.title()}</title>
% endif
</%def>
% if not c.ajax:
<h1>${next.title()}</h1>
% endif

${next.body()}
