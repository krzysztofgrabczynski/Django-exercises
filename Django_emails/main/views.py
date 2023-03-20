from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from .forms import send_email_v2_form


def index(request):
    return HttpResponse('index')


def send_email(request):
    subject = 'Test subject'
    message = 'Test message'
    from_email = 'django.emails.project@gmail.com'
    recipient_list = ['django.emails.project@gmail.com']
    send_mail(subject, message, from_email, recipient_list)

    return redirect(index)


def send_email_v2(request):
    email_form = send_email_v2_form(request.POST or None)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST.get('message')
        recipients = request.POST['recipients'].replace(' ', '').split(',')
        from_email = 'django.emails.project@gmail.com'

        if subject and message and recipients:
            try: 
                send_mail(subject, message, from_email, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect(index)
        else:    
            return HttpResponse('Error while sending email') 

    context = {
        'form': email_form,
    }
    return render(request, 'index.html', context)