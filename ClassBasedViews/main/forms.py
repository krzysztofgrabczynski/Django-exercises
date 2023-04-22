from django.forms import ModelForm

from .models import BookModel


class BookForm(ModelForm):
    class Meta:
        model = BookModel
        exclude = ('slug', 'redirect_counter',)