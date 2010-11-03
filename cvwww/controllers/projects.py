import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from cvwww.lib.base import BaseController, render
import cvwww.model as m
from cvwww.lib.decorators import check_ajax

log = logging.getLogger(__name__)

class ProjectsController(BaseController):

    @check_ajax
    def index(self):
        c.projects = m.Session.query(m.Project).all()
        return render('projects.mako')
