from django.db import models
from uuid import uuid4


class Film(models.Model):
    class CategoryChoices(models.TextChoices):
        SCI_FI = 'SF'
        DRAMA = 'D'
        ADVENTURE = 'AV'
        COMEDY = 'C'
        ACTION = 'A'
        OTHER = 'O'
        
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=128, blank=False)
    category = models.CharField(max_length=2, choices=CategoryChoices.choices, default=CategoryChoices.OTHER)
    description = models.TextField(blank=False)
    year = models.PositiveSmallIntegerField(blank=False, default=2000)
    premiere = models.DateField(blank=False)
    imdb_rating = models.DecimalField(blank=False, max_digits=4, decimal_places=2)
    director = models.CharField(max_length=256, blank=False)


