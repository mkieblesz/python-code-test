from rest_framework import metadata

from .models import Starship


class ListingViewSetMetadata(metadata.SimpleMetadata):
    def determine_metadata(self, request, view):
        metadata = super().determine_metadata(request, view)
        metadata['starship_class_choices'] = Starship.get_starship_class_choices()
        return metadata
