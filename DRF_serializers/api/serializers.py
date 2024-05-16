from rest_framework import serializers

from api.models import Book, Author, Library


class BookHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "url", "title", "author")


class BookTitleReadOnlySerialzer(serializers.BaseSerializer):
    title = serializers.CharField(max_length=128)

    def to_representation(self, instance):
        return {"title": instance.title}


class AuthorHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "url", "first_name", "last_name", "books")
        depth = 1


class CreateBooksListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        books = [Book(**item) for item in validated_data]
        return Book.objects.bulk_create(books)


class CreateManyBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "author")
        list_serializer_class = CreateBooksListSerializer


class LibrarySerializer(serializers.ModelSerializer):
    books = BookHyperlinkSerializer(many=True)

    class Meta:
        model = Library
        fields = ("id", "name", "books")
