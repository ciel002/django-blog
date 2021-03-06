# Generated by Django 2.1.4 on 2020-04-24 07:11

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_project_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, help_text='图片比例大小为宽高比1.33（最好为350*262）', upload_to='project/', verbose_name='项目图片'),
        ),
        migrations.AlterField(
            model_name='yzb',
            name='is_tj',
            field=models.BooleanField(choices=[('0', '一志愿'), ('1', '调剂')], verbose_name='是否调剂'),
        ),
    ]
