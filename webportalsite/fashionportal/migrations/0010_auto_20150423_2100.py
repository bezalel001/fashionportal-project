# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import image_cropping.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fashionportal', '0009_auto_20150423_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('document', models.FileField(upload_to='job', verbose_name='Upload CV ')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('website', models.URLField(max_length=255)),
                ('image', models.ImageField(upload_to='shop', null=True, blank=True, verbose_name='Photo')),
                ('cropping', image_cropping.fields.ImageRatioField('image', '860x760', hide_image_field=False, size_warning=False, free_crop=False, help_text=None, adapt_rotation=False, allow_fullsize=False, verbose_name='cropping')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='postentry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 23, 21, 0, 53, 938600, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
