from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


from checkout.webhook_handler import stripeWH_Handler
import stripe


# This file has been configured using CI Project Ado Webhooks. Credit in readme.md
#Project - Boutique Ado  Introducing and Configuring Webhooks  Setting Up Stripe Webhooks for Event Handling

@require_POST
@csrf_exempt

def webhook(request):
    """
    Stripe webhooks
    """
    #setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    #retrieve webhoook data

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    
    except Exception as e:
        return HttpResponse(content=e, status=400)