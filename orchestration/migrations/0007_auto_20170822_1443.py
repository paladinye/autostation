# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orchestration', '0006_project_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='dept_logo',
            field=models.FileField(default=1, upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='owner',
            field=models.CharField(default='paladin', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='opser',
            field=models.CharField(default='paladin', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]