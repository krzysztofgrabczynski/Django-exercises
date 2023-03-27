from django import forms
from .models import BaseModel, Film

class AddNewForm(forms.Form):
    title = forms.CharField(max_length=254)
    description = forms.CharField(widget=forms.Textarea)
    type = forms.ChoiceField(choices=BaseModel.TypeChoices.choices)
    price= forms.FloatField()
    is_available = forms.BooleanField(required=False)

    def set_instance(self, instance):
        self.instance = instance
        for key in self.fields:
            if hasattr(instance, key):
                self.fields[key].initial = getattr(instance, key)
