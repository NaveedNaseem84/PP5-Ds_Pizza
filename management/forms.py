from django import forms
from menu.models import Pizza, Deal

class NewPizzaForm(forms.ModelForm):
    """
    An instance to create a new pizza
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
         
            "description": forms.Textarea(attrs={'style': 'width:100%', "rows":3}),
            "price": forms.NumberInput(attrs={'style': 'width:100%'}),
            
        }

class NewDealForm(forms.ModelForm):
    """
    An instance of a new deal
    """
    class Meta:

        model = Deal
        fields =(
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
          
            "description": forms.Textarea(attrs={'style': 'width:100%', "rows":3}),            
            "price": forms.NumberInput(attrs={'style': 'width:100%'}),        
            
        }


