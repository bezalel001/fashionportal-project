# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fashionportal', '0002_remove_postentry_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='postentry',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 4, 19, 12, 51, 10, 912461, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
