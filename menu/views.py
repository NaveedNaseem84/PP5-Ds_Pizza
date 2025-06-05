from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Deal, Pizza, Extras
from cart.utils import increase_qty, decrease_qty, determine_product_type



def menu_view(request):

    if request.user.is_staff:
        deal = Deal.objects.all()
        pizza = Pizza.objects.all()
        extra = Extras.objects.all()
        
    else:
        deal = Deal.objects.filter(active='Yes')
        pizza = Pizza.objects.filter(active="Yes")
        extra = Extras.objects.filter(active='Yes')

    filter = request.GET.get('allergen-filter')
    
    if filter =="all":
        deal = deal
        pizza = pizza
        messages.add_message(
        request, messages.SUCCESS,
        'All options shown')         
    
    elif filter == "vg":        
        pizza = pizza.filter(is_veg="Yes", is_gf="No")
        deal = deal.filter(pizza__is_veg="Yes", pizza__is_gf="No")
        messages.add_message(
        request, messages.SUCCESS,
        'Veg options shown')        

    elif filter == "gf":        
        pizza =pizza.filter(is_veg="No", is_gf="Yes")
        deal = deal.filter(pizza__is_veg="No", pizza__is_gf="Yes")
        messages.add_message(
        request, messages.SUCCESS,
        'Gluten Free options shown') 
    
    elif filter == "vg_gf":        
        pizza =pizza.filter(is_veg="Yes", is_gf="Yes")
        deal = deal.filter(pizza__is_veg="Yes", pizza__is_gf="Yes")
        messages.add_message(
        request, messages.SUCCESS,
        'Veg and Gluten Free shown')

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
    selected_product = None    
    item= request.GET.get('item_type')
    

    deal = Deal.objects.filter(active='Yes')
    pizza = Pizza.objects.filter(active="Yes")
    extra = Extras.objects.filter(active='Yes')    
    
    if item =="pizza":
        selected_product = get_object_or_404(Pizza, pk=product_id)
    elif item=="deal":
        selected_product = get_object_or_404(Deal, pk=product_id)
    elif item in ("side","drink","dessert"):
         selected_product = get_object_or_404(Extras, pk=product_id)

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
    Display message to show which item has been updated.    """

    increase_qty(request, item_id, item_type)
  
    return HttpResponseRedirect(reverse(menu_view))


def menu_decrease_from_bag(request, item_id, item_type):
    """
    Decrease qunattiy of selected item in bag by 1
    Display message to show which item has been decreased.
    Display message when the cart is empty"
    """    
    decrease_qty(request, item_id, item_type)

    return HttpResponseRedirect(reverse(menu_view))


def delete_product(request, product_id):

    if not request.user.is_staff:
        messages.add_message(request, messages.ERROR, 'Please login as an admin')
        return HttpResponseRedirect(reverse(menu_view))    
    
    product = None    
        
    item_type= request.GET.get('item_type')
    product = determine_product_type(item_type, product_id)      

    product.delete()
    messages.add_message(request, messages.INFO,'Product Deleted') 

    return HttpResponseRedirect(reverse(menu_view))