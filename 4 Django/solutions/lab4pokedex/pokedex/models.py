from django.db import models

# Create your models here.


class PokemonType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.URLField()
    image_back = models.URLField()
    types = models.ManyToManyField(PokemonType, related_name="pokemon")

    def __str__(self):
        return self.name
