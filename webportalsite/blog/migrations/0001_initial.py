# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('tagline', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('author', models.CharField(max_length=255)),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField()),
                ('image', models.ImageField(upload_to='blog-photos', blank=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('mod_date', models.DateTimeField(auto_now=True)),
                ('n_comments', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('author', models.CharField(max_length=64, verbose_name='Name')),
                ('body_text', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('blog_entry', models.ForeignKey(to='blog.BlogEntry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
