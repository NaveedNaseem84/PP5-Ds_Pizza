from django import forms
from .models import PizzaOrder


class orderForm(forms.ModelForm):
    """
    An instance of the order form related to :model:`checkout.PizzaOrder`

    **context**
        ``fields``
            name, email, phone, billing_name, address_line_1,
            address_line_2, town, postcode
    """

    class Meta:

        model = PizzaOrder
        fields = (
            'name',
            'phone',
            'email',
            'billing_name',
            'address_line_1',
            'address_line_2',
            'town',
            'postcode',
            )
