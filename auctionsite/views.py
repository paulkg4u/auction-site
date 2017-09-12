# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import  timezone

from auctionsite.models import  AuctionObject
from auctionsite.models import  Bidder
# Create your views here.

def index(request):
    currentTime = timezone.now()
    liveAuction = AuctionObject.objects.filter(startTime__lte=currentTime, endTime__gte=currentTime)
    if len(liveAuction):
        response = {'liveAuction':liveAuction[0], 'hasLiveAuction':True}
    else:
        nextAuction = AuctionObject.objects.filter(startTime__gte=currentTime).order_by('startTime')
        if len(nextAuction):
            response = {'upcomingAuction':nextAuction[0],'hasLiveAuction':False}
        else:
            response = {'upcomingAuction':False,'hasLiveAuction':False}
    print response
    return render(request,'auction_site/index.html',response)


def reports(request):
    currentTime = timezone.now()
    previousAuctions = AuctionObject.objects.filter(endTime__lte=currentTime)
    print previousAuctions
    response = {'previousAuctions':previousAuctions}
    return render(request,'auction_site/reports.html', response)


def viewAuction(request, auctionId):
    auction = AcutionObject.objects.get(id = auctionId)
    response = {'auctionObject':auction}
    return render(request, 'auction_site/product.html', response)

def bid(request, auctionId):
    auctionObject = AuctionObject.objects.get(id = auctionId)
    pass

