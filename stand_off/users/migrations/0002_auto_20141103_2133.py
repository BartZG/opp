# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target_event',
            field=models.ForeignKey(to='locations.Event', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='target_user',
            field=models.ForeignKey(null=True, to='users.User', related_name='target_user'),
            preserve_default=True,
        ),
    ]
