from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages
from .models import PizzaOrder, OrderLineItem
from.forms import orderForm
from menu.models import Pizza, Deal, Extras
from cart.contexts import cart_contents

import stripe

def checkout_view(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        order_form = orderForm(data=request.POST)
        if order_form.is_valid():            
            order = PizzaOrder.objects.create(
            name =  request.POST.get('name'),
            phone = request.POST.get('phone'),
            email = request.POST.get('email'),
            )
            order_total = 0
            for item_type, items in bag.items():
                for item_id, item_quantity in items.items():
                    quantity = item_quantity['quantity']
                    if item_type == "pizza":
                        product = get_object_or_404(Pizza, pk = item_id)
                    elif item_type == "deal":
                        product = get_object_or_404(Deal, pk=item_id)
                    elif item_type =="side" or item_type =="drink" or item_type=="dessert":
                        product = get_object_or_404(Extras, pk=item_id)
                    line_total = product.price * quantity
                    OrderLineItem.objects.create(
                            order=order,
                            product=product.name,
                            price = product.price,
                            quantity=quantity,
                            line_total=line_total
                    )
                    order_total += line_total 
            order.order_total = order_total
            order.save()
            messages.add_message( request, messages.SUCCESS,'Order Created')
            return redirect(checkout_view)
    else:
 
        bag = request.session.get('bag', {})

        current_bag = cart_contents(request)
        #total = current_bag['grand_total']

       # stripe_total = round(total * 100)
       # stripe.api_key = stripe_secret_key
       # intent = stripe.PaymentIntent.create(
              #  amount=stripe_total,
           # currency=settings.STRIPE_CURRENCY,
          #  )
 
        order_form = orderForm()
    template = 'checkout/checkout.html'
    context = {
                'order_form': order_form,
               # 'stripe_public_key': stripe_public_key,
                #'client_secret': intent.client_secret,
            }
        
    return render(request, template, context)