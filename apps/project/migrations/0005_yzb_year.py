# Generated by Django 2.1.4 on 2020-04-24 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_yzb'),
    ]

    operations = [
        migrations.AddField(
            model_name='yzb',
            name='year',
            field=models.CharField(max_length=6, null=True, verbose_name='年份'),
        ),
    ]
