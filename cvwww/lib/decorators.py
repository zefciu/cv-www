from pylons import request, tmpl_context as c

def check_ajax(f, *args, **kwargs):
        c.ajax = \
                (request.headers.get('X-Requested-With') is 'XMLHttpRequest')
        return f(*args, **kwargs)
