import logging

import sqlalchemy as sa
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from cvwww.lib.base import BaseController, render
from cvwww.lib.decorators import check_ajax
import cvwww.model as m

log = logging.getLogger(__name__)

@check_ajax
class PagesController(BaseController):

    def index(self):
        return render('/main.mako')
    
    def get_page(self, slug):
        try:
            c.page = m.Session.query(m.Page).filter(m.Page.slug == slug).one()
        except sa.orm.exc.NoResultFound:
            abort(404)
            
        return render('page.mako')
