# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fashionportal', '0004_auto_20150420_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postentry',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 4, 20, 17, 5, 32, 745694, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
