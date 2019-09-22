import io
import requests_mock
from django.core.management import call_command
from django.test import TestCase

from shiptrader.management.commands.import_starships import prepare_starship_data
from shiptrader.models import Starship


class TestImportStarships(TestCase):
    @requests_mock.Mocker()
    def test_handle(self, m):
        # mock requests responses
        with open('shiptrader/tests/data/first_page.json', 'r') as f:
            m.get('https://swapi.co/api/starships', text=f.read())
        with open('shiptrader/tests/data/second_page.json', 'r') as f:
            m.get('https://swapi.co/api/starships/?page=2', text=f.read())

        # capture command output
        cmd_out_stream = io.StringIO()
        call_command('import_starships', stdout=cmd_out_stream)
        captured_output = cmd_out_stream.getvalue()

        # test command output
        self.assertIn('Successfully imported 20 starships', captured_output)
        self.assertIn('Omitted 0 already existing starships', captured_output)

        # test database state
        self.assertEqual(Starship.objects.count(), 20)

        # second command execution should omit all starships since they are already existing
        cmd_out_stream = io.StringIO()
        call_command('import_starships', stdout=cmd_out_stream)
        captured_output = cmd_out_stream.getvalue()

        self.assertIn('Successfully imported 0 starships', captured_output)
        self.assertIn('Omitted 20 already existing starships', captured_output)
        self.assertEqual(Starship.objects.count(), 20)

    def test_prepare_starship_data(self):
        data = {
            'starship_class': 'Upper class',
            'cargo_capacity': None,
            'passengers': 'unknown',
            'length': '1,600',
        }
        expected_result = {
            'starship_class': 'upper class',
            'cargo_capacity': None,
            'passengers': None,
            'length': '1600',
        }

        self.assertDictEqual(prepare_starship_data(data), expected_result)
