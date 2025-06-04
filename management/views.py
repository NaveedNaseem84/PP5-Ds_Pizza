from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from.forms import NewPizzaForm, NewDealForm, NewExtraForm
from menu.models import Deal, Pizza, Extras
from checkout.models import PizzaOrder
from menu.views import menu_view


def management_view(request):
    """
    dashboard to show the all current orders with status
    """


    if not request.user.is_staff:
        messages.add_message(request, messages.ERROR,'Please login') 
        return redirect(reverse('menu'))

    orders = PizzaOrder.objects.prefetch_related("pizzaorderlineitems").filter(status__in=["Ordered", "Preparing","Ready",])
    ordered_count = orders.filter(status="Ordered").count()
    preparing_count = orders.filter(status="Preparing").count()
    ready_count = orders.filter(status="Ready").count()
 
    template = "management/management.html"
    context = {
        "orders": orders,
        "order_count": ordered_count,
        "preparing_count": preparing_count,
        "ready_count": ready_count,
 
    }

    return render(request, template, context)

def add_product(request):
    """
    Creates a new instance of a product.
    Deal, side or Dessert passed in as an item type on URL retrieval
    """

    ## added to show proof of concept only, expand on in readme
    if not request.user.is_staff:
        messages.add_message(request, messages.ERROR,'Please login') 
        return redirect(menu_view)
    
   
    product_form = None  
    product = None      
    item= request.GET.get('item_type')
    print(item)
    
    if item =="deal":        
        product_form = NewDealForm
        product = "New Deal"
    
    elif item =="pizza":       
        product_form = NewPizzaForm
        product = "New Pizza"
    
    elif item =="extra":       
        product_form = NewExtraForm   
        product = "New Side, Drink or Dessert"

    if request.method =="POST":
        form = product_form(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Pizza added') 
        
            return redirect(menu_view)       
    else:
        form = product_form()

    context = {
        "form": form,
        "product":product
    }

    template = "management/product_admin.html"

    return render(request, template, context)


def update_product(request, product_id):

    if not request.user.is_staff:
        messages.add_message(request, messages.ERROR, 'Please login as an admin')
        return redirect(menu_view)
    
    product = None
    product_form = None
        
    item= request.GET.get('item_type')
    print(item)

    if item =="deal":
        product = get_object_or_404(Deal, id=product_id)
        product_form = NewDealForm

    elif item =="pizza":
        product = get_object_or_404(Pizza, id=product_id)
        product_form = NewPizzaForm
    
    elif item =="side" or item=="drink" or item=="dessert":
        product = get_object_or_404(Extras, id=product_id)
        product_form = NewExtraForm        
    
    if request.method =="POST":
        form = product_form(request.POST, instance=product)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Sucessfully updated') 
        
            return HttpResponseRedirect(reverse(menu_view))
    else:
        form = product_form( instance=product)

    context = {
        "form": form,
        "product": "Update",
        "item": item
    }

    template = "management/product_admin.html"
    return render(request, template, context)

