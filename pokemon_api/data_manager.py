from pokemon_api.api_connections import get_all_data_pokemon_api_chain_evolution, get_all_data_pokemon_api_data


def get_info_pokemon_from_api(item_id):
    """
    Get item information from Mercado Libre API
    :param item_id:
    :return: info item
    """
    info_pokemon = {}
    # Get data from pokemon evolution chain API
    all_data_pokemon_api_chain_evolution = get_all_data_pokemon_api_chain_evolution(item_id)
    # Get data from pokemon data API
    all_data_pokemon_api_data = get_all_data_pokemon_api_data(item_id)
    info_pokemon['id_pokemon'] = all_data_pokemon_api_data.get('id', None)
    info_pokemon['name'] = all_data_pokemon_api_data.get('name', None)
    info_pokemon['height'] = all_data_pokemon_api_data.get('height', None)
    info_pokemon['weight'] = all_data_pokemon_api_data.get('weight', None)
    return info_pokemon


def get_info_evolution_from_api(item_id):
    """
    Get item information from Mercado Libre API
    :param item_id:
    :return: info item
    """
    info_evolution = {}
    # Get data from pokemon evolution chain API
    all_data_pokemon_api_chain_evolution = get_all_data_pokemon_api_chain_evolution(item_id)
    info_evolution['id_evolution'] = all_data_pokemon_api_chain_evolution.get('id', None)
    info_evolution['name'] = all_data_pokemon_api_chain_evolution.get('name', None)
    info_evolution['type'] = all_data_pokemon_api_chain_evolution.get('type', None)
    return info_evolution
