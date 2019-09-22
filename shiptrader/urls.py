from rest_framework import routers

from .views import ListingViewSet, StarshipViewSet

router = routers.DefaultRouter()

router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'starships', StarshipViewSet, basename='starship')
