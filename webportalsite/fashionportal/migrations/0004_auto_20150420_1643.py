# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fashionportal', '0003_postentry_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postentry',
            name='posted_by',
            field=models.OneToOneField(to='fashionportal.UserProfile', primary_key=True, serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postentry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 16, 43, 11, 964448, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
