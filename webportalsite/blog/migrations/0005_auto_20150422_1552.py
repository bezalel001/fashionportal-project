# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150422_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog', null=True),
            preserve_default=True,
        ),
    ]
