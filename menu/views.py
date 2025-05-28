from django.shortcuts import render, get_object_or_404
from .models import Deal, Pizza, Extras

# Create your views here.


def menu_view(request):

    deal = Deal.objects.filter(active='Yes')
    pizza = Pizza.objects.filter(active="Yes")
    extra = Extras.objects.filter(active='Yes')

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

    print(selected_product.name)
    print(selected_product.description)
    print(selected_product.price)
    context = {
        "selected_product": selected_product,
        "item": item
    }

    return render(request, 'menu/menu_detail.html', context)

