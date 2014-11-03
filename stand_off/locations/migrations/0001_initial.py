# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Event name', max_length=256)),
                ('category', models.CharField(verbose_name='Event type', max_length=256)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('grade_received_sum', models.IntegerField()),
                ('grade_received_count', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('address', models.CharField(verbose_name='Address', max_length=256)),
                ('capacity', models.IntegerField(verbose_name='Capacity')),
                ('base_price', models.DecimalField(decimal_places=2, verbose_name='Base price', max_digits=10)),
                ('spring_modifier', models.DecimalField(decimal_places=1, verbose_name='Spring modifier', max_digits=3)),
                ('summer_modifier', models.DecimalField(decimal_places=1, verbose_name='Summer modifier', max_digits=3)),
                ('autumn_modifier', models.DecimalField(decimal_places=1, verbose_name='Autumn modifier', max_digits=3)),
                ('winter_modifier', models.DecimalField(decimal_places=1, verbose_name='Winter modifier', max_digits=3)),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(to='locations.Location'),
            preserve_default=True,
        ),
    ]
