from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add/', views.add_to_bag, name='add_to_bag'),

    path(
        'increase/<item_id>/<item_type>',
        views.increase_from_bag,
        name='increase_from_bag'
        ),

    path('decrease/<item_id>/<item_type>',
         views.decrease_from_bag,
         name='decrease_from_bag'
         ),
]
