from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NewPizzaForm, NewDealForm, NewExtraForm, StatusForm
from menu.models import Deal, Pizza, Extras
from checkout.models import PizzaOrder
from menu.views import menu_view


@login_required
def management_view(request):
    """
    dashboard to show the all current orders with status
    """

    if not request.user.is_staff:
        messages.add_message(request, messages.ERROR, 'Please login')
        return redirect(reverse('menu'))

    orders = PizzaOrder.objects.prefetch_related(
        "pizzaorderlineitems"
        ).filter(status__in=[
            "Ordered", "Preparing", "Ready", ])

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


def determine_product(item):
    """
    Used to determine the product time. Data passed into
    add update product below
    """
    if item == "deal":
        return Deal, NewDealForm, "New Deal"
    elif item == "pizza":
        return Pizza, NewPizzaForm, "New Pizza"
    elif item == "extra":
        return Extras, NewExtraForm, "New Side, Drink or Dessert"

    elif item in ['side', 'dessert', 'drink']:
        return Extras, NewExtraForm, "New Side, Drink or Dessert"
    else:
        return None, None, None


@login_required
def add_product(request):
    """
    Creates a new instance of a product.
    Deal, side or Dessert passed in as an item type on URL retrieval
    """

    # added to show proof of concept only, expand on in readme
    if not request.user.is_staff:
        messages.add_message(request, messages.ERROR, 'Please login')
        return redirect(menu_view)

    item = request.GET.get('item_type')

    if item not in ['pizza', 'deal', 'extra']:
        messages.add_message(request, messages.ERROR, 'Item type not found')
        return redirect(menu_view)

    model, product_form, product = determine_product(item)

    if request.method == "POST":
        form = product_form(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Pizza added')

            return redirect(menu_view)
    else:
        form = product_form()

    context = {
        "form": form,
        "product": product
    }

    template = "management/product_admin.html"

    return render(request, template, context)


@login_required
def update_product(request, product_id):

    if not request.user.is_staff:
        messages.add_message(request,
                             messages.ERROR,
                             'Please login as an admin')
        return redirect(menu_view)

    item = request.GET.get('item_type')

    model, product_form, product = determine_product(item)

    product = get_object_or_404(model, id=product_id)

    if request.method == "POST":
        form = product_form(request.POST, instance=product)

        if form.is_valid():
            form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Sucessfully updated')

            return HttpResponseRedirect(reverse(menu_view))
    else:
        form = product_form(instance=product)

    template = "management/product_admin.html"
    context = {
        "form": form,
        "product": "Update",
        "item": item
    }

    return render(request, template, context)


@login_required
def update_order_status(request, order_id):

    if not request.user.is_staff:
        messages.add_message(request,
                             messages.ERROR,
                             'Please login as an admin')
        return redirect(menu_view)

    product = get_object_or_404(PizzaOrder, id=order_id)

    form = StatusForm(request.POST, instance=product)

    if form.is_valid():
        form.save()
        messages.add_message(request,
                             messages.SUCCESS, 'Status updated')

        return redirect(management_view)
    else:
        form = StatusForm(instance=product)

    template = "management/update_status.html"
    context = {

        "form": form,
        "product": product,
    }

    return render(request, template, context)
