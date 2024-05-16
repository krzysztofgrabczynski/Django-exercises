from rest_framework import viewsets

from api.models import Author, Book, Library
from api import serializers


class LibraryViewset(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = serializers.LibrarySerializer

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return serializers.LibraryReadOnlySerializer

        return self.serializer_class


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return serializers.BookReadOnlySerializer

        return self.serializer_class

    def get_queryset(self):
        q = super().get_queryset()
        library_pk = self.kwargs.get("library_pk", None)
        if library_pk:
            return q.filter(library=library_pk)
        return q

    def perform_create(self, serializer):
        book = serializer.save()
        if "library_pk" in self.kwargs:
            library = Library.objects.get(pk=self.kwargs["library_pk"])
            library.books.add(book)


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer

    def get_queryset(self):
        q = super().get_queryset()
        book_pk = self.kwargs.get("books_pk", None)
        if book_pk:
            return q.filter(books=book_pk)
        return q
