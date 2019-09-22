from django.conf.urls import url

from .views import (
    ListingListCreateView,
    ListingRetrieveView,
    ListingUpdateStatusView,
    StarshipListView,
)

urlpatterns = [
    url(r'listings/$', ListingListCreateView.as_view()),
    url(r'listings/(?P<pk>[\d]+)/$', ListingRetrieveView.as_view()),
    url(r'listings/(?P<pk>[\d]+)/update-status/$', ListingUpdateStatusView.as_view()),
    url(r'starships/$', StarshipListView.as_view()),
]
