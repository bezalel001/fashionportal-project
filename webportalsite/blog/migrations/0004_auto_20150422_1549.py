# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150422_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='image',
            field=models.ImageField(upload_to='blog', blank=True),
            preserve_default=True,
        ),
    ]
