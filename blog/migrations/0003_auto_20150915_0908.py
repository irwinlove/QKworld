# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150915_0655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='artical',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='commentor',
        ),
        migrations.RemoveField(
            model_name='replys',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='replys',
            name='replyer',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Replys',
        ),
    ]
