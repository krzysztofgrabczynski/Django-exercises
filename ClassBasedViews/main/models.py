from django.db import models
from django.template.defaultfilters import slugify


class BookModel(models.Model):
    title = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=254, blank=False, null=True)
    author = models.CharField(max_length=254)
    price = models.IntegerField()
    redirect_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)