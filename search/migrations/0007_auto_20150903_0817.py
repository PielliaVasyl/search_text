# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_search_t_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='t_limit',
            field=models.PositiveSmallIntegerField(default=60, verbose_name=b'Time limit, sec'),
        ),
    ]
