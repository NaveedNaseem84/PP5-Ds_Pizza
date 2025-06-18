from django.contrib import admin
from .models import Pizza, Extras, Deal


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    """
    Admin Panel structure for Pizza Model
    """

    list_display = ('name', 'is_gf', 'is_veg', 'price', 'active')
    search_fields = ['name', 'is_gf', 'is_veg', 'active']
    list_filter = ('is_gf', 'is_veg', 'active')


@admin.register(Extras)
class ExtrasAdmin(admin.ModelAdmin):
    """
    Admin panel structure for the Extras model
    """

    list_display = ('name', 'description', 'category', 'price', 'active')
    search_fields = ['name', 'category', 'active']
    list_filter = ('category', 'active')


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    """
    Admin panel structure for the extras model
    """
    list_display = (
        'name', 'pizza', 'side', 'drink',
        'dessert', 'price', 'active'
        )
    search_fields = ['name', 'active']
    list_filter = ['active']
