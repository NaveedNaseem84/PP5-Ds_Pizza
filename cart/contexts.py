from .utils import determine_product_type


def cart_contents(request):

    # core logic to add to context processor adapter from ADO Ci project.
    # credit in readme.md

    """
    Recieves the bag in the current request session.
    Iterated to get the item type, id and quantity for each.

    Product type determined using the helper `determine_product_type`

    items added into bag items with the item, qty and name.

    **Context**
        `bag_items`
            holds the item and info
        `total`
            sum of quantity * item price
        `bag_quantity`
            sum of total quantity of items
        `grand_total`
            running total for bag collated
    """

    bag_items = []
    total = 0
    bag_quantity = 0
    grand_total = 0

    bag = request.session.get('bag', {})

    for item_type, items in bag.items():
        for item_id, item_quantity in items.items():
            quantity = item_quantity['quantity']

            product = determine_product_type(item_type, item_id)
            total = quantity * product.price
            bag_quantity += quantity
            grand_total += total
            bag_items.append(
                {
                    "item_id": item_id,
                    "item_type": item_type,
                    'quantity': quantity,
                    'product_name': product.name,
                    'price': product.price,
                    'total': total,
                }
                )

    context = {
         "bag_quantity": bag_quantity,
         "bag_items": bag_items,
         "grand_total": grand_total,
    }

    return context
