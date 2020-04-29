from django.db import models

# Create your models here.
from django.utils.timezone import now

from blog.models import Post


class WebVisit(models.Model):
    ip = models.GenericIPAddressField(verbose_name='IP地址', null=False)
    url = models.URLField(verbose_name='访问的地址', null=False)
    add_time = models.DateTimeField(default=now)

    class Meta:
        verbose_name = '网站访问'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "<WebVisit IpAddress %s>" % self.ip


class Banner(models.Model):
    image = models.ImageField(upload_to='banner/', verbose_name='轮播图')
    # url = models.URLField(default='#', max_length=200, verbose_name='图片链接')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='所属文章')
    add_time = models.DateTimeField(default=now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<Banner %s>' % self.post.title


class ContactEmail(models.Model):
    nickname = models.CharField(max_length=30, verbose_name='联系人昵称', null=False)
    email = models.EmailField(max_length=50, verbose_name='邮箱地址', null=False)
    message = models.TextField(verbose_name='联系信息', null=False)
    add_time = models.DateTimeField(default=now, verbose_name='添加时间')

    class Meta:
        verbose_name = '联系人信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<Banner %s>' % self.nickname
