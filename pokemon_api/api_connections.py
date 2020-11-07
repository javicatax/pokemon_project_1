import requests
from rest_framework.response import Response

from pokemon_project_1.settings import URL_API_POKEMON


URL_API_POKEMON_EVOLUTION_CHAIN = URL_API_POKEMON + "evolution-chain/"
URL_API_POKEMON_DATA = URL_API_POKEMON + "pokemon/"


def get_all_data_pokemon_api_chain_evolution(id_pokemon):
    """
    Request information from Mercado Libre API Categories
    :param item_id:
    :return:
    """
    url_get_pokemon_data = URL_API_POKEMON_EVOLUTION_CHAIN + "{}/".format(id_pokemon)
    response = requests.get(url_get_pokemon_data)
    if response.status_code != 200:
        return Response({'message': 'Pokemon {} not found API Pokemon evolution chain.'.format(id_pokemon)})
    return response.json()


def get_all_data_pokemon_api_data(id_pokemon):
    """
    Request information from Mercado Libre API items
    :param item_id:
    :return:
    """
    url_get_pokemon_data = URL_API_POKEMON_DATA + "{}/".format(id_pokemon)
    response = requests.get(url_get_pokemon_data)
    if response.status_code != 200:
        return Response({'message': 'Pokemon {} not found API Pokemon data.'.format(id_pokemon)})
    return response.json()