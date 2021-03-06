from django.db.models import F
from django.shortcuts import render

# Create your views here.
from project.forms import EmailForm
from project.models import Project, Yzb, YzbVisit
from utils.decorators import increase_web_visit, timeit
from utils.pagination import pagination
from utils.redis_pool import get_redis
from utils.template import template_context


@increase_web_visit
def index_view(request):
    projects = Project.objects.filter(show=True).all()

    context = template_context(tag='project', projects=projects)
    return render(request, 'project.html', context)


@timeit
def yzb_view(request):
    # 增加访问数
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META.get('HTTP_X_FORWARDED_FOR')
    else:
        ip = request.META.get('REMOTE_ADDR')
    # region = ip2_region_by_138(ip)
    YzbVisit.objects.create(ip=ip, url=request.get_full_path())

    # 查询
    year = request.GET.get('year', '')
    code = request.GET.get('code', '')
    tj = request.GET.get('tj', '')
    order = request.GET.get('order', '')
    page = int(request.GET.get('p', 1))
    yzb_while = {}
    if year:
        yzb_while['year'] = year
    if code:
        yzb_while['code'] = code
    if tj:
        yzb_while['is_tj'] = tj
    infos = Yzb.objects.filter(**yzb_while).order_by('num')
    if order:
        if order == 'zongfen':
            infos = infos.annotate(zongfen=F('chushi') + F('fushi')).order_by('-zongfen')
        else:
            infos = infos.order_by('-' + order)

    pages, page_range = pagination(page=page, queryset=infos, per_page=100)

    codes = Yzb.objects.values("code", "code_name").distinct()

    context = template_context(tag='project', pages=pages, page_range=page_range, page_count=(page - 1) * 100,
                               codes=codes, year=year, code=code,
                               tj=tj, order=order)
    return render(request, 'yzb.html', context=context)


@increase_web_visit
def yzb_zxxx_view(request):
    if request.method == 'GET':
        context = template_context(tag='project')
        return render(request, 'yzb_zxxx.html', context=context)
    elif request.method == 'POST':
        form = EmailForm(request.POST)
        if not form.is_valid():
            error = form.errors.get_json_data()['email'][0]['message']
            context = template_context(tag='project', error=error)
            return render(request, 'yzb_zxxx.html', context=context)
        with get_redis() as redis:
            ret = True
            try:
                redis.sadd('yzb:zxxx_to', form.cleaned_data.get('email'))
            except:
                ret = False
            context = template_context(tag='project', success="提交成功，若有最新消息，将发送至您的邮箱")
            return render(request, 'yzb_zxxx.html', context=context)


@increase_web_visit
def yzb_unzxxx_view(request):
    context = template_context(tag='project')
    return render(request, 'yzb_zxxx.html', context=context)
