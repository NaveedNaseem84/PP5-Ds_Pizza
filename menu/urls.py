from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu_view, name='menu'),
    path('product_detail/<product_id>', views.product_detail, name='product_detail'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product')  
]