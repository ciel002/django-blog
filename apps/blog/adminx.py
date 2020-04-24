import xadmin
from blog.models import Category, Post


class CategoryAdmin(object):
    model_icon = 'fa fa-list'
    list_display = ['name', 'sub_name']


class PostAdmin(object):
    model_icon = 'fa fa-file-text'
    list_display = ['title', 'category', 'add_time']
    search_fields = ('title',)  # 列表包含根据指定字段搜索
    list_filter = ('add_time', 'category')  # 右侧过滤选项
    style_fields = {'category': 'm2m_transfer'}
    readonly_fields = ('click_num',)


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Post, PostAdmin)
