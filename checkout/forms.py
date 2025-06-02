from django import forms
from.models import PizzaOrder

class orderForm(forms.ModelForm):

    class Meta:

        model = PizzaOrder
        fields = ('name', 'phone', 'email',)