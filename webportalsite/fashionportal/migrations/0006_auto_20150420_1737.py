# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fashionportal', '0005_auto_20150420_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postentry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 17, 37, 18, 545044, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
