# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_textsegment'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='t_limit',
            field=models.IntegerField(default=60, verbose_name=b'Time limit, sec'),
        ),
    ]
