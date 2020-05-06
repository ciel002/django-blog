from django.db import models

# Create your models here.
from django.utils.timezone import now
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Picture(models.Model):
    title = models.CharField(max_length=20, verbose_name='图片标题', null=False, help_text='必填，图片标题')
    alt = models.CharField(max_length=20, verbose_name='图片说明', null=True, blank=True, help_text='选填，当图片无法显示时，显示的文字信息')
    image = models.ImageField(upload_to='gallery/', verbose_name='图片', max_length=200, help_text='必填，上传图片')
    image_270x192 = ImageSpecField(source="image", processors=[ResizeToFill(270, 192)], format='JPEG',
                                   options={'quality': 95})
    add_time = models.DateTimeField(default=now, verbose_name='添加时间')

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def __repr__(self):
        return '<Picture %s>' % self.title
