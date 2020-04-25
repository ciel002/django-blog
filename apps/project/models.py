from django.db import models

# Create your models here.
from django.utils.timezone import now
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill


class Project(models.Model):
    name = models.CharField(max_length=30, verbose_name='项目名', null=False, blank=False, unique=True, help_text='项目名称')
    image = ProcessedImageField(upload_to='project/', processors=[ResizeToFill(350, 262)], format='JPEG',
                                options={'quality': 60}, verbose_name='项目图片', help_text='图片比例大小为宽高比1.33（最好为350*262）',
                                blank=True)
    url = models.CharField(max_length=100, verbose_name='项目URL地址', unique=True, null=False, blank=False,
                           help_text='项目URL地址，以/开始的地址')
    desc = models.CharField(max_length=200, verbose_name='项目说明')
    show = models.PositiveSmallIntegerField(choices=((0, '不显示'), (1, '显示')), verbose_name='是否显示')
    add_time = models.DateTimeField(default=now)

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "<Project %s>" % self.name

    def __repr__(self):
        return "<Project %s>" % self.name

    # def image_350_262_url(self):
    #     if self.image_350_262 and hasattr(self.image_350_262, 'url'):
    #         return self.image_350_262.url
    #     else:
    #         return self.image.url


class Yzb(models.Model):
    num = models.CharField(max_length=20, verbose_name='考生编号', null=False, blank=False, primary_key=True)
    name = models.CharField(max_length=10, verbose_name='姓名')
    code = models.CharField(max_length=8, verbose_name='专业代码')
    code_name = models.CharField(max_length=20, verbose_name='专业名称')
    chushi = models.PositiveSmallIntegerField(verbose_name='初试分数')
    fushi = models.PositiveSmallIntegerField(verbose_name='复试分数')
    mark = models.CharField(max_length=20, verbose_name='备注', default="")
    year = models.CharField(max_length=6, verbose_name='年份', null=True)
    is_tj = models.BooleanField(choices=(('0', '一志愿'), ('1', '调剂')), verbose_name='是否调剂')

    class Meta:
        verbose_name = '燕大研招办'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "<Yzb %s:%s>" % (self.name, self.chushi + self.fushi)

    def __repr__(self):
        return "<Yzb %s:%s>" % (self.name, self.chushi + self.fushi)
