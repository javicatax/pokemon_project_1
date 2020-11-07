from django.db import models

# Create your models here.


class Pokemon(models.Model):
    """
    Model to save Pokemon information
    """
    id_pokemon = models.IntegerField(unique=True)
    name = models.CharField(max_length=120)
    base_stats = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    evolutions = models.ManyToManyField('pokemon_api.Evolution', blank=True)

    def __str__(self):
        return '{}'.format(self.id_pokemon)


class Evolution(models.Model):
    """
    Model to save Evolution information
    """
    id_evolution = models.IntegerField(unique=True)
    name = models.CharField(max_length=120)
    evolution_type = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.id_evolution)