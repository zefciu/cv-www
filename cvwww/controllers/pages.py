import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from cvwww.lib.base import BaseController, render

log = logging.getLogger(__name__)

class PagesController(BaseController):

    def index(self):
        return render('/main.mako')
    
    def get_page(self, slug):
        pass
