from django.db.models import Count, F
from django.shortcuts import render

# Create your views here.
from project.models import Project, Yzb
from utils.template import template_context


def index_view(request):
    projects = Project.objects.filter(show=True).all()

    context = template_context(tag='project', projects=projects)
    return render(request, 'project.html', context)


def yzb_view(request):
    year = request.GET.get('year', '')
    code = request.GET.get('code', '')
    tj = request.GET.get('tj', '')
    order = request.GET.get('order', '')
    yzb_while = {}
    if year:
        yzb_while['year'] = year
    if code:
        yzb_while['code'] = code
    if tj:
        yzb_while['is_tj'] = tj
    infos = Yzb.objects.filter(**yzb_while)
    if order:
        if order == 'zongfen':
            infos = infos.annotate(zongfen=F('chushi') + F('fushi')).order_by('-zongfen')
        else:
            infos = infos.order_by('-'+order)

    codes = Yzb.objects.values("code", "code_name").distinct()

    context = template_context(tag='project', infos=infos, codes=codes, year=year, code=code, tj=tj, order=order)
    return render(request, 'yzb.html', context=context)
