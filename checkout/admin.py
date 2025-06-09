from django.contrib import admin
from .models import PizzaOrder, OrderLineItem


class PizzaOrderLineAdmin(admin.TabularInline):
    model = OrderLineItem
    fields = (
        'quantity',
        'product',
        'price',
        'line_total'
    )
    readonly_fields = (
        'line_total',
        'product',
        'price',
        'quantity',
    )


class PizzaOrderAdmin(admin.ModelAdmin):

    inlines = (PizzaOrderLineAdmin,)

    readonly_fields = (
        'user',
        'order_ref',
        'date',
        'order_total',
        'billing_name',
        'address_line_1',
        'address_line_2',
        'town',
        'postcode',
    )

    fields = (
        'user',
        'order_ref',
        'date',
        'name',
        'phone',
        'email',
        'billing_name',
        'address_line_1',
        'address_line_2',
        'town',
        'postcode',
        'order_total',
        'status',
    )

    list_display = (
        'order_ref',
        'name',
        'date',
        'order_total',
        'status',
    )

    search_fields = ['name', 'order_ref']
    list_filter = ['status']


admin.site.register(PizzaOrder, PizzaOrderAdmin)
