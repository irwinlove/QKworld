# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='duoshuo_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='token',
            field=models.IntegerField(default=0),
        ),
    ]
