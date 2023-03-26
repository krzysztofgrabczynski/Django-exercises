from django import forms
from .models import BaseModel, Film

class AddNewForm(forms.Form):
    # class Meta:
    #     model = Film
    #     fields = ['title', 'description', 'type', 'price', 'is_available']
    title = forms.CharField(max_length=254)
    description = forms.CharField(widget=forms.Textarea)
    type = forms.ChoiceField(choices=BaseModel.TypeChoices.choices)
    price= forms.FloatField()
    is_available = forms.BooleanField(required=False)
