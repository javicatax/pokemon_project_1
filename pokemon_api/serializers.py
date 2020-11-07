from rest_framework import serializers
from pokemon_api.models import Pokemon, Evolution


class PokemonSerializerHyperLinked(serializers.HyperlinkedModelSerializer):
    """
    Serialize Item DB model
    """
    id_pokemon = serializers.CharField(max_length=80)

    class Meta:
        model = Pokemon
        fields = ['id_pokemon', 'name','base_stats', 'height', 'weight', 'evolutions']


class EvolutionSerializerHyperLinked(serializers.HyperlinkedModelSerializer):
    """
    Serialize Evolution DB model
    """
    id_evolution = serializers.CharField(max_length=80)

    class Meta:
        model = Evolution
        fields = ['id_evolution', 'name','evolution_type']
