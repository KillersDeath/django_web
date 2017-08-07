# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-07 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpustag', '0014_auto_20170807_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='continent',
            name='name',
            field=models.CharField(choices=[('人文科技', '人文科技'), ('创业就业', '创业就业'), ('党建团建', '党建团建'), ('身心健康', '身心健康'), ('生活休闲', '生活休闲'), ('情感家庭', '情感家庭'), ('理想信念', '理想信念'), ('教育成长', '教育成长'), ('社团生活', '社团生活'), ('权益保障', '权益保障'), ('政策法规', '政策法规'), ('unknown', 'unknown')], default='unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(choices=[('人文科技', '人文科技'), ('创业就业', '创业就业'), ('党建团建', '党建团建'), ('身心健康', '身心健康'), ('生活休闲', '生活休闲'), ('情感家庭', '情感家庭'), ('理想信念', '理想信念'), ('教育成长', '教育成长'), ('社团生活', '社团生活'), ('权益保障', '权益保障'), ('政策法规', '政策法规'), ('unknown', 'unknown')], default='unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='youthforumdata',
            name='first_class',
            field=models.CharField(choices=[('人文科技', '人文科技'), ('创业就业', '创业就业'), ('党建团建', '党建团建'), ('身心健康', '身心健康'), ('生活休闲', '生活休闲'), ('情感家庭', '情感家庭'), ('理想信念', '理想信念'), ('教育成长', '教育成长'), ('社团生活', '社团生活'), ('权益保障', '权益保障'), ('政策法规', '政策法规'), ('unknown', 'unknown')], default='unknown', max_length=20),
        ),
        migrations.AlterField(
            model_name='youthforumdata',
            name='second_class',
            field=models.CharField(choices=[('人文科技', [['哲学社会', '哲学社会'], ['文学艺术', '文学艺术'], ['历史地理', '历史地理'], ['科学技术', '科学技术'], ['工业技术', '工业技术'], ['运输工程', '运输工程'], ['环境安全', '环境安全']]), ('创业就业', [['职场人际', '职场人际'], ['创业就业方向', '创业就业方向'], ['创业资质', '创业资质'], ['创业团队', '创业团队'], ['创业项目', '创业项目'], ['创业投资', '创业投资'], ['工作机会', '工作机会'], ['求职面试', '求职面试'], ['实习兼职', '实习兼职']]), ('党建团建', [['党史党章', '党史党章'], ['团章团史', '团章团史'], ['入党入团', '入党入团'], ['党务工作', '党务工作'], ['团务工作', '团务工作'], ['干部培训', '干部培训'], ['基层团建', '基层团建']]), ('身心健康', [['保健养生', '保健养生'], ['美容健体', '美容健体'], ['身体健康', '身体健康'], ['心理咨询', '心理咨询'], ['体育运动', '体育运动']]), ('生活休闲', [['衣食住行', '衣食住行'], ['户外休闲', '户外休闲'], ['娱乐活动', '娱乐活动'], ['数码游戏', '数码游戏'], ['生活服务', '生活服务']]), ('情感家庭', [['亲情', '亲情'], ['友情', '友情'], ['爱情', '爱情'], ['婚姻', '婚姻'], ['孕产', '孕产'], ['育儿', '育儿']]), ('理想信念', [['共产主义', '共产主义'], ['社会主义', '社会主义'], ['爱国主义', '爱国主义'], ['人生观', '人生观'], ['价值观', '价值观'], ['世界观', '世界观'], ['道德观', '道德观']]), ('教育成长', [['校园教育', '校园教育'], ['家庭教育', '家庭教育'], ['社会教育', '社会教育'], ['考研出国', '考研出国'], ['校园生活', '校园生活']]), ('社团生活', [['社团组织', '社团组织'], ['学生组织', '学生组织'], ['公益活动', '公益活动'], ['志愿服务', '志愿服务'], ['社会实践', '社会实践']]), ('权益保障', [['妇女权益保障', '妇女权益保障'], ['劳动者权益保障', '劳动者权益保障'], ['消费者权益保护', '消费者权益保护'], ['社会保障', '社会保障'], ['未成年人保护', '未成年人保护'], ['预防未成年人犯罪', '预防未成年人犯罪'], ['知识产权保护', '知识产权保护']]), ('政策法规', [['时事热点', '时事热点'], ['国情政策', '国情政策'], ['经济政治', '经济政治'], ['文化社会', '文化社会'], ['生态文明', '生态文明'], ['法律法规', '法律法规']]), ('unknown', 'unknown')], default='unknown', max_length=20),
        ),
    ]
