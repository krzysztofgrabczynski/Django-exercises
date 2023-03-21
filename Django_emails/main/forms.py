from django import forms

class send_email_v2_form(forms.Form):
    subject = forms.CharField(max_length=254)
    message = forms.CharField(widget=forms.Textarea())
    recipients = forms.CharField(max_length=254)
    
class send_email_with_attachments_form(forms.Form):
    subject = forms.CharField(max_length=254)
    body = forms.CharField(widget=forms.Textarea())
    recipients = forms.CharField(max_length=254)
    attatchment = forms.FileField()