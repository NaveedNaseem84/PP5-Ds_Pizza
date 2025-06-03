from django.http import HttpResponse

# This file has been configured using CI Project Ado Webhooks. Credit in readme.md
#Project - Boutique Ado  Introducing and Configuring Webhooks  Setting Up Stripe Webhooks for Event Handling

class stripeWH_Handler:
    """
    Handle webhook stripes
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle generic/unknown webhook event
        """

        return HttpResponse(
            content=f'Webhook unknown: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment intent succeeded from stripe
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_payment_failed(self, event):
        """
        Handle payment intent failed from stripe
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
    
 
