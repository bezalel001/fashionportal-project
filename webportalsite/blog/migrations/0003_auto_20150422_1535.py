# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150422_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '430x360', verbose_name='cropping', free_crop=False, adapt_rotation=False, size_warning=False, help_text=None, hide_image_field=False, allow_fullsize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='body_text',
            field=models.TextField(verbose_name='Comment'),
            preserve_default=True,
        ),
    ]
