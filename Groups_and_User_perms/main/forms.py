from django import forms
from .models import BaseModel, Film

class AddNewForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'