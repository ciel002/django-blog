import functools
import time
from urllib.parse import unquote

from home.models import WebVisit


def increase_web_visit(fun):
    @functools.wraps(fun)
    def wrap(request, *args, **kwargs):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META.get('HTTP_X_FORWARDED_FOR')
        else:
            ip = request.META.get('REMOTE_ADDR')
        # 增加访问数据
        WebVisit.objects.create(ip=ip, url=unquote(request.get_full_path()))
        return fun(request, *args, **kwargs)

    return wrap


def timeit(fun):
    @functools.wraps(fun)
    def timed(*args, **kw):
        ts = time.time()
        result = fun(*args, **kw)
        te = time.time()
        print('%r (%r, %r) %2.2f sec' % (fun.__name__, args, kw, te - ts))
        return result

    return timed
