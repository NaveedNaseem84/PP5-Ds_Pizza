from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout_view, name='checkout'),
    path('success/<order_ref>', views.success_page, name='success_page'),
    
]