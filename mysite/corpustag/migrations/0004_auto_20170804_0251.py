# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpustag', '0003_auto_20170804_0216'),
    ]

    operations = [
        migrations.CreateModel(
            name='YouthForumData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=2000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('first_class', models.CharField(choices=[('教育成长', '教育成长'), ('党建团建', '党建团建')], default='unknown', max_length=20)),
                ('second_class', models.CharField(choices=[('教育成长', (('校园生活', '校园生活'), ('考研出国', '考研出国'))), ('党建团建', (('团务工作', '团务工作'), ('党务工作', '党务工作'))), ('unknown', 'unknown')], default='unknown', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]