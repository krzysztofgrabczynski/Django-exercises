from django import forms


class AddPost(forms.Form):
    title = forms.CharField(max_length=128)
    visible = forms.BooleanField()
