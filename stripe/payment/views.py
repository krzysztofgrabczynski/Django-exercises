from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import stripe
from decimal import Decimal

from shop.models import TestOrder


def order_payment(request, order_id):
    stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

    order = TestOrder.objects.get(id=order_id)

    if request.method == "POST":
        success_url = request.build_absolute_uri(reverse("success_order_payment"))
        cancel_url = request.build_absolute_uri(reverse("cancel_order_payment"))
        line_items = []
        for item in order.products.all():
            data = {
                "price_data": {
                    "unit_amount": int(item.price * Decimal("100")),
                    "currency": "usd",
                    "product_data": {
                        "name": item.name,
                    },
                },
                "quantity": order.amount,
            }
            line_items.append(data)

        stripe_data = {
            "mode": "payment",
            "success_url": success_url,
            "cancel_url": cancel_url,
            "line_items": line_items,
        }

        session = stripe.checkout.Session.create(**stripe_data)
        return redirect(session.url, code=303)
    else:
        return render(request, "payment/order_payment.html")

def success_order_payment(request):
    return render(request, "payment/success_order_payment.html")


def cancel_order_payment(request):
    return render(request, "payment/cancel_order_payment.html")
