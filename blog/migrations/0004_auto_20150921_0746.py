# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150915_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='summary',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='artical',
            name='support',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='artical',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
