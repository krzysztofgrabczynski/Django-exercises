from django.shortcuts import render
from .models import Film
from .filters import FilmFilter


def index(request, *args, **kwargs):
    film_filter = FilmFilter(request.GET, queryset=Film.objects.all())

    context = {
        'form': film_filter.form,
        'films': film_filter.qs
    }
    return render(request, 'index.html', context)
