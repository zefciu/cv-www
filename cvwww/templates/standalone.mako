<%inherit file="/base.mako" />

<%def name="head()">
<title>${next.title()}</title>
</%def>

${next.body()}
