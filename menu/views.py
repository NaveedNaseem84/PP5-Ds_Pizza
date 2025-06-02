from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Deal, Pizza, Extras

# Create your views here.


def menu_view(request):

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
        messages.add_message(
        request, messages.SUCCESS,
        'Veg options shown')        

    elif filter == "gf":        
        pizza =pizza.filter(is_veg="No", is_gf="Yes")
        messages.add_message(
        request, messages.SUCCESS,
        'Gluten Free options shown') 
    
    elif filter == "vg_gf":        
        pizza =pizza.filter(is_veg="Yes", is_gf="Yes")
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

    if item =="pizza":
        selected_product = get_object_or_404(Pizza, pk=product_id)
    elif item=="deal":
        selected_product = get_object_or_404(Deal, pk=product_id)
    elif item in ("side","drink","dessert"):
         selected_product = get_object_or_404(Extras, pk=product_id)

    context = {
        "selected_product": selected_product,
        "item": item
    }

    return render(request, 'menu/menu_detail.html', context)


def delete_product(request, product_id):

    if not request.user.is_staff:
        messages.add_message(request, messages.ERROR, 'Please login as an admin')
        return HttpResponseRedirect(reverse(menu_view))    
    
    product = None    
        
    item= request.GET.get('item_type')
    print(item)
    print(request.get_full_path()) 

    if item =="deal":
        product = get_object_or_404(Deal, id=product_id)       

    elif item =="pizza":
        product = get_object_or_404(Pizza, id=product_id)
       
    
    elif item =="side" or item=="drink" or item=="dessert":
        product = get_object_or_404(Extras, id=product_id)       

    product.delete()
    messages.add_message(request, messages.INFO,'Product Deleted') 

    return HttpResponseRedirect(reverse(menu_view))