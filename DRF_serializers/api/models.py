from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return str(self.first_name) + " " + str(self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books"
    )

    def __str__(self) -> str:
        return str(self.title)
