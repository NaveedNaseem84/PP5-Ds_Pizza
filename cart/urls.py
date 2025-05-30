from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add/', views.add_to_bag, name='add_to_bag'),
    
]