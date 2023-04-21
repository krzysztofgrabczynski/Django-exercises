from django.db import models


class BookModel(models.Model):
    title = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=254, blank=False)
    author = models.CharField(max_length=254)
    price = models.IntegerField()

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()

