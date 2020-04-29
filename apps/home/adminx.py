import xadmin
from home.models import Banner, ContactEmail, WebVisit


class BannerAdmin(object):
    model_icon = 'fa fa-sliders'
    list_display = ['image', 'post', 'add_time']

    # 疑问!!!
    def has_delete_permission(self, request=None, obj=None):
        return True


class ContactEmailAdmin(object):
    model_icon = 'fa fa-paper-plane'
    list_display = ['nickname', 'email', 'message', 'add_time']
    search_fields = ('nickname', 'email')  # 列表包含根据指定字段搜索
    list_filter = ('add_time',)  # 右侧过滤选项


class WebVisitAdmin(object):
    model_icon = 'fa fa-list'
    list_display = ['ip', 'url', 'add_time']
    search_fields = ('ip', 'url')
    list_filter = ('add_time',)


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(ContactEmail, ContactEmailAdmin)
xadmin.site.register(WebVisit, WebVisitAdmin)
