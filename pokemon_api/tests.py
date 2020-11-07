import requests
from django.test import TestCase


# Create your tests here.
from pokemon_api.data_manager import get_info_pokemon_from_api
from pokemon_api.serializers import PokemonSerializerHyperLinked


class TestApiConnections(TestCase):

    def setUp(self):
        self.url_pokemon_data_api = "https://pokeapi.co/api/v2/pokemon/12"
        self.url_pokemon_evolution_chain_api = "https://pokeapi.co/api/v2/evolution-chain/12"

    def test_url_pokemon_data_api_check_status_code_equals_200(self):
        response = requests.get(self.url_pokemon_data_api)
        self.assertEqual(response.status_code, 200)

    def test_url_pokemon_evolution_chain_api_status_code_equals_200(self):
        response = requests.get(self.url_pokemon_evolution_chain_api)
        print(response)
        self.assertEqual(response.status_code, 200)


class TestDataManager(TestCase):

    def setUp(self):
        self.id_pokemon = 12

    def test_data_manager_function(self):
        info = get_info_pokemon_from_api(self.id_pokemon)
        self.assertEqual(info["id_pokemon"], str(self.id_pokemon))


class TestSerializers(TestCase):

    def setUp(self):
        self.id_pokemon = 12
        self.data = {'id_pokemon':12,
                     'price': '1000',
                     'start_time': None,
                     'name': "Test"}

    def test_serializer_create(self):
        serializer = PokemonSerializerHyperLinked(data=self.data)
        valid = serializer.is_valid(raise_exception=True)
        self.assertEqual(True, valid)
        serializer.save()
        self.assertEqual(serializer.data["item_id"], str(self.id_pokemon))
