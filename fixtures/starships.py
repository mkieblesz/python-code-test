from shiptrader.models import Starship, Listing

s1, _ = Starship.objects.get_or_create(
    **{
        'name': 'Executor',
        'model': 'Executor-class star dreadnought',
        'starship_class': 'star dreadnought',
        'manufacturer': 'Kuat Drive Yards, Fondor Shipyards',
        'length': 19000,
        'hyperdrive_rating': 2,
        'cargo_capacity': 250000000,
        'crew': 279144,
        'passengers': 38000,
    }
)
Listing.objects.get_or_create(headline='New starship for sale', ship_type=s1, price=200)
Listing.objects.get_or_create(headline='Check out 2020 starship', ship_type=s1, price=999)
Listing.objects.get_or_create(headline='Old but great', ship_type=s1, price=1999, active=False)

s2, _ = Starship.objects.get_or_create(
    **{
        'name': 'Naboo fighter',
        'model': 'N-1 starfighter',
        'starship_class': 'starfighter',
        'manufacturer': 'Theed Palace Space Vessel Engineering Corps',
        'length': 11,
        'hyperdrive_rating': 1,
        'cargo_capacity': 65,
        'crew': 1,
        'passengers': 0,
    }
)
Listing.objects.get_or_create(headline='Old, but great', ship_type=s2, price=9999)

s3, _ = Starship.objects.get_or_create(
    **{
        'name': 'Jedi starfighter',
        'model': 'Delta-7 Aethersprite-class interceptor',
        'starship_class': 'starfighter',
        'manufacturer': 'Kuat Systems Engineering',
        'length': 8,
        'hyperdrive_rating': 1,
        'cargo_capacity': 60,
        'crew': 1,
        'passengers': 0,
    }
)
Listing.objects.get_or_create(headline='Jedi starfighter for sale', ship_type=s3, price=100000)

Starship.objects.get_or_create(
    **{
        'name': 'Y-wing',
        'model': 'BTL Y-wing',
        'starship_class': 'assault starfighter',
        'manufacturer': 'Koensayr Manufacturing',
        'length': 14,
        'hyperdrive_rating': 1,
        'cargo_capacity': 110,
        'crew': 2,
        'passengers': 0,
    }
)
