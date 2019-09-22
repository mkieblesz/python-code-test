from rest_framework.test import APITestCase

from shiptrader.models import Listing, Starship

STARSHIP_DATA = {
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


class ListingCreateViewTestCase(APITestCase):
    def test_create(self):
        starship = Starship.objects.create(**STARSHIP_DATA)

        result = self.client.post(
            '/api/v1/listings/', data={'headline': 'test', 'price': 1, 'ship_type': starship.id}
        ).json()
        expected_result = {
            'id': 1,
            'headline': 'test',
            'ship_type': starship.id,
            'price': 1,
            'active': True,
        }
        # don't take created_at field into account
        self.assertDictContainsSubset(expected_result, result)
        self.assertEqual(Listing.objects.count(), 1)


class ListingUpdateStatusViewTestCase(APITestCase):
    def test_update_listing_status(self):
        starship = Starship.objects.create(**STARSHIP_DATA)
        listing = Listing.objects.create(headline='test', price=1, ship_type=starship)
        self.assertTrue(listing.active)

        self.client.patch(
            '/api/v1/listings/{}/update-status/'.format(listing.id), data={'active': False}
        )
        listing.refresh_from_db()
        self.assertFalse(listing.active)

        self.client.patch(
            '/api/v1/listings/{}/update-status/'.format(listing.id), data={'active': True}
        )
        listing.refresh_from_db()
        self.assertTrue(listing.active)


class ListingListViewTestCase(APITestCase):
    fixtures = ['shiptrader/tests/data/listings.json']

    def test_list_with_order(self):
        for order in ['-price', 'price', 'created_at', '-created_at']:
            results = self.client.get('/api/v1/listings/', data={'sort': order}).json()
            self.assertEqual(len(results), 5)

            descending_sort = order.startswith('-')
            order = order.strip('-')
            expected_result = sorted(results, key=lambda k: k[order], reverse=descending_sort)
            self.assertListEqual(results, expected_result)

    def test_list_with_filter_by_starship_class(self):
        results = self.client.get(
            '/api/v1/listings/', data={'ship_type__starship_class': 'starfighter'}
        ).json()
        self.assertEqual(len(results), 2)
        self.assertTrue(
            all(starship['ship_type']['starship_class'] == 'starfighter' for starship in results)
        )

        results = self.client.get(
            '/api/v1/listings/', data={'ship_type__starship_class': ''}
        ).json()
        self.assertEqual(len(results), 5)

    def test_starship_class_choices(self):
        results = self.client.options(
            '/api/v1/listings/', params={'ship_type__starship_class': ''}
        ).json()
        self.assertListEqual(
            results['starship_class_choices'],
            ['star dreadnought', 'starfighter', 'assault starfighter'],
        )
