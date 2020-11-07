from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from pokemon_api.data_manager import get_info_pokemon_from_api, get_info_evolution_from_api
from pokemon_api.models import Pokemon
from pokemon_api.serializers import PokemonSerializerHyperLinked, EvolutionSerializerHyperLinked


# Using ViewSet
class PokemonesViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializerHyperLinked

    def list(self, request, *args, **kwargs):
        queryset = Pokemon.objects.all()
        serializer = PokemonSerializerHyperLinked(queryset, many=True)
        return Response(serializer.data)


# Using ApiView
class PokemonApiView(APIView):
    """ Api view """
    serializer_class = PokemonSerializerHyperLinked

    def get_object(self, id_pokemon):
        try:
            return Pokemon.objects.get(id_pokemon=id_pokemon)
        except Pokemon.DoesNotExist:
            raise Http404

    def get(self, request, id_pokemon, format=None):
        """
        Get pokemon data from 'id_pokemon' user requested
        :param request:
        :param id_pokemon:
        :param format:
        :return:
        """
        item = self.get_object(id_pokemon)
        serializer = PokemonSerializerHyperLinked(item)
        return Response(serializer.data)

    def post(self, request, id_pokemon):
        """
        Create Pokemon from Pokemon API information
        :param request:
        :param id_pokemon:
        :return:
        """
        id_pokemon = request.data.get('id_pokemon', None)
        # Get pokemon information from Pokemon data API
        info_pokemon_api = get_info_pokemon_from_api(id_pokemon)
        # Get evolution information from Evolution data API
        info_evolution_api = get_info_evolution_from_api(id_pokemon)
        serializer = self.serializer_class(data=info_pokemon_api)
        serializer_evolution = EvolutionSerializerHyperLinked(data=info_pokemon_api)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return Response({'message': 'Error: {}'.format(e)})
        else:
            return Response({'message': "Pokemon {} could not be created. Pokemon doesn't exists.".format(id_pokemon)})
        if serializer_evolution.is_valid():
            try:
                serializer_evolution.save()
            except Exception as e:
                return Response({'message': 'Error: {}'.format(e)})
        else:
            return Response({'message': "Evolution {} could not be created. Evolution doesn't exists.".format(id_pokemon)})
        return Response({'message': 'Evolution {} created.'.format(id_pokemon)})

    def put(self, request, id_pokemon=None):
        """
        Update an Pokemon with form information
        :param request:
        :param id_pokemon:
        :return:
        """
        # Get item to update
        pokemon = self.get_object(id_pokemon)
        # Update item from form data
        serializer = self.serializer_class(pokemon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        """
        Update an specific field an object
        :param request:
        :param pk:
        :return:
        """
        return Response({'method': 'PATCH'})

    def delete(self, request, id_pokemon=None):
        """
        Delete an pokemon
        :param request:
        :param id_pokemon:
        :return:
        """
        pokemon = self.get_object(id_pokemon)
        pokemon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
