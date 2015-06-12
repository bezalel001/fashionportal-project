# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150422_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogentry',
            old_name='image',
            new_name='photo',
        ),
        migrations.AlterField(
            model_name='blogentry',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('photo', '430x360', allow_fullsize=False, help_text=None, hide_image_field=False, adapt_rotation=False, verbose_name='cropping', free_crop=False, size_warning=False),
            preserve_default=True,
        ),
    ]
