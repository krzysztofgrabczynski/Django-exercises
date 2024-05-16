from rest_framework import viewsets, generics

from api.serializers import (
    BookHyperlinkSerializer,
    AuthorHyperlinkSerializer,
    CreateManyBooksSerializer,
    BookTitleReadOnlySerialzer,
)
from api.models import Book, Author


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookHyperlinkSerializer


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorHyperlinkSerializer


class CreateManyBook(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = CreateManyBooksSerializer

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(many=True, *args, **kwargs)


class BookTitleView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookTitleReadOnlySerialzer
