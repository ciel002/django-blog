import xadmin
from project.models import Project, YzbVisit


class ProjectAdmin(object):
    model_icon = 'fa fa-list'
    list_display = ['name', 'url', 'desc', 'add_time']
    search_fields = ('name', 'url')
    list_filter = ('add_time',)


xadmin.site.register(Project, ProjectAdmin)


class YzbVisitAdmin(object):
    model_icon = 'fa fa-list'
    list_display = ['ip', 'url', 'add_time']
    search_fields = ('ip', 'url')
    list_filter = ('add_time',)


xadmin.site.register(YzbVisit, YzbVisitAdmin)
