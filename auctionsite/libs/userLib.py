from auctionsite.models import Bidder

def getOrCreateBidder(email,name):
    try:
        bidder = Bidder.objects.get(email = email)
        return bidder
    except:
        bidder = Bidder.objects.create(
            name = name,
            email = email
        )
        return bidder

