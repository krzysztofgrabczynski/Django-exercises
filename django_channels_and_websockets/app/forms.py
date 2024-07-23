from django import forms


class ImageLink(forms.Form):
    url = forms.CharField(max_length=256)