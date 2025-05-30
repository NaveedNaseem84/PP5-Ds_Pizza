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
                "item_type":item_type,
                'quantity': quantity,
                'product_name': product.name,
                'price': product.price,
                'total':total,
            }
        )             
    



     """
     pizza_bag = request.session.get('pizza_bag', {})
     deal_bag = request.session.get('deal_bag', {})
     side_bag = request.session.get('side_bag', {})
     drink_bag = request.session.get('drink_bag', {})
     dessert_bag = request.session.get('dessert_bag', {})

     for item_type, quantity in pizza_bag.items():
        pizza = get_object_or_404(Pizza, pk=item_type)
        total = quantity * pizza.price
        bag_quantity += quantity
        grand_total += total
        bag_items.append(
            {
                "item_type":item_type,
                'quantity': quantity,
                'product_name': pizza.name,
                'price': pizza.price,
                'total':total,
            }
        )     
     for item_type, quantity in deal_bag.items():
        deal = get_object_or_404(Deal, pk=item_type)
        total = quantity * deal.price
        bag_quantity += quantity
        grand_total += total
        bag_items.append(
            {
                "item_type":item_type,
                'quantity': quantity,
                'product_name': deal.name,
                'price': deal.price,
                'total':total,
            }
        )
     for item_type, quantity in side_bag.items():
        side = get_object_or_404(Extras, pk=item_type)
        total = quantity * side.price
        bag_quantity += quantity
        grand_total += total
        bag_items.append(
            {
                "item_type":item_type,
                'quantity': quantity,
                'product_name': side.name,
                'price': side.price,
                'total':total,
            }
        )

     for item_type, quantity in drink_bag.items():
        drink = get_object_or_404(Extras, pk=item_type)
        total = quantity * drink.price
        bag_quantity += quantity
        grand_total += total
        bag_items.append(
            {
                "item_type":item_type,
                'quantity': quantity,
                'product_name': drink.name,
                'price': drink.price,
                'total':total,
            }
        )

     for item_type, quantity in dessert_bag.items():
        dessert = get_object_or_404(Extras, pk=item_type)
        total = quantity * dessert.price
        bag_quantity += quantity
        grand_total += total
        bag_items.append(
            {
                "item_type":item_type,
                'quantity': quantity,
                'product_name': dessert.name,
                'price': dessert.price,
                'total':total,
            }
        )     
     """
     context = {        
         "bag_quantity": bag_quantity,
         "bag_items": bag_items,      
         "grand_total": grand_total,
    }

     return context