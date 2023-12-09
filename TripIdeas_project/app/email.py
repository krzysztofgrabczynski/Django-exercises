from django.core.mail import send_mail
from django.utils.safestring import SafeString


def send_reset_password_email(message: SafeString, from_email: str, to_email: str):
    subject = "Reset password email"
    to_email = [to_email]

    send_mail(subject, message, from_email, to_email)
