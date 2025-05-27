from django.urls import path
from . import views

urlpatterns = [
    path('', views.management_view, name='management'),
    
]