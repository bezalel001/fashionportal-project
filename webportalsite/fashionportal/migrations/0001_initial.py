# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('post_code', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255, default=None)),
                ('date', models.DateTimeField(default=None)),
                ('image', models.ImageField(blank=True, upload_to='events')),
                ('address', models.OneToOneField(default=None, to='fashionportal.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(blank=True, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LargePictures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('imageTitle', models.CharField(max_length=200)),
                ('largeImage', models.ImageField(blank=True, upload_to='gallery', verbose_name='Photo')),
                ('cropping', image_cropping.fields.ImageRatioField('largeImage', '860x760', free_crop=False, verbose_name='cropping', hide_image_field=False, size_warning=False, allow_fullsize=False, help_text=None, adapt_rotation=False)),
                ('gallery', models.ForeignKey(to='fashionportal.Gallery')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('headline', models.CharField(blank=True, max_length=255)),
                ('body', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='news')),
                ('pub_date', models.DateTimeField(default=None, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('imageTitle', models.CharField(max_length=200)),
                ('smallImage', models.ImageField(blank=True, upload_to='gallery', verbose_name='Photo')),
                ('cropping', image_cropping.fields.ImageRatioField('smallImage', '1290x1080', free_crop=False, verbose_name='cropping', hide_image_field=False, size_warning=False, allow_fullsize=False, help_text=None, adapt_rotation=False)),
                ('gallery', models.ForeignKey(to='fashionportal.Gallery')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(default=None, to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('bio', models.TextField(null=True)),
                ('phone', models.CharField(null=True, max_length=255)),
                ('profile_image', models.ImageField(blank=True, upload_to='photos', null=True, verbose_name='Photo')),
                ('occupation', models.CharField(choices=[('DESIGNER', 'Designer'), ('MODEL', 'Model'), ('TAILOR', 'Tailor'), ('PHOTOGRAPHER', 'Photographer')], max_length=50, default=None)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('date_of_birth', models.DateField(blank=True, null=True, default=None)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('cropping', image_cropping.fields.ImageRatioField('profile_image', '430x360', free_crop=False, verbose_name='cropping', hide_image_field=False, size_warning=False, allow_fullsize=False, help_text=None, adapt_rotation=False)),
                ('brand_name', models.CharField(blank=True, null=True, max_length=255)),
                ('location', models.CharField(blank=True, null=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tailor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(to='fashionportal.UserProfile', auto_created=True, primary_key=True, serialize=False, parent_link=True)),
            ],
            options={
            },
            bases=('fashionportal.userprofile',),
        ),
        migrations.CreateModel(
            name='PostEntry',
            fields=[
                ('posted_by', models.ForeignKey(to='fashionportal.UserProfile', primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='post-photos', verbose_name='Photo', default='Images', null=True)),
                ('cropping', image_cropping.fields.ImageRatioField('photo', '430x360', free_crop=False, verbose_name='cropping', hide_image_field=False, size_warning=False, allow_fullsize=False, help_text=None, adapt_rotation=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('userprofile_ptr', models.OneToOneField(to='fashionportal.UserProfile', auto_created=True, primary_key=True, serialize=False, parent_link=True)),
            ],
            options={
            },
            bases=('fashionportal.userprofile',),
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('userprofile_ptr', models.OneToOneField(to='fashionportal.UserProfile', auto_created=True, primary_key=True, serialize=False, parent_link=True)),
            ],
            options={
            },
            bases=('fashionportal.userprofile',),
        ),
        migrations.CreateModel(
            name='FashionDesigner',
            fields=[
                ('userprofile_ptr', models.OneToOneField(to='fashionportal.UserProfile', auto_created=True, primary_key=True, serialize=False, parent_link=True)),
            ],
            options={
            },
            bases=('fashionportal.userprofile',),
        ),
    ]
