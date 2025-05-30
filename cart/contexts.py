

def cart_contents(request):


    total = 123
    grand_total = 10

    context = {        
         "total": total,
         "grand_total": grand_total,
    }

    return context