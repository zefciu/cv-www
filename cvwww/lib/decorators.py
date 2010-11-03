from pylons import request, tmpl_context as c
from decorator import decorator

@decorator
def check_ajax(f, self, *args, **kwargs):
    self.ajax = c.ajax = \
            (request.headers.get('X-Requested-With') == 'XMLHttpRequest')
    return f(self, *args, **kwargs)
