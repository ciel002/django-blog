import xadmin
from xadmin import views
from home.models import Banner, ContactEmail, WebVisit


# 全局xadmin配置
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    site_title = '夏尔的实验室'
    site_footer = '夏尔的实验室'
    menu_style = 'accordion'  # 左侧导航栏的修改


xadmin.site.register(views.CommAdminView, GlobalSettings)


class BannerAdmin(object):
    model_icon = 'fa fa-sliders'
    list_display = ['image', 'post', 'add_time']

    # 疑问!!!
    def has_delete_permission(self, request=None, obj=None):
        return True


xadmin.site.register(Banner, BannerAdmin)


class ContactEmailAdmin(object):
    model_icon = 'fa fa-paper-plane'
    list_display = ['nickname', 'email', 'message', 'add_time']
    search_fields = ('nickname', 'email')  # 列表包含根据指定字段搜索
    list_filter = ('add_time',)  # 右侧过滤选项


xadmin.site.register(ContactEmail, ContactEmailAdmin)


class WebVisitAdmin(object):
    model_icon = 'fa fa-list'
    list_display = ['ip', 'url', 'add_time']
    search_fields = ('ip', 'url')
    list_filter = ('add_time',)


xadmin.site.register(WebVisit, WebVisitAdmin)
