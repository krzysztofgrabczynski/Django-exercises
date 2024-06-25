from django.urls import path

from payment import views as payment_views
from payment.webhooks import stripe_webhook


urlpatterns = [
    path("process/<order_id>/", payment_views.order_payment, name="order_payment"),
    path("success/", payment_views.success_order_payment, name="success_order_payment"),
    path("cancel/", payment_views.cancel_order_payment, name="cancel_order_payment"),
    path("webhook/", stripe_webhook, name="stripe_webhook"),
]
