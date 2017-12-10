# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-08 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessage',
            name='id',
        ),
        migrations.AddField(
            model_name='usermessage',
            name='object_id',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u7528\u6237\u540d'),
        ),
    ]