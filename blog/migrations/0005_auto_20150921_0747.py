# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150921_0746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artical',
            old_name='support',
            new_name='like',
        ),
    ]
