from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from.forms import NewPizzaForm, NewDealForm, NewExtraForm
from menu.models import Deal, Pizza, Extras
from menu.views import menu_view


def management_view(request):

    return render(request, 'management/management.html')

def add_pizza(request):
    """
    Creates a new instance of a pizza once
    """

    ## added to show proof of concept only, expand on in readme
    if not request.user.is_staff:
        messages.add_message(request, messages.ERROR,'Please login') 
        return redirect(menu_view)

    if request.method =="POST":
        form = NewPizzaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Pizza added') 
        
            return redirect(menu_view)       
    else:
        form = NewPizzaForm()

    context = {
        "form": form,
        "product":"Pizza"
    }

    template = "management/product_admin.html"

    return render(request, template, context)

def add_deal(request):
   """
   Creates a new instance of a deal once valid
   """ 
   ## added to show proof of concept only, expand on in readme
   if not request.user.is_staff:
        messages.add_message(request, messages.ERROR,'Please login') 
        return redirect(menu_view)
   
   if request.method =="POST":
        form = NewDealForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Deal added') 
        
            return redirect(menu_view)
   else:
        form = NewDealForm()

   context = {
        "form": form,
        "product":"Deal"
    }

   template = "management/product_admin.html"

   return render(request, template, context)

def add_extra(request):
   """
   Creates a new instance of a side, drink or dessert once valid
   """ 
   ## added to show proof of concept only, expand on in readme
   if not request.user.is_staff:
        messages.add_message(request, messages.ERROR,'Please login') 
        return redirect(menu_view)
   
   if request.method =="POST":
        form = NewExtraForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Side, Drink or Dessert added') 
        
            return redirect(menu_view)
   else:
        form = NewExtraForm()

   context = {
        "form": form,
        "product":"Side, Drink or Dessert"
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

