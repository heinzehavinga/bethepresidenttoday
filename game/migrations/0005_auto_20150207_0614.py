# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20150206_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='event_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 7, 6, 14, 17, 407461, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='choice',
            name='scoreA',
            field=models.FloatField(default=1.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='choice',
            name='scoreB',
            field=models.FloatField(default=1.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='choice',
            name='scoreC',
            field=models.FloatField(default=1.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='choice',
            name='scoreD',
            field=models.FloatField(default=1.0),
            preserve_default=True,
        ),
    ]
