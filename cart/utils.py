from django.shortcuts import get_object_or_404
from django.contrib import messages
from menu.models import Pizza, Deal, Extras


def determine_product_type(item_type, item_id):
    """
    helper function used to determine the item type
    **Context**
        ``item_type``
            recieved from the function calling this one`

        ``item_id``
            `int` recieved from the function calling

        ``pizza``
            Instance ID of :model:`Pizza` model

        ``deal``
            Instance ID of :model:`Deal` model

        ``side, drink, dessert``
            Instance ID of :model:`Extra` model

    """

    if item_type == "pizza":
        return get_object_or_404(Pizza, id=item_id)
    elif item_type == "deal":
        return get_object_or_404(Deal, id=item_id)
    elif item_type == "side" or item_type == "drink" or item_type == "dessert":
        return get_object_or_404(Extras, id=item_id)
    return None


def increase_qty(request, item_id, item_type):
    """
    Increase quantity of selected item in bag

    Display message to show which item has been updated.

    **Context**
        ``product``
            result of product definition`

        ``bag``
            latest version of the bag in session

    """

    product = None

    bag = request.session.get('bag', {})

    if item_id in bag[item_type]:
        bag[item_type][item_id]['quantity'] += 1
        product = determine_product_type(item_type, item_id)
        messages.add_message(request, messages.SUCCESS, f"'{product}'+ 1")

    request.session['bag'] = bag


def decrease_qty(request, item_id, item_type):
    """
    Increase quantity of selected item in bag

    Display message to show which item has been updated.

    If the quantity reaches 0, remove it.

    **Context**
         ``product``
            result of product definition`

        ``bag``
            latest version of the bag in session
    """

    product = None

    bag = request.session.get('bag', {})
    if item_id in bag[item_type]:
        bag[item_type][item_id]['quantity'] -= 1
        product = determine_product_type(item_type, item_id)
        messages.add_message(request, messages.SUCCESS, f"'{product}'- 1")

        if bag[item_type][item_id]['quantity'] < 1:
            del bag[item_type][item_id]

    request.session['bag'] = bag


def max_qty_in_cart(request, item_id, item_type):
    """
    Allow a maximum of 10 of any item in the bag.

    **Context**
         ``quantity``
            The posted value recieved from quantity`

        ``bag``
            latest version of the bag in session

    """

    bag = request.session.get('bag', {})
    quantity = int(request.POST.get('quantity'))

    if bag[item_type][item_id]['quantity'] + quantity > 10:
        messages.add_message(request, messages.INFO,
                             "Maxiumum quantity of 10 allowed")
        return True
    return False


def max_new_product_qty(request):
    """
    Allow a maximum of 10 to be added into bag.

     **Context**
         ``quantity``
            The posted value recieved from quantity`

        ``bag``
            latest version of the bag in session
    """

    quantity = int(request.POST.get('quantity'))
    if quantity > 10:
        messages.add_message(request, messages.INFO,
                             "Maxiumum quantity of 10 allowed")
        return True
    return False


def max_allowed_in_cart(request, item_id, item_type):
    """
    Allow an increase  maximum of 10 in bag.

     **Context**

        ``bag``
            latest version of the bag in session
    """

    bag = request.session.get('bag', {})
    if bag[item_type][item_id]['quantity'] > 9:
        messages.add_message(request, messages.INFO,
                             "Maxiumum quantity of 10 allowed")
        return True
    return False
