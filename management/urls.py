from django.urls import path
from . import views

urlpatterns = [
    path('', views.management_view, name='management'),
    path('add/item/', views.add_product, name='add_product'),
    path('update/int:<product_id>', views.update_product, name='update_product'),
    path('update_status/int:<order_id>', views.update_order_status, name='update_order_status'),    
]