# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150422_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='photo',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/blog'), upload_to=''),
            preserve_default=True,
        ),
    ]
