# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Bidder(models.Model):
    name = models.CharField(max_length= 250)
    email = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

class AuctionObject(models.Model):
    name = models.CharField(max_length = 250)
    description = models.TextField(default = "") 
    minAmount = models.IntegerField(default=0)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    itemImage = models.ImageField()
    winner = models.ForeignKey(Bidder,blank=True, null = True)
    bidAmount = models.IntegerField(default=0)
    currentBid = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name


