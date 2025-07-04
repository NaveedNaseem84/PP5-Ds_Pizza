from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from cart.contexts import cart_contents
from cart.utils import determine_product_type
from .models import PizzaOrder, OrderLineItem
from .forms import orderForm


import stripe
import uuid


def checkout_view(request):
    """
    Renders the checkout view.

    Recieves the bag in session.

    determines if the user is logged in.

    if so, booking attached
    if not, as none.

    Validates the form using and payment details

    if valid creates the order recieving the items from
    the context processor bag

    Order number is generated automatically using UUID

    Stripe intent is created and sent via API to process.
    if the form/payment is valid.

    **Template:**
        :template:`checkout/checkout.html`
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    order_total = 0

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        order_no_length = 10
        order_num = str(uuid.uuid4()).replace('-', '')[:order_no_length]
        order_form = orderForm(data=request.POST)

        if request.user.is_authenticated:
            user = request.user
        else:
            user = None

        if order_form.is_valid():

            order = PizzaOrder.objects.create(
                order_ref=f"DS-{order_num}",
                name=request.POST.get('name'),
                user=user,
                phone=request.POST.get('phone'),
                email=request.POST.get('email'),
                billing_name=request.POST.get('billing_name'),
                address_line_1=request.POST.get('address_line_1'),
                address_line_2=request.POST.get('address_line_2'),
                town=request.POST.get('town'),
                postcode=request.POST.get('postcode'),
                )

            for item_type, items in bag.items():
                for item_id, item_quantity in items.items():
                    quantity = item_quantity['quantity']
                    product = determine_product_type(item_type, item_id)
                    line_total = product.price * quantity
                    OrderLineItem.objects.create(
                            order=order,
                            product=product.name,
                            price=product.price,
                            quantity=quantity,
                            line_total=line_total
                    )
                    order_total += line_total
            order.order_total = order_total
            order.save()
            request.session['success_page'] = order.order_ref

            print("from Checkout")
            print(request.session['success_page'])

            messages.add_message(request,
                                 messages.SUCCESS, 'Order Created')
            return redirect(reverse('success_page', args=[order.order_ref]))
        else:
            messages.add_message(request,
                                 messages.ERROR,
                                 'There seems to be an issue on the form.')
    else:

        bag = request.session.get('bag', {})

        current_bag = cart_contents(request)
        total = current_bag['grand_total']

        if total == 0:
            messages.info(request, "Nothing to checkout at the moment")
            return redirect(reverse('menu'))

        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )

        order_form = orderForm()
    template = 'checkout/checkout.html'
    context = {
                'order_form': order_form,
                'stripe_public_key': stripe_public_key,
                'client_secret': intent.client_secret,

            }

    return render(request, template, context)


def success_page(request, order_ref):
    """
    rendered once the order has been completed succesfully.

    Confirmation shown to the user with order ref recieved

    Email sent out using Gmail API to order email

    Session success deleted so it can't be accessed via URL

    **Template:**
        :template:`checkout/success.html`

    """
    session_ref = request.session.get('success_page')

    if session_ref != order_ref:
        raise Http404

    del request.session['success_page']

    order = get_object_or_404(PizzaOrder, order_ref=order_ref)
    item_count = 0
    for item in order.pizzaorderlineitems.all():
        item_count += item.quantity

    if 'bag' in request.session:
        del request.session['bag']

    subject = f"Your order at D's: {order_ref}"

    address = order.email
    items_on_order = ""
    for item in order.pizzaorderlineitems.all():
        items_on_order += f"\n{item.quantity} x {item.product}"

    message = f"""Many thanks for your order.\n\nYour order is as follows:\n
    {items_on_order}\n\nItems: {item_count}\nTotal: £{order.order_total}\n
    \n\nEnjoy!\nD's """

    try:
        send_mail(subject, message, settings.EMAIL_HOST_USER, [address])

    except Exception as e:
        messages.ERROR(request, f"{e} occured when trying to send an email")

    template = 'checkout/success.html'
    context = {
                'order_ref': order_ref,
                'order_name': order.name,
                'order': order,
                'item_count': item_count
            }
    return render(request, template, context)


@login_required
def my_orders(request):
    """
    User is able to login and see the orders created
    whilst logged in. Only results attached to user
    shown.

    Requires login

    **Template:**
        :template:`checkout/myorders.html`
    """

    user_orders = PizzaOrder.objects.filter(
        user=request.user
        ).order_by('-date')

    order_count = user_orders.count()

    template = 'checkout/myorders.html'
    context = {

        'orders': user_orders,
        'order_count': order_count
            }
    return render(request, template, context)
