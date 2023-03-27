from django.db import models
from polymorphic.query import PolymorphicQuerySet
from uuid import uuid4


class BaseModel(models.Model):
    class TypeChoices(models.IntegerChoices):
        FILM = 0
        BOOK = 1
        ARTICLE = 2

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    title = models.CharField(max_length=254)
    description = models.TextField()
    type = models.IntegerField(choices=TypeChoices.choices)
    price = models.FloatField()
    is_available = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return self.__str__()

    class SubclassesContextManager:
        def __init__(self) -> None:
            self.subclasses = BaseModel.__subclasses__()

        def __enter__(self):
            for subclass in self.subclasses:
                yield subclass
            
        def __exit__(self, exc_type, exc_value, trace):
            pass


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
