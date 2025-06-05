from django.shortcuts import get_object_or_404
from django.contrib import messages
from menu.models import Pizza, Deal, Extras



def determine_product_type(item_type, item_id):

    if item_type =="pizza":
            return get_object_or_404(Pizza, id=item_id)
    elif item_type =="deal":
            return get_object_or_404(Deal, id=item_id) 
    elif item_type =="side" or item_type =="drink" or item_type =="dessert":
            return get_object_or_404(Extras, id=item_id)
    return None 


def increase_qty(request, item_id, item_type):
    """
    Increase quantity of selected item in bag
    Display message to show which item has been updated.    """

    product = None

    bag = request.session.get('bag', {})
   
    if item_id in bag[item_type]:
        bag[item_type][item_id]['quantity'] += 1
        product = determine_product_type(item_type, item_id)
        messages.add_message(request, messages.SUCCESS,f"'{product}'+ 1") 

    request.session['bag'] = bag  

def decrease_qty(request, item_id, item_type):
    """
    Increase quantity of selected item in bag
    Display message to show which item has been updated.    """

    product = None 

    bag = request.session.get('bag', {})
    if item_id in bag[item_type]:
        bag[item_type][item_id]['quantity'] -= 1
        product = determine_product_type(item_type, item_id)      
        messages.add_message(request, messages.SUCCESS,f"'{product}'- 1") 

        if bag[item_type][item_id]['quantity'] < 1:
            del bag[item_type][item_id]

    request.session['bag'] = bag