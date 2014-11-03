# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date_start', models.DateTimeField(verbose_name='Reservation start')),
                ('date_end', models.DateTimeField(verbose_name='Reservation end')),
                ('small_stand_count', models.IntegerField()),
                ('medium_stand_count', models.IntegerField()),
                ('large_stand_count', models.IntegerField()),
                ('event', models.ForeignKey(to='locations.Event')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(verbose_name='First name', max_length=20)),
                ('surname', models.CharField(verbose_name='Surname', max_length=20)),
                ('dob', models.DateField()),
                ('oib_user', models.CharField(verbose_name='User OIB', max_length=11)),
                ('email', models.EmailField(verbose_name='Email', max_length=75)),
                ('password', models.CharField(verbose_name='Password', max_length=50)),
                ('trade_name', models.CharField(blank=True, verbose_name='Trade name', max_length=256)),
                ('oib_trade', models.CharField(blank=True, verbose_name='Trade OIB', max_length=11)),
                ('phone', models.CharField(blank=True, verbose_name='Phone', max_length=15)),
                ('mobile', models.CharField(blank=True, verbose_name='Mobile', max_length=15)),
                ('cc_number', models.CharField(blank=True, verbose_name='Credit Card Number', max_length=16)),
                ('grade_received_sum', models.IntegerField()),
                ('grade_received_number', models.IntegerField()),
                ('grade_given_sum', models.IntegerField()),
                ('grade_given_number', models.IntegerField()),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(to='users.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(to='users.User', related_name='owner'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='target_event',
            field=models.ForeignKey(to='locations.Event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='target_user',
            field=models.ForeignKey(to='users.User', related_name='target_user'),
            preserve_default=True,
        ),
    ]
