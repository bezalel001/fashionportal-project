# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150422_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='photo',
            field=models.ImageField(verbose_name='Photo', blank=True, upload_to='blog-photos', null=True),
            preserve_default=True,
        ),
    ]
