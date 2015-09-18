# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('commentTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Replys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('replyTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(to='blog.Comments')),
                ('replyer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='artical',
            old_name='publish_time',
            new_name='publishTime',
        ),
        migrations.RenameField(
            model_name='artical',
            old_name='update_time',
            new_name='updateTime',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='create_time',
            new_name='createTime',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag_name',
            new_name='tagName',
        ),
        migrations.AddField(
            model_name='comments',
            name='artical',
            field=models.ForeignKey(to='blog.Artical'),
        ),
        migrations.AddField(
            model_name='comments',
            name='commentor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
