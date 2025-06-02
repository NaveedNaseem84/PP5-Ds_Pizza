from django.shortcuts import render
from.forms import orderForm

# Create your views here.


def checkout_view(request):

    order_form = orderForm(data=request.POST)
    template = 'checkout/checkout.html'
    context = {
            'order_form': order_form,
            'stripe_public_key': 'pk_test_51ROMmoRq53b8oxxiELQlxjLJj339AZZZM6nfxlfNtQcszTYsLYuqdgvicVNhBpgfEgnm7DoyZ72fE5ONEIzrvV4600L6rDAclB',
            'client_secret': 'test_client_key',
        }

    return render(request, template, context)