# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 16:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projekty', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nazwa',
            name='data_publikacji',
        ),
    ]
