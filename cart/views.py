from django.shortcuts import render, redirect
from django.contrib import messages
from menu.views import menu_view
from .utils import increase_qty, decrease_qty, max_qty_in_cart
from .utils import max_new_product_qty, max_allowed_in_cart


def cart_view(request):

    return render(request, 'cart/cart.html')


def add_to_bag(request):
    """Add a quantity of a specified product type to the shopping bag."""

    quantity = int(request.POST.get('quantity'))
    item_id = request.POST.get('item_id')
    item_type = request.POST.get('item_type')

    bag = request.session.get('bag', {})

    if item_type not in bag:
        bag[item_type] = {}

    if item_id in bag[item_type]:
        if max_qty_in_cart(request, item_id, item_type):
            return redirect(menu_view)
        bag[item_type][item_id]['quantity'] += quantity

        messages.add_message(request, messages.SUCCESS,
                             'Item quantity updated')
    else:

        if max_new_product_qty(request):
            return redirect(menu_view)

        bag[item_type][item_id] = {
            'quantity': quantity,
        }
        messages.add_message(request,
                             messages.SUCCESS, 'Item added')
    request.session['bag'] = bag

    return redirect(menu_view)


def increase_from_bag(request, item_id, item_type):
    """
    Increase quantity of selected item in bag
    Display message to show which item has been updated.    """

    if max_allowed_in_cart(request, item_id, item_type):
        return redirect(cart_view)

    increase_qty(request, item_id, item_type)

    return redirect(cart_view)


def decrease_from_bag(request, item_id, item_type):
    """
    Decrease quantity of selected item in bag by 1
    Display message to show which item has been decreased.
    Display message when the cart is empty"
    """
    decrease_qty(request, item_id, item_type)

    return redirect(cart_view)
