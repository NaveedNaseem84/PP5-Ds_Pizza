import uuid
from django.db import models
from django.core.validators import RegexValidator



class PizzaOrder(models.Model):

    STATUS = [
        ("Ordered", "Ordered"),
        ("Preparing", "Preparing"),
        ("Ready", "Ready",),
        ("Completed", "Completed",)
    ]

    order_ref = models.CharField(max_length=32, null=False, editable=False)
    name = models.CharField(max_length=40, null=False, blank=False)
    phone = models.CharField(
        max_length=11,
        validators=[RegexValidator(
            regex=r'^\d+$',
            message="Please enter a valid phone number.",
            code="invalid_number")]
    )
    email = models.EmailField(null=False, blank=False)
    date = models.DateTimeField(auto_now=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    status = models.CharField(choices=STATUS,
                              max_length=9,
                              blank=False,
                              default="Ordered")
    
    
    # generate order and save method: adapted from CI ado content
    # reference in readme.md

    def _generate_order_number(self):

        return uuid.uuid4()
    
    def save(self, *args, **kwargs):

        if not self.order_ref:
            self.order_ref = self._generate_order_number() 
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Order for {self.name}"


class OrderLineItem(models.Model):

    order = models.ForeignKey(PizzaOrder, null=False, blank=False, on_delete=models.CASCADE, related_name="pizzaorderlineitems")   
    product = models.CharField(max_length=96, null=False, editable=False, default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(null=False, blank=False)
    line_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, editable=False)
     

    def __str__(self):
        return ""




    


