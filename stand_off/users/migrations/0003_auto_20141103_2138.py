# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20141103_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target_event',
            field=models.ForeignKey(blank=True, to='locations.Event', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='target_user',
            field=models.ForeignKey(blank=True, related_name='target_user', to='users.User', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='large_stand_count',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='medium_stand_count',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='small_stand_count',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
