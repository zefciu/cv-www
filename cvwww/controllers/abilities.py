import logging
import sqlalchemy as sa

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from cvwww.lib.base import BaseController, render
from cvwww.lib.decorators import check_ajax
import cvwww.model as m

log = logging.getLogger(__name__)

class AbilitiesController(BaseController):

    @check_ajax
    def index(self):
        c.cats = m.Session.query(m.AbilityCat).all()
        return render('/abilities/index.mako')

    def get_abilities(self, slug):
        try:
            c.cat = m.Session.query(m.AbilityCat).filter(
                m.AbilityCat.slug == slug
            ).one()
        except sa.orm.exc.NoResultFound:
            abort(404)

        response.headers['Content-type'] = 'application/xml; charset=utf-8'
        return render('/abilities/get_category.mako')
