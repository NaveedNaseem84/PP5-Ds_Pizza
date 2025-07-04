from django.db import models
from django.contrib.auth.models import User


class PizzaOrder(models.Model):
    """
    Stores a single Pizza Order Entry.
    """

    STATUS = [
        ("Ordered", "Ordered"),
        ("Preparing", "Preparing"),
        ("Ready", "Ready",),
        ("Completed", "Completed",)
    ]

    order_ref = models.CharField(max_length=32, null=False, editable=False)
    name = models.CharField(max_length=40, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True, blank=True,
                             related_name="PizzaOrders")

    phone = models.CharField(max_length=11, null=False, blank=False)

    email = models.EmailField(null=False, blank=False)
    billing_name = models.CharField(max_length=60, null=False,
                                    blank=False,
                                    default="")
    address_line_1 = models.CharField(max_length=100, null=False,
                                      blank=False,
                                      default="")
    address_line_2 = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=25, null=False, blank=False, default="")
    postcode = models.CharField(max_length=10, null=False,
                                blank=False, default="")

    date = models.DateTimeField(auto_now=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0.00)
    status = models.CharField(choices=STATUS,
                              max_length=9,
                              blank=False,
                              default="Ordered")

    def __str__(self):
        return f"Order for {self.name}"


class OrderLineItem(models.Model):
    """
    Stores multiple entries for :Model:`PizzaOrder`.
    """

    order = models.ForeignKey(PizzaOrder, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name="pizzaorderlineitems")
    product = models.CharField(max_length=96, null=False,
                               editable=False, default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(null=False, blank=False)
    line_total = models.DecimalField(max_digits=6, decimal_places=2,
                                     null=False, editable=False)

    def __str__(self):
        return ""
