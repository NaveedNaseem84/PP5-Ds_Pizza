from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout_view, name='checkout'),
    path('myorders/', views.my_orders, name='my_orders'),
    path('success/<order_ref>', views.success_page, name='success_page'),
    path('wh/', webhook, name='webhook'),
]
