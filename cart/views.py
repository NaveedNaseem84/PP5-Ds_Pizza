from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from menu.models import Pizza, Deal, Extras
from menu.views import menu_view

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
        bag[item_type][item_id]['quantity'] += quantity
        messages.add_message(
        request, messages.SUCCESS,
        'Item quantity updated') 
    else:
        bag[item_type][item_id] = {
            'quantity': quantity,
        }
        messages.add_message(
        request, messages.SUCCESS,
        'Item added') 
    request.session['bag'] = bag

    return redirect(menu_view)

def increase_from_bag(request, item_id, item_type):
    """
    Increase quantity of selected item in bag
    Display message to show which item has been updated.    """

    product = None

    bag = request.session.get('bag', {})
   
    if item_id in bag[item_type]:
        bag[item_type][item_id]['quantity'] += 1

        if item_type =="pizza":
            product = get_object_or_404(Pizza, pk=item_id)
        elif item_type =="deal":
            product = get_object_or_404(Deal, pk=item_id) 
        elif item_type =="side" or item_type =="drink" or item_type =="dessert":
            product = get_object_or_404(Extras, pk=item_id) 
        
        messages.add_message(request, messages.SUCCESS,f"'{product}'+ 1") 

    request.session['bag'] = bag  
  
    return redirect(cart_view)


def decrease_from_bag(request, item_id, item_type):
    """
    Decrease qunattiy of selected item in bag by 1
    Display message to show which item has been decreased.
    Display message when the cart is empty"
    """    
    product = None 

    bag = request.session.get('bag', {})
    if item_id in bag[item_type]:
        bag[item_type][item_id]['quantity'] -= 1
        if item_type =="pizza":
            product = get_object_or_404(Pizza, pk=item_id)
        elif item_type =="deal":
            product = get_object_or_404(Deal, pk=item_id) 
        elif item_type =="side" or item_type =="drink" or item_type =="dessert":
            product = get_object_or_404(Extras, pk=item_id) 
        
        messages.add_message(request, messages.SUCCESS,f"'{product}'- 1") 

        if bag[item_type][item_id]['quantity'] < 1:
            del bag[item_type][item_id]

    request.session['bag'] = bag

    return redirect(cart_view)
