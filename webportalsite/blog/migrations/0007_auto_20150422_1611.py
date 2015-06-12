# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150422_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='image',
            field=models.ImageField(blank=True, null=True, verbose_name='Photo', upload_to='blog-photos'),
            preserve_default=True,
        ),
    ]
