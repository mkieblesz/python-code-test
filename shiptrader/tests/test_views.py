from django.test import TestCase

from shiptrader.models import Listing
from .factory import fixture_factory


class TestListing(TestCase):
    def test_create(self):
        s = fixture_factory.create_single_starship()
        response = self.client.post(
            '/api/v1/listings/', data={'headline': 'test', 'price': 1, 'ship_type': s.id}
        )
        self.assertDictContainsSubset(
            {'id': 1, 'headline': 'test', 'ship_type': s.id, 'price': 1, 'active': True},
            response.json(),
        )

    def test_toggle_activation_status(self):
        s = fixture_factory.create_single_starship()
        listing = Listing.objects.create(ship_type=s, price=1, headline='Test listing')

        self.assertTrue(listing.active)
        self.client.patch('/api/v1/listings/{}/toggle-activation-status/'.format(listing.id))
        listing.refresh_from_db()
        self.assertFalse(listing.active)

        self.client.patch('/api/v1/listings/{}/toggle-activation-status/'.format(listing.id))
        listing.refresh_from_db()
        self.assertTrue(listing.active)

    def test_list_with_order(self):
        fixture_factory.create_listings()

        for order in ['-price', 'price', 'created_at', '-created_at']:
            results = self.client.get('/api/v1/listings/', data={'sort': order}).json()
            self.assertEqual(len(results), 5)

            descending_sort = order.startswith('-')
            order = order.strip('-')
            expected_result = sorted(
                results, key=lambda k: k[order], reverse=descending_sort
            )
            self.assertListEqual(results, expected_result)

    def test_filter_by_starship_class(self):
        fixture_factory.create_listings()
        results = self.client.get(
            '/api/v1/listings/', data={'ship_type__starship_class': 'starfighter'}
        ).json()
        self.assertEqual(len(results), 1)
        self.assertTrue(all(s['ship_type']['starship_class'] == 'starfighter' for s in results))

        results = self.client.get('/api/v1/listings/', data={'ship_type__starship_class': ''}).json()
        self.assertEqual(len(results), 5)

    def test_filter_by_starship_class_options(self):
        fixture_factory.create_single_starship()
        response = self.client.options(
            '/api/v1/listings/', params={'ship_type__starship_class': ''}
        )
        self.assertListEqual(response.json()['starship_class_choices'], ['star dreadnought'])
