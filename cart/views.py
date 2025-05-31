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
    print(bag)
    print(bag.keys())

    """
    if item_type == 'pizza':
        pizza_bag = request.session.get('pizza_bag', {})
        if item_id in pizza_bag:
            pizza_bag[item_id] += quantity            
        
        else:          
            pizza_bag[item_id] = quantity
        request.session['pizza_bag'] = pizza_bag

    elif item_type == 'deal':
        deal_bag = request.session.get('deal_bag', {})
        if item_id in deal_bag:
            deal_bag[item_id] += quantity 

        else:           
            deal_bag[item_id] = quantity
            
        request.session['deal_bag'] = deal_bag

    elif item_type == 'side':
        side_bag = request.session.get('side_bag', {})
        if item_id in side_bag:
            side_bag[item_id] += quantity

        else:            
            side_bag[item_id] = quantity
        request.session['side_bag'] = side_bag

    elif item_type == 'drink':
        drink_bag = request.session.get('drink_bag', {})
        if item_id in drink_bag:
            drink_bag[item_id] += quantity

        else:            
            drink_bag[item_id] = quantity
        request.session['drink_bag'] = drink_bag

    elif item_type == 'dessert':
        dessert_bag = request.session.get('dessert_bag', {})
        if item_id in dessert_bag:
            dessert_bag[item_id] += quantity

        else:            
            dessert_bag[item_id] = quantity
        request.session['dessert_bag'] = dessert_bag
    """
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
            messages.add_message(request, messages.INFO,f"Empty cart.")   

    request.session['bag'] = bag

    return redirect(cart_view)
