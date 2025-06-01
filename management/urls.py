from django.urls import path
from . import views

urlpatterns = [
    path('', views.management_view, name='management'),
    path('add/pizza/', views.add_pizza, name='add_pizza'),
    path('add/deal/', views.add_deal, name='add_deal'),
    
]