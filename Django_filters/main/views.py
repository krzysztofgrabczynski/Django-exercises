from django.shortcuts import render
from .models import Film
from .filters import FilmFilter
from django.views.generic import ListView


def index(request, *args, **kwargs):
    film_filter = FilmFilter(request.GET, queryset=Film.objects.all())

    context = {
        'filter': film_filter.form,
        'films': film_filter.qs
    }
    return render(request, 'index.html', context)


class FilmListView(ListView):
    template_name = 'index.html'
    queryset = Film.objects.all()
    context_object_name = 'films'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = FilmFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset.form
        return context