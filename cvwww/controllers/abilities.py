import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from cvwww.lib.base import BaseController, render
from cvwww.lib.decorators import check_ajax
import cvwww.model as m

log = logging.getLogger(__name__)

class AbilitiesController(BaseController):

    def index(self):
        c.cats = m.Session.query(m.AbilityCat).all()
        return render('/abilities.mako')
