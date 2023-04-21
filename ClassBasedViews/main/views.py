from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, RedirectView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.utils import timezone

from .models import BookModel


class TimeTemplateView(TemplateView):
    template_name = 'templateView.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = timezone.now()

        return context 
    

class BooksListView(ListView):
    model = BookModel
    queryset = BookModel.objects.all()
    context_object_name = 'books'
    template_name = 'books.html'
    paginate_by = 2

    # def get_queryset(self):
    #     queryset = BookModel.objects.filter(author__icontains='James')
    #     return queryset

class BooksRedirectView(RedirectView):
    pattern_name = 'books-list-view'


class BookDetailView(DetailView):
    model = BookModel
    queryset = BookModel.objects.all()
    context_object_name = 'book'
    template_name = 'book-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = BookModel.objects.get(slug=self.kwargs.get('slug'))
        if book.redirect_counter > 0:
            context['redirect_counter'] = f'Somebody get into that site by RedirectView ({book.redirect_counter} times)'

        return context
    

class BookRedirectView(RedirectView):
    pattern_name = 'book-detail-view'

    def get_redirect_url(self, *args, **kwargs):
        book = BookModel.objects.get(slug=self.kwargs.get('slug'))
        book.redirect_counter += 1
        book.save()

        return super().get_redirect_url(*args, **kwargs)
