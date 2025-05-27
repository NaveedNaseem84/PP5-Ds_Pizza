from django.db import models

ACTIVE_CHOICES = [
        ("Yes", "Yes"),
        ("No", "No"),
    ]

class Pizza(models.Model):
    """
    A single instance of the pizza model
    """

    ALLERGEN_CHOICES = [
        ("VG", "VG"),
        ("PB", "PB"),
        ("GF", "GF",)
    ]

    name = models.CharField(max_length=120,
                            unique=True)

    description = models.TextField(blank=True)

    active = models.CharField(choices=ACTIVE_CHOICES,
                              max_length=3,
                              blank=False,
                              default="No")

    is_gf = models.CharField(choices=ACTIVE_CHOICES,
                             blank=True,
                             max_length=3)

    is_veg = models.CharField(choices=ACTIVE_CHOICES,
                              blank=True,
                              max_length=3)

    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Artisan Pizzas"


class Extras(models.Model):
    """
    Holds a single instance of a drink, side or dessert.
    """
    CATEGORIES_CHOICES = [
        ("Desserts", "Desserts"),
        ("Drinks", "Drinks"),
        ("Sides", "Sides"),
    ]

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    category = models.CharField(choices=CATEGORIES_CHOICES,
                                max_length=10,
                                blank=False)

    active = models.CharField(choices=ACTIVE_CHOICES,
                              max_length=3,
                              blank=False,
                              default="No")

    price = models.DecimalField(max_digits=6, decimal_places=2) 

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Desserts, Drinks and Sides"


class Deal(models.Model):
    """
    A deal consisting of a pizza, one side, one drink, and one dessert.
    """

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    pizza = models.ForeignKey(
        Pizza,
        on_delete=models.CASCADE,
        limit_choices_to={'active': 'Yes'},
        related_name='deals'
    )

    side = models.ForeignKey(
        Extras,
        on_delete=models.CASCADE,
        limit_choices_to={'category': 'Sides', 'active': 'Yes'},
        related_name='side_deals'
    )

    drink = models.ForeignKey(
        Extras,
        on_delete=models.CASCADE,
        limit_choices_to={'category': 'Drinks', 'active': 'Yes'},
        related_name='drink_deals'
    )

    dessert = models.ForeignKey(
        Extras,
        on_delete=models.CASCADE,
        limit_choices_to={'category': 'Desserts', 'active': 'Yes'},
        related_name='dessert_deals'
    )

    price = models.DecimalField(max_digits=6, decimal_places=2)

    active = models.CharField(choices=ACTIVE_CHOICES,
                              max_length=3,
                              blank=False,
                              default="No")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Combo Deals"

