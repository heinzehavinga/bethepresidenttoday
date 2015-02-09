# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20150206_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='actual_result',
            field=models.TextField(default=b'What happend in reallife'),
            preserve_default=True,
        ),
    ]
