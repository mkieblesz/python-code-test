import requests
from django.core.management.base import BaseCommand

from shiptrader.serializers import StarshipSerializer

STASHIP_ENDPOINT_URL = 'https://swapi.co/api/starships'


def prepare_starship_data(data):
    """Make data returned by starship api to be consistent and fiting model requirements"""

    # treat all unknown values as empty
    for field, value in data.items():
        if isinstance(value, str) and value.lower() == 'unknown':
            data[field] = None

    # remove comma digit grouping from suspect integer and float fields
    # 1,600 becomes 1600
    for field in ['length', 'cargo_capacity', 'crew', 'passengers']:
        if data.get(field, None) is not None and ',' in data[field]:
            data[field] = data[field].replace(',', '')

    # always make starship class lowercase
    data['starship_class'] = data['starship_class'].lower()

    return data


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        url = STASHIP_ENDPOINT_URL

        imported_count = 0
        omitted_count = 0

        self.stdout.write('Starting to import starships.\n')

        while url is not None:
            response = requests.get(url).json()

            starship_list = response['results']
            url = response['next']

            for starship_data in starship_list:
                serializer = StarshipSerializer(data=prepare_starship_data(starship_data))

                if serializer.is_valid():
                    serializer.save()
                    imported_count += 1
                else:
                    # serializer validator checks for uniqueness already
                    omitted_count += 1

            # display progress
            percent = (imported_count + omitted_count) / response['count']
            self.stdout.write('[{:<{}}] {:.0f}%'.format('=' * int(20 * percent), 20, percent * 100))

        self.stdout.write('\nSummary:\n')
        self.stdout.write(f'Successfully imported {imported_count} starships')
        self.stdout.write(f'Omitted {omitted_count} already existing starships')
