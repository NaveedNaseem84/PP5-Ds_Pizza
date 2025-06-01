from django.shortcuts import render, redirect
from django.contrib import messages
from.forms import NewPizzaForm
from menu.views import menu_view


def management_view(request):

    return render(request, 'management/management.html')

def add_pizza(request):
    
    ## added to show proof of concept only, expand on in readme
    if not request.user.is_staff:
        messages.add_message(request, messages.ERROR,'Please login') 
        return redirect(menu_view)

    if request.method =="POST":
        form = NewPizzaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(menu_view)       
    else:
        form = NewPizzaForm()

    context = {
        "form": form,
        "product":"Pizza"
    }

    template = "management/product_admin.html"

    return render(request, template, context)
    