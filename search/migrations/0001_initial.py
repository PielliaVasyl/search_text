# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('searching_text', models.CharField(default=b'put search text here', max_length=150, verbose_name=b'Search text')),
                ('email', models.EmailField(default=b'put your email here', max_length=254, verbose_name=b'E-mail to send response')),
                ('timestamp', models.TimeField(auto_now=True)),
            ],
        ),
    ]
