# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 17:53
from __future__ import unicode_literals

import Notes.current_user
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0003_auto_20160726_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listcontent',
            name='content',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='listdo',
            name='user',
            field=models.ForeignKey(default=Notes.current_user.get_current_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='note',
            name='user',
            field=models.ForeignKey(default=Notes.current_user.get_current_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
