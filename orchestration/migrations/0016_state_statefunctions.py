# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-07 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orchestration', '0015_auto_20170906_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='statefunctions',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]