# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 10:21
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projekty', '0002_nazwa_zdjecie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nazwa',
            name='zdjecie',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to=b''),
        ),
    ]