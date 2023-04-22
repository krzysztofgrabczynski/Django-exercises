from django.urls import path
from django.views.generic import TemplateView

from .views import *


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('template-view/', TimeTemplateView.as_view(), name='template-view'),
    path('books-list-view/', BooksListView.as_view(), name='books-list-view'),
    path('books-redirect-view/', BooksRedirectView.as_view(), name='books-redirect-view'),
    path('book-detail-view/<slug:slug>', BookDetailView.as_view(), name='book-detail-view'),
    path('book-redirect-view/<slug:slug>', BookRedirectView.as_view(), name='book-redirect-view'),
    path('book-form-view/', AddBookFormView.as_view(), name='book-form-view'),
    path('create-book-create-view/', AddBookCreateView.as_view(), name='create-book-create-view'),
    path('edit-book-update-view/<int:pk>', EditBookUpdateView.as_view(), name='edit-book-update-view'),

]
