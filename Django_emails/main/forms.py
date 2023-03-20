from django import forms

class send_email_v2_form(forms.Form):
    subject = forms.CharField(max_length=254)
    message = forms.CharField(widget=forms.Textarea())
    recipients = forms.CharField(max_length=254)