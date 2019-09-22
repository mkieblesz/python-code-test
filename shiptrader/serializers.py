from rest_framework import serializers

from .models import Listing, Starship


class StarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starship
        fields = '__all__'


class ListingSerializer(serializers.ModelSerializer):
    ship_type = StarshipSerializer()

    class Meta:
        model = Listing
        fields = '__all__'


class ListingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        read_only_fields = ('active', 'created_at')


class ListingUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        read_only_fields = ('headline', 'ship_type', 'created_at', 'price')
