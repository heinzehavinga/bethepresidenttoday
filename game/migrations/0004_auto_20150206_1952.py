# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_problem_actual_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='actual_result_media_url',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='background_media_url',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
