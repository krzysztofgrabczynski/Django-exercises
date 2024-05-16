from django.contrib import admin

from api.models import Author, Book, Library


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
