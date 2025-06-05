from django.shortcuts import get_object_or_404
from menu.models import Pizza, Deal, Extras

def cart_contents(request):

    # core logic to add to context processor adapter from ADO Ci project. 
    # credit in readme.md

     bag_items = []
     total = 0
     bag_quantity = 0
     grand_total = 0

     bag = request.session.get('bag', {})
     
     for item_type, items in bag.items():
          for item_id, item_quantity in items.items():
                quantity = item_quantity['quantity']
                
                if item_type == "pizza":
                    product = get_object_or_404(Pizza, pk = item_id)
                elif item_type == "deal":
                    product = get_object_or_404(Deal, pk=item_id)
                elif item_type =="side" or item_type =="drink" or item_type=="dessert":
                    product = get_object_or_404(Extras, pk=item_id)
                
                total = quantity * product.price
                bag_quantity += quantity
                grand_total +=total
                bag_items.append(
                    {
                        "item_id": item_id, 
                        "item_type":item_type,
                        'quantity': quantity,
                        'product_name': product.name,
                        'price': product.price,
                        'total':total,
                    }
                )             

     context = {        
         "bag_quantity": bag_quantity,
         "bag_items": bag_items,      
         "grand_total": grand_total,
    }

     return context