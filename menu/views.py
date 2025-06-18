from django.shortcuts import render, reverse, redirect
from django.db import DatabaseError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Deal, Pizza, Extras
from cart.utils import (
    increase_qty,
    decrease_qty,
    determine_product_type,
    max_allowed_in_cart
    )


def menu_view(request):
    """
    Renders the menu with the active items

    Allows the option to filter based on allergy.

    Admin is able to see ALL items regardless if active/not

    **Template:**
        :template:`menu/menu.html`
    """

    filter = request.GET.get('allergen-filter')

    try:

        if request.user.is_staff:
            deal = Deal.objects.all()
            pizza = Pizza.objects.all()
            extra = Extras.objects.all()

        else:
            deal = Deal.objects.filter(active='Yes')
            pizza = Pizza.objects.filter(active="Yes")
            extra = Extras.objects.filter(active='Yes')

    except DatabaseError as e:
        messages.add_message(
            request, messages.ERROR, f'{e} occurred. Please try again later.')

    if filter == "vg":
        pizza = pizza.filter(is_veg="Yes", is_gf="No")
        deal = deal.filter(pizza__is_veg="Yes", pizza__is_gf="No")
        messages.add_message(
            request, messages.SUCCESS,
            'Veg options shown')

    elif filter == "gf":
        pizza = pizza.filter(is_veg="No", is_gf="Yes")
        deal = deal.filter(pizza__is_veg="No", pizza__is_gf="Yes")
        messages.add_message(
            request, messages.SUCCESS,
            'Gluten Free options shown')

    elif filter == "vg_gf":
        pizza = pizza.filter(is_veg="Yes", is_gf="Yes")
        deal = deal.filter(pizza__is_veg="Yes", pizza__is_gf="Yes")
        messages.add_message(
            request, messages.SUCCESS,
            'Veg and Gluten Free shown')

    elif filter == "all":
        messages.add_message(
            request, messages.SUCCESS,
            'All options shown')

    elif filter == "default":
        messages.add_message(
            request, messages.INFO,
            'Please select an option first')

    template = "menu/menu.html"
    context = {
        "deals": deal,
        "pizza": pizza,
        "extras": extra
    }

    return render(request, template, context)


def product_detail(request, product_id):
    """
    Retrieves the full details of the selected product which
    are passed to the product detail modal

    The product type is determined using the helper function
    `determine_product_type`
    """
    selected_product = None
    item = request.GET.get('item_type')

    if item not in ['pizza', 'deal', 'side', 'drink', 'dessert']:
        messages.add_message(request, messages.ERROR, 'Item type not found')
        return redirect(menu_view)

    deal = Deal.objects.filter(active='Yes')
    pizza = Pizza.objects.filter(active="Yes")
    extra = Extras.objects.filter(active='Yes')

    selected_product = determine_product_type(item, product_id)

    context = {
        "selected_product": selected_product,
        "item": item,
        "deals": deal,
        "pizza": pizza,
        "extras": extra
    }

    return render(request, 'menu/menu.html', context)


def menu_increase_from_bag(request, item_id, item_type):
    """
    Increase quantity of selected item in bag
    Display message to show which item has been updated.

    Same concept as in `cart` increase
    """
    if max_allowed_in_cart(request, item_id, item_type):
        return redirect(menu_view)

    increase_qty(request, item_id, item_type)

    return redirect(reverse(menu_view))


def menu_decrease_from_bag(request, item_id, item_type):
    """
    Decrease quantity of selected item in bag by 1
    Display message to show which item has been decreased.
    Display message when the cart is empty"

    Same concept as in `cart` decrease
    """
    decrease_qty(request, item_id, item_type)

    return redirect(reverse(menu_view))


@login_required
def delete_product(request, product_id):
    """
    Delete the selected product

    Product determined via the product type and Id recieved

    Login required - only admin is able to access!
    """

    if not request.user.is_staff:
        messages.add_message(request, messages.ERROR,
                             'Please login as an admin')
        return redirect(reverse(menu_view))

    product = None

    item_type = request.GET.get('item_type')
    product = determine_product_type(item_type, product_id)

    product.delete()
    messages.add_message(request, messages.INFO,
                         'Product Deleted')

    return redirect(reverse(menu_view))
