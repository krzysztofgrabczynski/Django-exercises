from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, send_mass_mail, BadHeaderError, EmailMessage
from .forms import send_email_v2_form, send_email_with_attachments_form
from django_emails.settings import EMAIL_HOST_USER


def index(request):
    return HttpResponse('index')


def send_email(request):
    subject = 'Test subject'
    message = 'Test message'
    from_email = 'django.emails.project@gmail.com'
    recipient_list = ['django.emails.project@gmail.com']
    send_mail(subject, message, from_email, recipient_list)

    return HttpResponse('Sent')


def send_email_v2(request):
    email_form = send_email_v2_form(request.POST or None)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST.get('message', '')
        recipients = request.POST['recipients'].replace(' ', '').split(',')
        from_email = EMAIL_HOST_USER

        if subject and message and recipients:
            try: 
                send_mail(subject, message, from_email, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Sent')
        else:    
            return HttpResponse('Error while sending email') 

    context = {
        'form': email_form,
    }
    return render(request, 'send_email_v2.html', context)

def send_email_with_attachments(request):
    form = send_email_with_attachments_form(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        body = request.POST.get('body', '')
        from_email = EMAIL_HOST_USER
        recipients = request.POST.get('recipients', '').replace(' ', '').split(',')
        file = request.FILES['attatchment']

        email = EmailMessage(
            subject,
            body,
            from_email,
            recipients,
        )

        email.attach(file.name, file.read(), file.content_type)
        email.send()
        
        return HttpResponse('Sent')
        
    return render(request, 'send_email_with_attachments.html', {'form': form})