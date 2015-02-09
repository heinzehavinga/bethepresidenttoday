# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20150207_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='actual_result_source',
            field=models.TextField(default=b'Put your source here'),
            preserve_default=True,
        ),
    ]
