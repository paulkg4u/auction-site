# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionsite', '0002_auto_20170912_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionobject',
            name='currentBid',
            field=models.IntegerField(default=0),
        ),
    ]
