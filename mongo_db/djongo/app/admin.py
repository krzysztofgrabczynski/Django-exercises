from django.contrib import admin

from .models import Post, Comment, Book, Author


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Book)
admin.site.register(Author)