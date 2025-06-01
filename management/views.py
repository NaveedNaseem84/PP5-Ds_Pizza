from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from.forms import NewPizzaForm, NewDealForm, NewExtraForm
from menu.views import menu_view
from menu.models import Deal

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

    item= request.GET.get('item_type')
    print(item)

    if not request.user.is_staff:
        messages.add_message(request, messages.ERROR, 'Please login as an admin')
        return redirect(menu_view)

    pizza = get_object_or_404(Deal, id=product_id)
    
    if request.method =="POST":
        form = NewDealForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Sucessfully updated') 
        
            return redirect(menu_view)
    else:
        form = NewDealForm( instance=pizza)

    context = {
        "form": form,
        "product": "Update",
        "pizza": pizza
    }

    template = "management/product_admin.html"
    return render(request, template, context)


    