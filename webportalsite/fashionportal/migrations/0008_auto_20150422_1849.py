# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fashionportal', '0007_auto_20150420_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '860x760', size_warning=False, allow_fullsize=False, help_text=None, hide_image_field=False, verbose_name='cropping', free_crop=False, adapt_rotation=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='Describe event here'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postentry',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 4, 22, 18, 49, 30, 50401, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
