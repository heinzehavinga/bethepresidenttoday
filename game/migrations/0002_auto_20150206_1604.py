# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='resultText',
            field=models.TextField(default=b'This is the resolution text'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='problem',
            name='text',
            field=models.TextField(default=b'Put your problem here'),
            preserve_default=True,
        ),
    ]
