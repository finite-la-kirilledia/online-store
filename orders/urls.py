from django.urls import path
from . import views

urlpatterns = [
    path('add_to_basket', views.add_to_basket, name='add_to_basket'),
    path('checkout/<int:user_id>', views.checkout, name='checkout'),
    path('delete_from_basket/<int:user_id>/<int:book_id>', views.delete_from_basket, name='delete_from_basket'),
    path('book/is_in_basket', views.is_in_basket, name='is_in_basket'),
    path('book/delete_book_from_basket', views.delete_book_from_basket, name='delete_book_from_basket'),
]
