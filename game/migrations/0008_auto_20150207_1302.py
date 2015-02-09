# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20150207_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='scoreE',
            field=models.FloatField(default=1.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choice',
            name='scoreF',
            field=models.FloatField(default=1.0),
            preserve_default=True,
        ),
    ]
