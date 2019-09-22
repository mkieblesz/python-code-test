from django_filters import rest_framework as django_filters
from rest_framework import filters, mixins, viewsets, decorators, response

from .metadata import ListingViewSetMetadata
from .models import Listing, Starship
from .serializers import ListingSerializer, ListingListSerializer, StarshipSerializer


class StarshipViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StarshipSerializer
    queryset = Starship.objects.all()


class ListingViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    metadata_class = ListingViewSetMetadata
    queryset = Listing.objects.all()

    filter_backends = [django_filters.DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['ship_type__starship_class']
    ordering_fields = ['price', 'created_at']

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return ListingSerializer
        return ListingListSerializer

    @decorators.action(detail=True, methods=['PATCH'], url_path='toggle-activation-status')
    def toggle_activation_status(self, request, pk=None):
        listing = self.get_object()
        listing.active = not listing.active
        listing.save()

        return response.Response(ListingSerializer(listing).data)
