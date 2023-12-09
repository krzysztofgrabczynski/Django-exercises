from celery import shared_task
from celery.utils.log import get_task_logger
from django.utils.safestring import SafeString

from app.email import send_reset_password_email

logger = get_task_logger(__name__)


@shared_task
def send_reset_password_email_task(message: SafeString, from_email: str, to_email: str):
    print("dasdasdasd")
    logger.info("Sending reset password email")
    return send_reset_password_email(message, from_email, to_email)
