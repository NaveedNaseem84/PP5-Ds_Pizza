from django import forms
from .models import PizzaOrder


class orderForm(forms.ModelForm):

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
