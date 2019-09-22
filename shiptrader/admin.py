from django.contrib import admin

from .models import Starship, Listing


@admin.register(Starship)
class StarshipAdmin(admin.ModelAdmin):
    list_display = (
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


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('headline', 'ship_type', 'created_at', 'active', 'price')
