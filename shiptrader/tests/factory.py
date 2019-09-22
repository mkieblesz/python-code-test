from shiptrader.models import Listing, Starship


class FixtureFactory:
    def create_single_starship(self):
        return Starship.objects.create(
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

    def create_listings(self):
        starship_data = [
            {
                'name': 'Executor',
                'model': 'Executor-class star dreadnought',
                'starship_class': 'star dreadnought',
                'manufacturer': 'Kuat Drive Yards, Fondor Shipyards',
                'length': 19000,
                'hyperdrive_rating': 2,
                'cargo_capacity': 250000000,
                'crew': 279144,
                'passengers': 38000,
            },
            {
                'name': 'Naboo fighter',
                'model': 'N-1 starfighter',
                'starship_class': 'starfighter',
                'manufacturer': 'Theed Palace Space Vessel Engineering Corps',
                'length': 11,
                'hyperdrive_rating': 1,
                'cargo_capacity': 65,
                'crew': 1,
                'passengers': 0,
            },
            {
                'name': 'Jedi starfighter',
                'model': 'Delta-7 Aethersprite-class interceptor',
                'starship_class': 'starfighter',
                'manufacturer': 'Kuat Systems Engineering',
                'length': 8,
                'hyperdrive_rating': 1,
                'cargo_capacity': 60,
                'crew': 1,
                'passengers': 0,
            },
            {
                'name': 'Y-wing',
                'model': 'BTL Y-wing',
                'starship_class': 'assault starfighter',
                'manufacturer': 'Koensayr Manufacturing',
                'length': 14,
                'hyperdrive_rating': 1,
                'cargo_capacity': 110,
                'crew': 2,
                'passengers': 0,
            },
        ]

        starship_list = []
        for starship in starship_data:
            s = Starship.objects.create(**starship)
            starship_list.append(s)

        s1 = starship_list[0]
        Listing.objects.create(headline='New starship for sale', ship_type=s1, price=200)
        Listing.objects.create(headline='Check out 2020 starship', ship_type=s1, price=999)
        Listing.objects.create(headline='Old but great', ship_type=s1, price=1999, active=False)
        Listing.objects.create(headline='Old, but great', ship_type=starship_list[1], price=9999)
        Listing.objects.create(
            headline='Jedi starfighter for sale', ship_type=starship_list[3], price=100000
        )


fixture_factory = FixtureFactory()  # NOQA
