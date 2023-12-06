from django.core.mail import send_mail

from core.settings import EMAIL_HOST_USER


def send_reset_password_email(reset_password_link: str, recipient: str):
    subject = "Reset password email"
    message = f"Here is your reset password link {reset_password_link}"
    from_email = EMAIL_HOST_USER
    recipient = [recipient]

    send_mail(subject, message, from_email, recipient)
