# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fashionportal', '0008_auto_20150422_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '860x760', adapt_rotation=False, size_warning=False, free_crop=False, help_text=None, hide_image_field=False, allow_fullsize=False, verbose_name='cropping'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postentry',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 4, 23, 20, 5, 41, 986706, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
