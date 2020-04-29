from django.utils.safestring import mark_safe

import xadmin
from gallery.models import Picture


class PictureAdmin(object):
    model_icon = 'fa fa-picture-o'
    list_display = ['title', 'alt', 'image', 'image_data', 'add_time']
    list_filter = ['title', 'add_time']
    search_fields = ['title']
    # readonly_fields = ('image_data',)

    def image_data(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return mark_safe(u'<img src="%s" width="100px" />' % obj.image.url)
        else:
            return "没有图片"

    # 页面显示的字段名称
    image_data.short_description = u'图片'


xadmin.site.register(Picture, PictureAdmin)
