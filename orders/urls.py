from django.urls import path
from . import views

urlpatterns = [
    path('add_to_basket', views.add_to_basket, name='add_to_basket'),
    path('checkout/<int:user_id>/', views.checkout, name='checkout'),
]
