from django.shortcuts import render
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
    