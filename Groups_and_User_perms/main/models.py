from django.db import models


class BaseModel(models.Model):
    class TypeChoices(models.IntegerChoices):
        FILM = 1
        BOOK = 2
        ARTICLE = 3

    title = models.CharField(max_length=254)
    description = models.TextField()
    type = models.CharField(max_length=7, choices=TypeChoices.choices)
    price = models.FloatField()
    is_available = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def get_all_objects(cls):
        objects = []
        for subclass in cls.__subclasses__():
            subclass_objects = subclass.objects.all()
            if subclass_objects:
                objects.extend(subclass_objects)
                
        return objects


class Film(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = self.TypeChoices.FILM

class Book(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = self.TypeChoices.BOOK

class Article(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = self.TypeChoices.ARTICLE
