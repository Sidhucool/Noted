# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-04 11:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0009_remove_tag_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listdotags',
            name='listdo',
        ),
        migrations.RemoveField(
            model_name='listdotags',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='notetags',
            name='note',
        ),
        migrations.RemoveField(
            model_name='notetags',
            name='tag',
        ),
        migrations.DeleteModel(
            name='ListDoTags',
        ),
        migrations.DeleteModel(
            name='NoteTags',
        ),
    ]
