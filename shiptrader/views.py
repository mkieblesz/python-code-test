from django_filters import rest_framework as django_filters
from rest_framework import filters, generics, mixins

from .metadata import ListingListViewMetadata
from .models import Listing, Starship
from .serializers import (
    ListingSerializer,
    ListingUpdateStatusSerializer,
    ListingCreateSerializer,
    StarshipSerializer,
)


class StarshipListView(generics.ListAPIView):
    serializer_class = StarshipSerializer
    queryset = Starship.objects.all()


class ListingRetrieveView(generics.RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ListingListCreateView(generics.ListCreateAPIView):
    metadata_class = ListingListViewMetadata
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ('ship_type__starship_class',)
    ordering_fields = ('price', 'created_at')

    def get_serializer_class(self):
        return ListingCreateSerializer if self.request.method == 'POST' else ListingSerializer


class ListingUpdateStatusView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingUpdateStatusSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
