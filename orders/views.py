from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from orders.models import *


def add_to_basket(request):
    book_id = request.POST.get('book_id')
    user_id = request.POST.get('user_id')

    user = User.objects.get(id=user_id)
    book = Book.objects.get(id=book_id)

    basket, created = Basket.objects.get_or_create(user=user)
    basket.save()
    basket_element = BasketElement(basket=basket, book=book)
    basket_element.save()

    return HttpResponse()


def checkout(request, user_id):
    basket = User.objects.get(id=user_id).basket

    books = []
    for item in basket.basketelement_set.all():
        books.append(item.book)

    return render(request, 'frontend/checkout.html', locals())
