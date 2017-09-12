from django.conf.urls import url


from . import views


urlpatterns = [
    url('^$', views.index, name = "index"),
    url('^previousBid/$', views.reports, name = "previous_bids")
]

