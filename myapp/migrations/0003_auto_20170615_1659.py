# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 16:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20170518_2132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'Students'},
        ),
    ]
