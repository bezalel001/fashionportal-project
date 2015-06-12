# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fashionportal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postentry',
            name='pub_date',
        ),
    ]
