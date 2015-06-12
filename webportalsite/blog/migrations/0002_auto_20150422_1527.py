# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='image',
            field=models.ImageField(upload_to='blogphotos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='body_text',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
