import json

from django.core.management.base import BaseCommand
from pokedex.models import PokemonType, Pokemon


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('pokemon.json', 'r') as file:
            data = file.read()

        all_pokemon = json.loads(data)['pokemon']
        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()

        for pokemon in all_pokemon:
            db_types = []
            for type in pokemon['types']:
                obj, created = PokemonType.objects.get_or_create(name=type)
                db_types.append(obj)
            mon = Pokemon()
            mon.number = pokemon['number']
            mon.name = pokemon['name']
            mon.height = pokemon['height']
            mon.weight = pokemon['weight']
            mon.image_front = pokemon['image_front']
            mon.image_back = pokemon['image_back']
            mon.save()

            for type in db_types:
                print(type)
                mon.types.add(type)

            mon.save()
