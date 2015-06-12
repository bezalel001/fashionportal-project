# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fashionportal', '0006_auto_20150420_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postentry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 18, 12, 26, 55259, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
