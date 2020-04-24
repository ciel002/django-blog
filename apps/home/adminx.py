import xadmin
from home.models import Banner, ContactEmail
from xadmin.views import ModelAdminView


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
