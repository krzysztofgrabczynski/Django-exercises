from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to="images/", blank=True)
    created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)
    
class Book(models.Model):
    title = models.CharField(max_length=32)
    authors = models.ManyToManyField(Author)

