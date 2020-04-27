import xadmin
from project.models import Project, YzbVisit


class ProjectXadmin(object):
    model_icon = 'fa fa-list'
    list_display = ['name', 'url', 'desc', 'add_time']
    search_fields = ('name', 'url')
    list_filter = ('add_time',)


class YzbVisitXadmin(object):
    model_icon = 'fa fa-list'
    list_display = ['ip', 'region', 'url', 'add_time']
    search_fields = ('ip', 'url')
    list_filter = ('add_time',)


xadmin.site.register(Project, ProjectXadmin)
xadmin.site.register(YzbVisit, YzbVisitXadmin)
