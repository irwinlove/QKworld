# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150921_0747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artical',
            old_name='like',
            new_name='likes',
        ),
        migrations.RenameField(
            model_name='artical',
            old_name='view',
            new_name='views',
        ),
    ]
