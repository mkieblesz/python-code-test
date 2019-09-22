from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Listing, Starship


class StarshipSerializer(ModelSerializer):
    class Meta:
        model = Starship
        fields = (
            'id',
            'name',
            'model',
            'starship_class',
            'manufacturer',
            'length',
            'hyperdrive_rating',
            'cargo_capacity',
            'crew',
            'passengers',
        )


class ListingSerializer(ModelSerializer):
    active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Listing
        fields = ('id', 'headline', 'ship_type', 'price', 'created_at', 'active')


class ListingListSerializer(ModelSerializer):
    ship_type = StarshipSerializer(read_only=True)

    class Meta:
        model = Listing
        fields = ('id', 'headline', 'ship_type', 'price', 'created_at', 'active')
