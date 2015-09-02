# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20150902_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='timestamp',
            field=models.TimeField(auto_now=True),
        ),
    ]
