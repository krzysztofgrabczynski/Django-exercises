from rest_framework import serializers

from api.models import Author, Book, Library


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("first_name", "last_name")


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "author")


class BookReadOnlySerializer(serializers.ModelSerializer):
    library = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ("title", "author", "library")
        depth = 1

    def get_library(self, obj):
        library = obj.library.first()
        return library.name if library else None


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ("name", "books")


class LibraryReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ("name", "books")
        depth = 1
