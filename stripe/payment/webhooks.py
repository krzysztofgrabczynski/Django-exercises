import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from shop.models import TestOrder


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
    
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    
    session = event.data.object
    if event.type == "checkout.session.completed":
        handle_checkout_session_completed(session)

    return HttpResponse(status=200)

def handle_checkout_session_completed(session):
    if session.mode == 'payment' and session.payment_status == 'paid':
        print("set user as subscriber and send email notification")
    