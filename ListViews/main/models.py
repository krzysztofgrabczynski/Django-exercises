from django.db import models


class Product(models.Model):
    class TypeChoices(models.TextChoices):
        FOOD = 'F'
        ELECTRONIC = 'E'
        CLOTHES = 'C'
        BOOK = 'B'
        OTHER = 'O'

    name = models.CharField(max_length=254)
    price = models.FloatField()
    description = models.TextField()
    type = models.CharField(max_length=10, choices=TypeChoices.choices)
    

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.__str__()