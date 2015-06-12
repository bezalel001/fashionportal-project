# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fashionportal', '0010_auto_20150423_2100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'ordering': ['-pub_date'], 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'ordering': ['name'], 'verbose_name_plural': []},
        ),
        migrations.AlterField(
            model_name='postentry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 5, 54, 22, 218186, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
