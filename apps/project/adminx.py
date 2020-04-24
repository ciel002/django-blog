import xadmin
from project.models import Project


class ProjectXadmin(object):
    model_icon = 'fa fa-list'
    list_display = ['name', 'url', 'desc', 'add_time']
    search_fields = ('name', 'url')
    list_filter = ('add_time', )


xadmin.site.register(Project, ProjectXadmin)
