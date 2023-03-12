import django_filters
from .models import Film


class FilmFilter(django_filters.FilterSet):
    imdb_rating = django_filters.NumberFilter()
    imdb_rating__lt = django_filters.NumberFilter(field_name='imdb_rating', lookup_expr='lt')
    imdb_rating__gt = django_filters.NumberFilter(field_name='imdb_rating', lookup_expr='gt')

    class Meta:
        model = Film
        fields = {
            'title': ['icontains'],
            'category': ['exact'],
            'premiere': ['exact'],
            'year': ['lt', 'gt'],
            'director': ['icontains'],
        }