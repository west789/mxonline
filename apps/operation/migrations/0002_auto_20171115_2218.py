# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 22:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursecomments',
            old_name='courses',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='usercourse',
            old_name='courses',
            new_name='course',
        ),
    ]
