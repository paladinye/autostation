# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-07 05:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orchestration', '0017_state_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='statefunctions',
            new_name='statefunction',
        ),
    ]
