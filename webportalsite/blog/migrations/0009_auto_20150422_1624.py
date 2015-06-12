# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150422_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/blog'), upload_to=''),
            preserve_default=True,
        ),
    ]
