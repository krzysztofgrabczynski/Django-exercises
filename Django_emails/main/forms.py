from django import forms

class SendEmailForm(forms.Form):
    subject = forms.CharField(max_length=254)
    message = forms.CharField(widget=forms.Textarea())
    recipients = forms.CharField(max_length=254)
    
class SendEmailWithAttachmentsForm(forms.Form):
    subject = forms.CharField(max_length=254)
    body = forms.CharField(widget=forms.Textarea())
    recipients = forms.CharField(max_length=254)
    attatchment = forms.FileField()