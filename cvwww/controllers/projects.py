import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from cvwww.lib.base import BaseController, render
import cvwww.model as m

log = logging.getLogger(__name__)

class ProjectsController(BaseController):

    def index(self):
        c.projects = m.Session.query(m.Project).join(m.Abilities).all()
        return render('projects.mako')
