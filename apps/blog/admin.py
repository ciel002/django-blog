from django.contrib import admin

# Register your models here.
from django.utils.translation import gettext_lazy

from blog.models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # 列表显示的字段
    search_fields = ('name',)  # 列表包含根据指定字段搜索
    # list_filter = ('publish_date',)  # 右侧过滤选项


class PostAdmin(admin.ModelAdmin):

    def 分类(self, obj):
        return [a.name for a in obj.category.all()]

    list_display = ('title', '分类', 'click_num', 'add_time')  # 列表显示的字段
    search_fields = ('title',)  # 列表包含根据指定字段搜索
    list_filter = ('add_time', 'category')  # 右侧过滤选项

    fieldsets = [
        ('基本', {'fields': ['title', 'category']}),
        ('内容', {'fields': ['content']}),
        ('杂项', {'fields': ['click_num', 'add_time']})
    ]

    filter_horizontal = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
