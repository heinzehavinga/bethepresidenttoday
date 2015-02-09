# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_problem_actual_result_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='actual_result_title',
            field=models.CharField(default='Set a title!', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='tweet',
            field=models.CharField(default='a glorious tweet', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='tweet_link',
            field=models.CharField(default='https://twitter.com/presidentaz/status/563988347035463680', max_length=255),
            preserve_default=False,
        ),
    ]
