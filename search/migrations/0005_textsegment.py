# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20150902_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextSegment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('book', models.CharField(max_length=300)),
                ('chapter', models.CharField(max_length=300)),
                ('page', models.IntegerField()),
            ],
        ),
    ]
