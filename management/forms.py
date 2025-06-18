from django import forms
from menu.models import Pizza, Deal, Extras
from checkout.models import PizzaOrder


class NewPizzaForm(forms.ModelForm):
    """
    An form instance to create a new pizza
    """
    class Meta:

        model = Pizza
        fields = (
            "name",
            "description",
            "active",
            "is_gf",
            "is_veg",
            "price",
        )

        widgets = {
            "description": forms.Textarea(attrs={'style': 'width:100%',
                                                 "rows": 3}),
            "price": forms.NumberInput(attrs={'style': 'width:100%'}),
        }


class NewDealForm(forms.ModelForm):
    """
    An form instance of a new deal
    """
    class Meta:

        model = Deal
        fields = (
            "name",
            "description",
            "pizza",
            "side",
            "drink",
            "dessert",
            "price",
            "active",
        )
        widgets = {
            "description": forms.Textarea(attrs={'style': 'width:100%',
                                                 "rows": 3}),
            "price": forms.NumberInput(attrs={'style': 'width:100%'}),
        }


class NewExtraForm(forms.ModelForm):
    """
    An form instance of a side, drink or dessert
    """
    class Meta:

        model = Extras
        fields = (
            "name",
            "description",
            "category",
            "price",
            "active",
        )
        widgets = {
            "description": forms.Textarea(attrs={'style': 'width:100%',
                                                 "rows": 3}),
            "price": forms.NumberInput(attrs={'style': 'width:100%'}),
        }


class StatusForm(forms.ModelForm):
    """
    An form instance of the Pizza Order
    """

    class Meta:

        model = PizzaOrder

        fields = (
            "status",
        )
