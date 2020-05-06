from datetime import datetime

from django.db import models

# Create your models here.
from django.utils.timezone import now
from imagekit.models import ImageSpecField
from mdeditor.fields import MDTextField
from pilkit.processors import ResizeToFill


class Category(models.Model):
    name = models.CharField(verbose_name='名称', max_length=20, unique=True, null=False, help_text='文章分类所属的分类名称')
    sub_name = models.CharField(verbose_name='子名称', max_length=20, unique=False, null=False,
                                help_text='url地址传参的字符串(英文)')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return '<Category %s>' % self.name

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题', unique=True, null=False, db_index=True,
                             help_text='文章标题。必填，不超过30个字符')
    image = models.ImageField(max_length=200, verbose_name='文章封面', blank=True, upload_to='post/',
                              help_text='文章封面，必填，建议图片尺寸最好为770*(377-399)')
    image_270x115 = ImageSpecField(source="image", processors=[ResizeToFill(270, 115)], format='JPEG',
                                   options={'quality': 95})
    image_740x315 = ImageSpecField(source="image", processors=[ResizeToFill(740, 315)], format='JPEG',
                                   options={'quality': 95})
    abstract = models.TextField(max_length=300, null=True, blank=True, verbose_name='文章摘要',
                                help_text='文章摘要，选填，最多不超过300个字符', default="")
    category = models.ManyToManyField(Category, verbose_name='分类', help_text='文章分类。必填，可选多个')
    content = MDTextField(verbose_name='内容', help_text='文章内容，必填')
    click_num = models.PositiveIntegerField(default=0, verbose_name='访问量', help_text='文章的点击量，不需要设置')
    add_time = models.DateTimeField(default=now, verbose_name='添加时间', help_text='文章的创建时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return '<Post %s>' % self.title

    def __str__(self):
        return self.title

    def increase_click_num(self):
        self.click_num += 1
        self.save(update_fields=['click_num'])
